import argparse
from etl import template_fit, etl
from motion.squat import Squat
from predict import score, overlay

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--front_view_image", help="image containing the front view of the user")
    parser.add_argument("-p", "--profile_view_image", help="image containing the profile view of the user")
    parser.add_argument("-v", "--motion_video", help="video containing the user performing a motion")
    args = parser.parse_args()

    # Find the front and profile skeletons
    print("Fitting images")
    front_view_points, profile_view_points = template_fit.get_points(args.front_view_image, args.profile_view_image)

    # Use the skeletons to start the motion
    print("Starting Motion")
    motion = Squat(front_view_points, profile_view_points)

    # Find the user skeletons throughout the video
    print("Fitting Video")
    user_skeletons = etl.get_user_skeletons(args.motion_video)

    # Find when the user was in a benchmark zone
    print("Finding benchmark zones")
    benchmark_zone_skeletons = motion.find_benchmark_zones_of_user(user_skeletons)

    # Overlay the template skeletons on the user's video
    print("Overlaying Video")
    overlay.display_overlay(args.motion_video, motion.template_skeletons)

    # Score the user's benchmark zones
    print("Calculating Score")
    score = score.compute_score(benchmark_zone_skeletons, motion.score)
    print(score)
