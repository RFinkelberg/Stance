import cv2

"""
@author: Vikas Gupta
@organization: LearnOpenCV
@see: https://www.learnopencv.com/deep-learning-based-human-pose-estimation-using-opencv-cpp-python/
@see: https://github.com/spmallick/learnopencv/blob/master/OpenPose/OpenPoseImage.py
"""


def get_points_from_image(image, get_points):
    """
    COCO Output Format
    Neck – 1, Right Shoulder – 2, Right Elbow – 3, Right Wrist – 4,
    Left Shoulder – 5, Left Elbow – 6, Left Wrist – 7, Right Hip – 8,
    Right Knee – 9, Right Ankle – 10, Left Hip – 11, Left Knee – 12,
    LAnkle – 13

    Parameters
    ----------
    image : ndarray
        numpy array containing image

    get_points : List[Int]
        COCO Indices of points to retrieve

    Returns
    -------
    points : List[Tuple[int, int]]
        points relating to body parts of the user from the image
        a certain point is None if no relative point is found
    """
    proto_file = "../../model/pose_deploy_linevec.prototxt"
    weights_file = "../../model/pose_iter_440000.caffemodel"
    n_points = 18

    frame = image
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
    threshold = 0.1

    net = cv2.dnn.readNetFromCaffe(proto_file, weights_file)

    # input image dimensions for the network
    in_weight = 368  # frame.shape[1]
    in_height = 368  # frame.shape[0]
    inp_blob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (in_weight, in_height),
                                     (0, 0, 0), swapRB=False, crop=False)

    net.setInput(inp_blob)

    output = net.forward()

    h = output.shape[2]
    w = output.shape[3]

    # Empty list to store the detected keypoints
    points = []

    get_points = set(get_points)
    for i in range(n_points):
        if i in get_points:
            # confidence map of corresponding body's part.
            prob_map = output[0, i, :, :]

            # Find global maxima of the probMap.
            _, prob, _, point = cv2.minMaxLoc(prob_map)

            # Scale the point to fit on the original image
            x = (frame_width * point[0]) / w
            y = (frame_height * point[1]) / h

            if prob > threshold:
                # Add the point to the list if the probability is greater than the threshold
                points.append((int(x), int(y)))
            else:
                points.append(None)
        else:
            points.append(None)

    return points
