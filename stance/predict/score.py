def compute_score(user_skeletons, scorer):
    """
    Uses the user skeletons and scorer method to calculate
    how well the user is performing the motion

    Parameters
    ----------
    user_skeletons : List[Skeletons]
        The Skeletons found to be in the benchmark zones
    scorer : method used to compute the score

    Returns
    -------
    score : integer
            integer score ranging from [0, 100] where 100 is a perfect motion.

    """
    return scorer(user_skeletons)
