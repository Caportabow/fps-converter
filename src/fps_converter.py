import os
import cv2
import numpy as np
from tqdm import tqdm

class FPS_Converter:
    def __init__(self, video_name: str, video_path: str = None, output_name: str = None, output_path: str = None, new_fps_amount: int = None, threshold: int = None, enable_default_logging: bool = True):
        """
        Changes the frames per second (FPS) of .mp4 videos using frame detection (OpenCV).

        Suitable for clips with unstable or choppy framerate, but compatible with any video.

        Args:
            video_name (str): The name of the video file without the extension.
            video_path (str, optional): Path to the video if it is located in subfolders (excluding the file name).
                Defaults to None, which means the current directory.
            output_name (str, optional): The name for the output file without the extension.
                Defaults to "{video_name}_out".
            output_path (str, optional): Path for the output file if it should be in a subfolder (excluding the file name).
                Defaults to None, which means the current directory.
            new_fps_amount (int, optional): Desired FPS for the output video.
                Defaults to 60 FPS.
            threshold (int, optional): Threshold to detect significant change.
                Defaults to 500. Not recommended to change.
            enable_default_logging (bool, optional): Enables or disables basic logging (start, processing, completion, etc.).
                Defaults to True.
        """
        # Check and set up video_name
        if not video_name:
            raise ValueError("The 'video_name' parameter is required.")
        self.video_name = video_name

        # Check and set up video_path
        self.video_path = video_path if video_path else ""
        if self.video_path and not os.path.exists(self.video_path):
            raise FileNotFoundError(f"The specified video path does not exist: {self.video_path}")

        # Check and set up output_name
        self.output_name = output_name if output_name else f"{video_name}_out"

        # Check and set up output_path
        self.output_path = output_path if output_path else ""
        if self.output_path:
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path)
                if enable_default_logging:
                    print(f"// Output directory created: {self.output_path}\n")

        # Check and set up new_fps_amount and threshold
        self.new_fps_amount = new_fps_amount if new_fps_amount else 60
        self.threshold = threshold if threshold else 500

        # Set logging options
        self._enable_default_logging = enable_default_logging

        # Construct the full input and output file paths
        self.full_input_path = os.path.join(self.video_path, f"{self.video_name}.mp4")
        if not os.path.isfile(self.full_input_path):
            raise FileNotFoundError(f"The specified video does not exist: {self.video_path}")

        self.full_output_path = os.path.join(self.output_path, f"{self.output_name}.mp4")

        if self._enable_default_logging:
            print("------ VARIABLES SETUP COMPLETE ------")
            print(f"Video Name: {self.video_name}")
            print(f"Full Input Path: {self.full_input_path}")
            print(f"Output Name: {self.output_name}")
            print(f"Full Output Path: {self.full_output_path}")
            print(f"Threshold: {self.threshold}")
            print(f"New FPS: {self.new_fps_amount}")
            print("--------------------------------------\n")

        self.make()
        if self._enable_default_logging: print("---------------- DONE ----------------")

    def make(self):
        cap = cv2.VideoCapture(self.full_input_path)
        if not cap.isOpened():
            raise IOError(f"Cannot open video: {self.full_input_path}")
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_interval = max(1, int(fps / self.new_fps_amount))  # Ensure frame_interval is at least 1

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.full_output_path, fourcc, self.new_fps_amount, (frame_width, frame_height))

        frame_count = 0
        last_frame = None

        try:
            with tqdm(total=total_frames, desc="Processing", unit="frame") as pbar:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    if last_frame is None:
                        last_frame = gray_frame
                        out.write(frame)
                    else:
                        diff = cv2.absdiff(gray_frame, last_frame)
                        non_zero_count = np.count_nonzero(diff)

                        if non_zero_count > self.threshold:  # Threshold to detect significant change
                            out.write(frame)
                            #last_frame = gray_frame
                        
                        last_frame = gray_frame

                    frame_count += 1
                    pbar.update(1)

        finally:
            cap.release()
            out.release()
            print("\n")
