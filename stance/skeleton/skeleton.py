import numpy as np
from typing import Dict, Tuple, Sequence


COCOPts = Sequence[Tuple[float, float]]


class SKVector(object):
    def __init__(self, head: Tuple[float, float], tail: Tuple[float, float]) -> None:
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
        self.vectors: Dict[str, SKVector] = {
            'l_lower_leg': SKVector(head=coco_points[13], tail=coco_points[12]),
            'r_lower_leg': SKVector(head=coco_points[10], tail=coco_points[9]),
            'l_upper_leg': SKVector(head=coco_points[12], tail=coco_points[11]),
            'r_upper_leg': SKVector(head=coco_points[9], tail=coco_points[8]),
            'l_spine': SKVector(head=coco_points[11], tail=coco_points[1]),
            'r_spine': SKVector(head=coco_points[8], tail=coco_points[1])
        }


    def __getitem__(self, key: str) -> SKVector:
        """ 
        Gets a certain SKVector from the skeleton

        Parameters
        ----------
        key : str
            key of vector to get

        Returns
        -------
        SKVector
            Corresponding vector in skeleton
        """
        return self.vectors[key]
