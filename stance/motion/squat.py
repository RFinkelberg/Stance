from .Motion import Motion
import json
from skeleton.skeleton import Skeleton, SKVector
import math


class Squat(Motion):
    def __init__(self, front_view_points, profile_view_points):
        self.template_skeletons = self.create_template_skeletons(front_view_points, profile_view_points)

    # --------------- IMPLEMENTED ABSTRACT METHODS ------------------

    @staticmethod
    def find_benchmark_zones_of_user(user_skeletons):
        """
        SEE MOTION DOCSTRING
        """
        # --------------- SKELETON SIMILARITY SCORES ------------------
        def _0_similarity(user_skeleton):
            # TODO Implement this method
            return 0

        def _1_similarity(user_skeleton):
            # TODO Implement this method
            return 1

        def _2_similarity(user_skeleton):
            # TODO Implement this method
            return 2

        def _3_similarity(user_skeleton):
            # TODO Implement this method
            return 3

        def _4_similarity(user_skeleton):
            # TODO Implement this method
            return 4

        similarity_scorers = [_0_similarity, _1_similarity, _2_similarity,
                              _3_similarity, _4_similarity]

        idxs = range(len(user_skeletons))
        return [min(idxs, key=lambda i: scorer(i))
                for scorer in similarity_scorers]

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

    @staticmethod
    def score(user_skeletons):

        # --------------- SKELETON SCORERS ------------------
        # Each score is from range [0, 20] so that total is out of 100

        def _0_score(user_skeleton):
            # TODO Implement this method
            return 0

        def _1_score(user_skeleton):
            # TODO Implement this method
            return 1

        def _2_score(user_skeleton):
            # TODO Implement this method
            return 2

        def _3_score(user_skeleton):
            # TODO Implement this method
            return 3

        def _4_score(user_skeleton):
            # TODO Implement this method
            return 4

        scorers = [_0_score, _1_score, _2_score, _3_score, _4_score]
        assert len(user_skeletons) == len(scorers), "Must have as many skeletons as scorers"
        return sum(scorer(skeleton) for scorer, skeleton in zip(scorers, user_skeletons))
