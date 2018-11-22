import argparse
import logging
import pickle
from time import time

from etl import template_fit, etl
from motion.squat import Squat
from predict import score, overlay


def main():
    # Example calling: python main.py -v etl/squat.mp4
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--video_path", help="filepath to video containing the user performing a motion")
    parser.add_argument("-v", "--verbose", help="Verbosity level. 1 (v) displays info, 2 (vv) displays debug logs",
                        action="count")
    parser.add_argument("-p", "--use_pickle", help="uses the pickle file corresponding to the video file given",
                        action="store_true")
    args = parser.parse_args()

    verbosity = args.verbose or 0
    logger.setLevel(logging.WARNING - (10 * verbosity))
    logger.info("Starting Motion")

    # Set the motion to be Squat
    motion = Squat(verbose=verbosity)

    # Find the user skeletons throughout the video
    logger.info("Fitting Video")
    if not args.use_pickle:
        user_skeletons = etl.get_user_skeletons(args.video_path)
    elif args.video_path == "example/squat.mp4":
        with open("squat_user_skeletons.json", "rb") as fp:
            user_skeletons = pickle.load(fp)
    elif args.video_path == "example/squatbad.mp4":
        with open("squatbad_user_skeletons.json", 'rb') as fp:
            user_skeletons = pickle.load(fp)
    elif args.video_path == "example/squatpoop.mp4":
        with open("squatterrible_user_skeletons.json", 'rb') as fp:
            user_skeletons = pickle.load(fp)
    else:
        logger.error("Error parsing command line arguments")
        raise ValueError("The pickle for the motion video {} given has not been computed,"
                         " please run without --use_pickle".format(args.video_path))

    # Find when the user was in a benchmark zone
    logger.info("Finding Benchmark Zones")
    t0 = time()
    benchmark_zone_skeletons = motion.find_benchmark_zones_of_user(user_skeletons)
    benchmark_zone_indices = motion.find_benchmark_indices_of_user(user_skeletons)
    logger.info("Found Benchmark Zones in {:.3f} sec".format(time() - t0))

    # Overlay the template skeletons on the user's video
    logger.info("Overlaying Video")
    overlay.display_overlay(args.video_path, motion.template_skeletons)
    # overlay.compare_user_skeletons(args.motion_video, benchmark_zone_indices, user_skeletons, motion)

    # Score the user's benchmark zones
    logger.info("Calculating Score")
    user_score = score.compute_score(benchmark_zone_skeletons, motion.score)
    print("Final Score: {}".format(user_score))


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                           '%H:%M:%S'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    main()
