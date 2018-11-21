import argparse
from etl import template_fit, etl
from motion.squat import Squat
from predict import score, overlay
import pickle

if __name__ == "__main__":
    # Example calling: python main.py -v etl/squat.mp4
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--motion_video", help="filepath to video containing the user performing a motion")
    parser.add_argument("-p", "--use_pickle",
                        help="Number in range(0, 3) which signifies which pickled file to test the code without "
                             "running the neural network")
    args = parser.parse_args()

    print("Starting Motion")
    # Set the motion to be Squat
    motion = Squat()

    # Find the user skeletons throughout the video
    print("Fitting Video")
    if not args.use_pickle:
        user_skeletons = etl.get_user_skeletons(args.motion_video)
    elif args.use_pickle == str(0):
        args.motion_video = "example/squat.mp4"
        with open("squat_user_skeletons.json", "rb") as fp:
            user_skeletons = pickle.load(fp)
    elif args.use_pickle == str(1):
        args.motion_video = "example/squatbad.mp4"
        with open("squatbad_user_skeletons.json", 'rb') as fp:
            user_skeletons = pickle.load(fp)
    elif args.use_pickle == str(2):
        args.motion_video = "example/squatpoop.mp4"
        with open("squatterrible_user_skeletons.json", 'rb') as fp:
            user_skeletons = pickle.load(fp)
    else:
        raise Exception("Unknown pickle number, try a number from 0 to 2")

    # Find when the user was in a benchmark zone
    print("Finding benchmark zones")
    benchmark_zone_skeletons = motion.find_benchmark_zones_of_user(user_skeletons)
    benchmark_zone_indices = motion.find_benchmark_indices_of_user(user_skeletons)

    # Overlay the template skeletons on the user's video
    print("Overlaying Video")
    overlay.display_overlay(args.motion_video, motion.template_skeletons)
    # overlay.compare_user_skeletons(args.motion_video, benchmark_zone_indices, user_skeletons, motion)

    # Score the user's benchmark zones
    print("Calculating Score")
    score = score.compute_score(benchmark_zone_skeletons, motion.score)
    print(score)
