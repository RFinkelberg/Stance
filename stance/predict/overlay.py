import cv2
import matplotlib.pyplot as plt


def display_overlay(input_video, template_skeletons):
    """
    This method displays the correct template skeleton the user is supposed to be
    mimicking on top of the user while performing the motion

    Parameters
    ----------
    input_video : String
        path to the video of the user performing the motion
    template_skeletons : List[Skeletons]
    """
    pass


def compare_user_skeletons(input_video, idxs, user_skeletons, motion):
    raw_score = motion.raw_scores(user_skeletons)
    vid_obj = cv2.VideoCapture(input_video)
    success = 1
    i = 0
    plt.figure()
    subplot_num = 1
    while success:
        success, image = vid_obj.read()
        if image is None:
            break
        if i in idxs:
            print(i, subplot_num)
            plt.subplot(2, 5, subplot_num)
            plt.title(str(raw_score[subplot_num - 1]))
            subplot_num += 1
            plt.imshow(image)
        i += 1

    vid_obj = cv2.VideoCapture("etl/squat.mp4")
    success = 1
    i = 0
    while success:
        success, image = vid_obj.read()
        if image is None:
            break
        if i in [12, 32, 79, 105, 129]:
            print(i, subplot_num)
            plt.subplot(2, 5, subplot_num)
            subplot_num += 1
            plt.imshow(image)
        i += 1

    plt.show()
