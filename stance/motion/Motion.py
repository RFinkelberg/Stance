from abc import ABC, abstractmethod


class Motion(ABC):
    @abstractmethod
    def create_template_skeletons(self):
        """
        Using the body points from a user standing from two views, create
        template skeletons for benchmark zones that define the specific motion.

        Returns
        -------
        template_skeletons : List[Skeletons]
            one skeleton for each benchmark zone which define the perfect
            skeleton the user would have at that time in the motion.

        """
        raise NotImplementedError

    @abstractmethod
    def find_benchmark_zones_of_user(self, user_skeletons):
        """
        Find which user skeletons map closest to the template
        skeletons

        Parameters
        ----------
        user_skeletons : List[Skeletons]

        Returns
        -------
        benchmark_zones : List[Skeletons]
            list of skeletons representing the benchmark zones

        """
        raise NotImplementedError

    @abstractmethod
    def score(self, user_skeletons):
        """
        Uses user's skeleton to make a score value that defines how close the user
        is to performing the motion perfectly.

        Parameters
        ----------
        user_skeletons : List[Skeletons]

        Returns
        -------
        score : integer
            integer score ranging from [0, 100] where 100 is a perfect motion.
        """
        raise NotImplementedError
