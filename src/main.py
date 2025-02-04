import argparse
from fps_converter import FPS_Converter

def main():
    parser = argparse.ArgumentParser(description="Convert video to a specific FPS")

    parser.add_argument('--input', type=str, required=True, help='Input video file (without extension)')
    parser.add_argument('--output', type=str, required=False, help='Output video file (without extension)')
    parser.add_argument('--fps', type=int, required=True, help='Desired frames per second (FPS)')
    parser.add_argument('--threshold', type=int, required=False, help='Threshold to detect significant change')
    parser.add_argument('--disable_logging', type=bool, required=False, help='Threshold to detect significant change')

    args = parser.parse_args()

    FPS_Converter(video_name=args.input, output_name=args.output, new_fps_amount=args.fps, threshold=args.threshold, enable_default_logging= not args.disable_logging)

if __name__ == "__main__":
    main()
