import argparse
from etl import template_fit, etl
from motion.squat import Squat
from predict import score, overlay
import pickle

if __name__ == "__main__":
    # Example calling: python main.py -v etl/squat.mp4
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--motion_video", help="filepath to video containing the user performing a motion")
    args = parser.parse_args()

    print("Starting Motion")
    # Set the motion to be Squat
    motion = Squat()

    # Find the user skeletons throughout the video
    print("Fitting Video")
    user_skeletons = etl.get_user_skeletons(args.motion_video)
    # with open("squat_user_skeletons.json", "rb") as fp:  # Use with etl/squat.mp4
    #     user_skeletons = pickle.load(fp)
    # with open("squatbad_user_skeletons.json", 'rb') as fp:  # Use with etl/squatbad.mp4
    #     user_skeletons = pickle.load(fp)
    # with open("squatterrible_user_skeletons.json", 'rb') as fp:  # Use with etl/squatpoop.mp4
    #     user_skeletons = pickle.load(fp)

    # Find when the user was in a benchmark zone
    print("Finding benchmark zones")
    benchmark_zone_skeletons = motion.find_benchmark_zones_of_user(user_skeletons)
    benchmark_zone_indices = motion.find_benchmark_indices_of_user(user_skeletons)

    # Overlay the template skeletons on the user's video
    print("Overlaying Video")
    overlay.display_overlay(args.motion_video, motion.template_skeletons)

    # Score the user's benchmark zones
    print("Calculating Score")
    score = score.compute_score(benchmark_zone_skeletons, motion.score)
    print(score)
