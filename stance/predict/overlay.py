import cv2
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
    benchmark_indices : List[ints]
        frames where benchmark skeletons should be overlayed
    user_skeletons : List[Skeletons]
        user's skeleton for each frame of the video
    """
    cap = cv2.VideoCapture(input_video)
    numFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # used for scaling template skeleton to user video
    # 1280 and 720 are the dimensions of the template video
    scale_x = width / 1280
    scale_y = height / 720
    count = 0

    out = cv2.VideoWriter('output.mp4', -1, 20.0, (width, height))

    for i in range(numFrames):
        _, frame = cap.read()

        # User skeleton
        try:
            temp = list(user_skeletons[i].vectors.values())
        except IndexError:
            break
        for points in temp:
            if points is not None:
                pointA = (points.head[0], points.head[1])
                pointB = (points.tail[0], points.tail[1])
                cv2.line(frame, pointA, pointB, (0, 255, 255), 4)

        # Template skeleton (scale and translate to align with center of gravity)
        if count < len(benchmark_indices) and i == benchmark_indices[count]:
            temp_skeleton = template_skeletons[count]
            temp = list(temp_skeleton.vectors.values())
            count += 1
            # calculate how much to shift the scaled template skeleton by
            user_center = user_skeletons[i].vectors['l_spine'].head
            temp_center = temp_skeleton.vectors['l_spine'].head
            dif_x = temp_center[0] * scale_x - user_center[0]
            dif_y = temp_center[1] * scale_y - user_center[1]
            for points in temp:
                if points is not None:
                    pointA = (int(points.head[0] * scale_x - dif_x), int(points.head[1] * scale_y - dif_y))
                    pointB = (int(points.tail[0] * scale_x - dif_x), int(points.tail[1] * scale_y - dif_y))
                    cv2.line(frame, pointA, pointB, (0, 255, 0), 4)
        if frame is not None:
            cv2.imshow('Frame', frame)
            out.write(frame)
        # pause video when skeleton is visible
        if i == benchmark_indices[count - 1] + 1:
            time.sleep(1)
        if cv2.waitKey(70) & 0xFF == ord('q'):
            break
        if i == benchmark_indices[count - 1]:
            for j in range(20):
                out.write(frame)

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
