from .motion import Motion
import numpy as np


class Squat(Motion):
    def __init__(self, front_view_points, profile_view_points):
        self.template_skeletons = self.create_template_skeletons(front_view_points, profile_view_points)
        self.benchmark_zones = [self._0, self._1, self._2, self._3, self._4]
        self.similarity_scorers = [self._0_similarity, self._1_similarity,
                                   self._2_similarity, self._3_similarity, self._4_similarity]

    # --------------- IMPLEMENTED ABSTRACT METHODS ------------------

    def find_benchmark_zones_of_user(self, user_skeletons):
        """
        SEE MOTION DOCSTRING
        """
        benchmark_zone_indices = []
        for similarity_scorer in self.similarity_scorers:
            score_array = np.array([])
            for user_skeleton in user_skeletons:
                np.append(score_array, similarity_scorer(user_skeleton))
            index_array = np.argmin(score_array)
            benchmark_zone_indices.append(index_array[0])
        return benchmark_zone_indices

    def create_template_skeletons(self, front_view_points, profile_view_points):
        # TODO Implement this method
        return [0, 1, 2, 3, 4]

    def score(self, user_skeletons):
        # TODO Implement this method
        return 100

    # --------------- BENCHMARK ZONES ------------------

    def _0(self, front_view_points, profile_view_points):
        # TODO Implement this method
        return 0

    def _1(self, front_view_points, profile_view_points):
        # TODO Implement this method
        return 1

    def _2(self, front_view_points, profile_view_points):
        # TODO Implement this method
        return 2

    def _3(self, front_view_points, profile_view_points):
        # TODO Implement this method
        return 3

    def _4(self, front_view_points, profile_view_points):
        # TODO Implement this method
        return 4

    # --------------- SKELETON SIMILARITY SCORES ------------------

    def _0_similarity(self, user_skeleton):
        # TODO Implement this method
        return 0

    def _1_similarity(self, user_skeleton):
        # TODO Implement this method
        return 1

    def _2_similarity(self, user_skeleton):
        # TODO Implement this method
        return 2

    def _3_similarity(self, user_skeleton):
        # TODO Implement this method
        return 3

    def _4_similarity(self, user_skeleton):
        # TODO Implement this method
        return 4
