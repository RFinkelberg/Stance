import numpy as np


class Skeleton:
    def __init__(self, coco_points):
        """
        Uses the output from the COCO model to create body variables

        Parameters
        ----------
        coco_points : List[Points]
            points in the COCO format
        """
        self.neck = coco_points[1]
        self.right_shoulder = coco_points[2]
        self.right_elbow = coco_points[3]
        self.right_wrist = coco_points[4]
        self.left_shoulder = coco_points[5]
        self.left_elbow = coco_points[6]
        self.left_wrist = coco_points[7]
        self.right_hip = coco_points[8]
        self.right_knee = coco_points[9]
        self.right_ankle = coco_points[10]
        self.left_hip = coco_points[11]
        self.left_knee = coco_points[12]
        self.left_ankle = coco_points[13]
        self.body_points = [self.neck, self.right_shoulder, self.right_elbow, self.right_wrist,
                            self.left_shoulder, self.left_elbow, self.left_wrist, self.right_hip,
                            self.right_knee, self.right_ankle, self.left_hip, self.left_knee,
                            self.left_ankle]

    def centered_points(self):
        """
        Computes the points but changes the origin to where the right ankle is.
        
        Returns
        -------
        centered_body_points : List[Points]
        """
        centered_body_points = []
        for body_point in self.body_points:
            centered_body_points.append(tuple(np.subtract(body_point, self.right_ankle)))
        return centered_body_points
