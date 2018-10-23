import argparse
import template_fit

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--front_view_image", help="image containing the front view of the user")
    parser.add_argument("-p","--profile_view_image", help="image containing the profile view of the user")
    parser.add_argument("-v","--motion_video", help="video containing the user performing a motion")
    args = parser.parse_args()

    template_fit.template_fitting(args.front_view_image, args.profile_view_image)
