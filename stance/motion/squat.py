from .motion import Motion


class Squat(Motion):
    def __init__(self, front_view_points, profile_view_points):
        self.template_skeletons = self.create_template_skeletons(front_view_points,
                                                                 profile_view_points)

    # --------------- IMPLEMENTED ABSTRACT METHODS ------------------

    def find_benchmark_zones_of_user(self, user_skeletons):
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

        # --------------- BENCHMARK ZONES ------------------
        def _0(front_view_points, profile_view_points):
            # TODO Implement this method
            return 0

        def _1(front_view_points, profile_view_points):
            # TODO Implement this method
            return 1

        def _2(front_view_points, profile_view_points):
            # TODO Implement this method
            return 2

        def _3(front_view_points, profile_view_points):
            # TODO Implement this method
            return 3

        def _4(front_view_points, profile_view_points):
            # TODO Implement this method
            return 4

        return [zone(front_view_points, profile_view_points) for zone in self.benchmark_zones]


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
        return sum(scorer(skeleton) for scorer, skeleton in zip(scorers,
                                                                user_skeletons))
