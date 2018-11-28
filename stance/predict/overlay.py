import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time


def display_overlay(input_video, template_skeletons, benchmark_indices, user_skeletons):
    """
    This method displays the correct template skeleton the user is supposed to be
    mimicking on top of the user while performing the motion

    Parameters
    ----------
    input_video : String
        path to the video of the user performing the motion
    template_skeletons : List[Skeletons]
    """
    cap = cv2.VideoCapture(input_video)
    numFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(width, height)
    count = 0

    for i in range(numFrames):
        _, frame = cap.read()
        temp = list(user_skeletons[i].vectors.values())
        for points in temp:
            if points is not None:
                pointA = (points.head[0], points.head[1])
                pointB = (points.tail[0], points.tail[1])
                cv2.line(frame, pointA, pointB, (0, 255, 255), 4)

        # Template skeleton
        if count < len(benchmark_indices) and i == benchmark_indices[count]:
            temp = list(template_skeletons[count].vectors.values())
            count += 1
            for points in temp:
                if points is not None:
                    pointA = (points.head[0], points.head[1])
                    pointB = (points.tail[0], points.tail[1])
                    cv2.line(frame, pointA, pointB, (255, 0, 0), 4)
        if frame is not None:
            cv2.imshow('Frame', frame)
        # pause video when skeleton is visible
        if i == benchmark_indices[count - 1] + 1:
            time.sleep(1)
        if cv2.waitKey(70) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


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
