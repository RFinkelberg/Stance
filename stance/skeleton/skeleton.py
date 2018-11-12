import numpy as np
from typing import Dict, Tuple, Sequence, Optional


Point = Tuple[float, float]
COCOPts = Sequence[Point]


class SKVector(object):
    def __init__(self, head: Point, tail: Point) -> None:
        self.head: np.ndarray = np.array(head)
        self.tail: np.ndarray = np.array(tail)
        self.vec = self.head - self.tail


    def cos_similarity(self, other: 'SKVector') -> float:
        """
        Computes the cosine similarity between this vector and another, defined
        as the normalized inner product between them

        Parameters
        ----------
        other : SKVector
            another vector

        Returns
        -------
        float
            cosine similarity between self and other. Approaches -1 or 1 for linearly
            dependent vectors and 0 for completely orthogonal vectors
        """
        magnitude = np.linalg.norm(self.vec) * np.linalg.norm(other.vec)
        return np.dot(self.vec, other.vec) / magnitude


    def __repr__(self) -> str:
        return 'SKVector: {} -> {}'.format(tuple(self.head), tuple(self.tail))


class Skeleton(object):
    def __init__(self, coco_points: COCOPts) -> None:
        """
        Uses the output from the COCO model to create body variables

        Parameters
        ----------
        coco_points : COCOPts
            points in the COCO format
        """
        self.body_points = coco_points
        self.vectors: Dict[str, Optional[SKVector]] = {
            'l_lower_leg': Skeleton.create_vector(coco_points[13], coco_points[12]),
            'r_lower_leg': Skeleton.create_vector(coco_points[10], coco_points[9]),
            'l_upper_leg': Skeleton.create_vector(coco_points[12], coco_points[11]),
            'r_upper_leg': Skeleton.create_vector(coco_points[9], coco_points[8]),
            'l_spine': Skeleton.create_vector(coco_points[11], coco_points[1]),
            'r_spine': Skeleton.create_vector(coco_points[8], coco_points[1]),
            'l_lower_arm': Skeleton.create_vector(coco_points[7], coco_points[6]),
            'r_lower_arm': Skeleton.create_vector(coco_points[4], coco_points[3]),
            'l_upper_arm': Skeleton.create_vector(coco_points[6], coco_points[5]),
            'r_upper_arm': Skeleton.create_vector(coco_points[3], coco_points[2]),
            'l_upper_back': Skeleton.create_vector(coco_points[5], coco_points[1]),
            'r_upper_back': Skeleton.create_vector(coco_points[2], coco_points[1]),
        }


    @staticmethod
    def create_vector(head: Point, tail: Point) -> Optional[SKVector]:
        """
        Creates an SKVector from tail->head, or returns None if either point
        is invalid (that is, it wasn't found by COCO)
        """
        if head is None or tail is None:
            return None
        return SKVector(head=head, tail=tail)


    def __getitem__(self, key: str) -> Optional[SKVector]:
        """
        Gets a certain SKVector from the skeleton

        Parameters
        ----------
        key : str
            key of vector to get

        Returns
        -------
        Optional[SKVector]
            Corresponding vector in skeleton or None if the vector doesn't exist
        """
        return self.vectors[key]
