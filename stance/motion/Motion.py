from abc import ABC, abstractmethod


class Motion(ABC):
    @abstractmethod
    def create_template_skeletons(self, front_view_points, profile_view_points):
        """
        Using the body points from a user standing from two views, create
        template skeletons for benchmark zones that define the specific motion.

        Parameters
        ----------
        front_view_points : array of points of the front view of the user
            points in the style of the COCO output (defined in template_fit)

        profile_view_points : array of points of the profile of the user
            points in the style of the COCO output (defined in template_fit)

        Returns
        -------
        template_skeletons : array of skeletons
            one skeleton for each benchmark zone which define the perfect
            skeleton the user would have at that time in the motion.

        """
        pass

    @abstractmethod
    def skeleton_similarity(self, skeleton1, skeleton2):
        """
        Compares two skeletons to determine how similar the two skeletons are.

        Parameters
        ----------
        skeleton1 : An array of points defining a skeleton
        skeleton2 : An array of points defining a skeleton

        Returns
        -------
        similarity_score : float
            score from [0, inf) where 0 is a perfect match.

        """
        pass

    @abstractmethod
    def score(self, user_skeletons):
        """
        Uses user's skeleton to make a score value that defines how close the user
        is to performing the motion perfectly.

        Parameters
        ----------
        user_skeletons : An array of skeletons

        Returns
        -------
        score : integer
            integer score ranging from [0, 100] where 100 is a perfect motion.
        """
        pass
