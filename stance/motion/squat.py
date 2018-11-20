from functools import partial
from typing import Sequence

from skeleton.skeleton import Skeleton
from .Motion import Motion
import json
from skeleton.skeleton import Skeleton, SKVector
import math


class Squat(Motion):
    def __init__(self, front_view_points, profile_view_points):
        self.template_skeletons = self.create_template_skeletons(front_view_points,
                                                                 profile_view_points)

    # --------------- IMPLEMENTED ABSTRACT METHODS ------------------

    def find_benchmark_zones_of_user(self, user_skeletons: Sequence[Skeleton]) -> Sequence[Skeleton]:
        """
        SEE MOTION DOCSTRING
        """
        benchmark_zones = []
        for template in self.template_skeletons:
            cmp = partial(Squat.compare_skeletons, template)
            benchmark_zones.append(max(user_skeletons, key=cmp))
        return benchmark_zones


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



    def create_template_skeletons(self, front_view_points, profile_view_points):
        """
        See Motion Docstring
        """
        benchmark_zones = {}
        with open("etl/benchmark_zones.json", 'r') as fp:
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
            template_skeleton.normalize()
            return template_skeleton

        return [_find_template_skeleton(i) for i in range(5)]


    def score(self, user_skeletons):

        # --------------- SKELETON SCORERS ------------------
        # Each score is from range [0, 20] so that total is out of 100
        # TODO or we could just normalize

        # def _0_score(user_skeleton):
        #     # TODO Implement this method
        #     return 0

        # def _1_score(user_skeleton):
        #     # TODO Implement this method
        #     return 1

        # def _2_score(user_skeleton):
        #     # TODO Implement this method
        #     return 2

        # def _3_score(user_skeleton):
        #     # TODO Implement this method
        #     return 3

        # def _4_score(user_skeleton):
        #     # TODO Implement this method
        #     return 4

        # scorers = [_0_score, _1_score, _2_score, _3_score, _4_score]
        # assert len(user_skeletons) == len(scorers), "Must have as many skeletons as scorers"
        # return sum(scorer(skeleton) for scorer, skeleton in zip(scorers, user_skeletons))
        pass
