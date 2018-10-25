import argparse
import template_fit
from Stance.stance.motion.squat import Squat

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--front_view_image", help="image containing the front view of the user")
    parser.add_argument("-p", "--profile_view_image", help="image containing the profile view of the user")
    parser.add_argument("-v", "--motion_video", help="video containing the user performing a motion")
    args = parser.parse_args()

    front_view_points, profile_view_points = template_fit.get_points(args.front_view_image, args.profile_view_image)

    motion = Squat(front_view_points, profile_view_points)
