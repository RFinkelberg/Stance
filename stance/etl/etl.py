import time
import logging

import cv2

from etl import logger
from etl.template_fit import get_points_from_image
from skeleton.skeleton import Skeleton


def get_user_skeletons(video_input, get_points, verbose=0):
    """
    This function takes in a file path to a video of the user performing the motion. It then
    separates the video into frames and performing template_fit's get points from image
    to compute the wire skeleton.

    Parameters
    ----------
    video_input : String
        file path to the video source

    get_points : List[Int]
        COCO Indices of points to retrieve
    
    verbose : int
        verbosity

    Returns
    -------
    user_skeletons : List[Skeletons]

    """
    logger.setLevel(logging.WARNING - (10 * verbose))

    vid_obj = cv2.VideoCapture(video_input)

    user_skeletons = []

    success = 1
    i = 1
    while success:
        success, image = vid_obj.read()
        if image is None:
            break
        start_time = time.time()
        user_skeletons.append(Skeleton(get_points_from_image(image, get_points)))
        logger.debug("Processed frame {} in {} sec".format(i,
                                                           time.time() - start_time))
        i += 1

    return user_skeletons, i
