import numpy as np
from collections import namedtuple

COCOPts = namedtuple('COCOPts', ('nose',
                                 'neck',
                                 'right_shoulder',
                                 'right_elbow',
                                 'right_wrist',
                                 'left_shoulder',
                                 'left_elbow',
                                 'left_wrist',
                                 'right_hip',
                                 'right_knee',
                                 'right_ankle',
                                 'left_hip',
                                 'left_knee',
                                 'left_ankle'))


class Skeleton:
    def __init__(self, coco_points):
        """
        Uses the output from the COCO model to create body variables

        Parameters
        ----------
        coco_points : List[Points]
            points in the COCO format
        """
        self.body_points = COCOPts(coco_points)

    def centered_points(self):
        """
        Computes the points but changes the origin to where the right ankle is.
        
        Returns
        -------
        centered_body_points : List[Points]
        """
        centered_body_points = []
        for body_point in self.body_points:
            centered_body_points.append(tuple(np.subtract(body_point, self.body_points.right_ankle)))
        return centered_body_points
