from functools import partial
from typing import Sequence
import logging
import json

import matplotlib.pyplot as plt
import numpy as np

from motion import logger
from skeleton.skeleton import Skeleton
from .Motion import Motion


class Squat(Motion):
    def __init__(self, verbose: int = 0):
        self.template_skeletons = self.create_template_skeletons()
        logger.setLevel(logging.WARNING - (10 * verbose))

    # --------------- IMPLEMENTED ABSTRACT METHODS ------------------

    def find_benchmark_indices_of_user(self, user_skeletons: Sequence[Skeleton]) -> Sequence[Skeleton]:
        """
        SEE MOTION DOCSTRING
        """
        def gaussian(x, mu, sig) -> float:
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

        benchmark_zones = []
        score_array = []
        gaussian_dists = [(0 * 24 + 10, 20), (1 * 24 + 10, 20), (2 * 24 + 10, 20), (3 * 24 + 10, 20), (4 * 24 + 10, 20)]

        for template in self.template_skeletons:
            cmp = partial(Squat.compare_skeletons, template)
            # benchmark_zones.append(min(user_skeletons, key=cmp))
            # print(min(range(len(user_skeletons)), key=lambda i: cmp(user_skeletons[i])))
            score_array.append(list(map(cmp, user_skeletons)))
        xs = np.arange(0, len(user_skeletons), 1)
        for scores, (mu, sig) in zip(score_array, gaussian_dists):
            scores = [score + gaussian(x, mu, sig)/20 for x, score in zip(xs, scores)]
            benchmark_zones.append(int(np.argmax(np.array(scores))))
        return benchmark_zones

    def find_benchmark_zones_of_user(self, user_skeletons: Sequence[Skeleton]) -> Sequence[Skeleton]:
        """
        SEE MOTION DOCSTRING
        """
        def gaussian(x, mu, sig) -> float:
            return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

        benchmark_zones = []
        score_array = []
        gaussian_dists = [(0 * 24 + 10, 20), (1 * 24 + 10, 20), (2 * 24 + 10, 20), (3 * 24 + 10, 20), (4 * 24 + 10, 20)]

        for template in self.template_skeletons:
            cmp = partial(Squat.compare_skeletons, template)
            # benchmark_zones.append(min(user_skeletons, key=cmp))
            # print(min(range(len(user_skeletons)), key=lambda i: cmp(user_skeletons[i])))
            score_array.append(list(map(cmp, user_skeletons)))
        xs = np.arange(0, len(user_skeletons), 1)
        for scores, (mu, sig) in zip(score_array, gaussian_dists):
            scores = [score + gaussian(x, mu, sig)/20 for x, score in zip(xs, scores)]
            benchmark_zones.append(user_skeletons[int(np.argmax(np.array(scores)))])
            logger.debug("Found Benchmark zone: frame {}".format(np.argmax(np.array(scores))))
        return benchmark_zones
        # for template in self.template_skeletons:
        #     cmp = partial(Squat.compare_skeletons, template)
        #     benchmark_zones.append(list(map(cmp, user_skeletons)))
        # xs = np.arange(0, len(user_skeletons), 1)
        # colors = ('r-', 'g-', 'b-', 'o-', 'p-')
        # for c, scores, (mu, sig) in zip(colors, benchmark_zones, gaussian_dists):
        #     scores = [score + gaussian(x, mu, sig)/4 for x, score in zip(xs, scores)]
        #     plt.plot(xs, scores, c)
        # plt.show()

    @staticmethod
    def compare_skeletons(this, other: Skeleton) -> float:
        """
        Gives a normalized similarity score between two skeletons by summing
        the cosine similarities of each scored body part vector. If one or both
        vectors are None, then the similarity is defined to be 0

        Parameters
        ----------
        this, other : Skeleton
            Two skeletons to compare

        Returns
        -------
        float
            cumulative similarity score between this and other
        """
        scored_vectors = ('l_lower_leg', 'l_upper_leg', 'l_spine')

        def _compare(label: str):
            u = this.vectors[label]
            v = other.vectors[label]
            if u is None or v is None:
                return 0
            return u.cos_similarity(v)

        return sum(map(_compare, scored_vectors)) / (len(scored_vectors))

    def create_template_skeletons(self):
        """
        See Motion Docstring
        """
        benchmark_zones = {}
        with open("etl/squat_benchmark_zones.json", 'r') as fp:
            # Loads benchmark zone skeletons from JSON file
            benchmark_zones = json.load(fp)

        def _find_template_skeleton(skeleton_number):
            """
            Uses frames 12, 32, 79, 105, and 129 from etl/squat.mp4 to
            create normalized template skeletons that can be used for comparisons.

            Parameters
            ----------
            skeleton_number : int
                Number between 0 - 4 that represents which of the 5 benchmark skeletons to return.
            """
            template_coco_points = benchmark_zones[str(skeleton_number)]
            template_skeleton = Skeleton(template_coco_points)
            return template_skeleton

        return [_find_template_skeleton(i) for i in range(5)]

    def score(self, user_skeletons):
        """
        See Motion Docstring
        """
        # Each score total is out of 100
        weights = np.array([5, 20, 50, 20, 5])  # adds up to 100
        exponent_weights = np.array([1, 2, 20, 2, 1])
        scores = list(map(lambda p: Squat.compare_skeletons(p[0], p[1]) ** p[2],
                          zip(self.template_skeletons, user_skeletons, exponent_weights)))
        return np.dot(weights, scores)

    def raw_scores(self, user_skeletons):
        scores = list(map(lambda p: Squat.compare_skeletons(p[0], p[1]),
                          zip(self.template_skeletons, user_skeletons)))
        return scores
