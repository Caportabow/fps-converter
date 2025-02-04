# 🎥 FPS Converter for Anime Clips

## 🌟 Overview
This is a simple yet effective Python tool designed to adjust the framerate of anime clips to a static FPS value. If you're an editor who works with anime, you might be familiar with the challenge of dealing with variable framerates. This tool eliminates the hassle by converting any video to a fixed FPS, making it easier to process in Flowframes or other interpolation software.

## ⚡ Why Use This Tool?
When editing anime clips, you often need to interpolate frames to achieve smooth motion. However, anime episodes do not have a uniform framerate, which complicates the process. Instead of manually deciding where the movement is significant enough to justify a framerate change, this tool standardizes the FPS for the entire video, streamlining your workflow.

## 🚀 Features
- 🎞️ Converts variable framerate videos into a static FPS.
- ⏳ Saves time when preparing clips for interpolation.
- 🐍 Simple and lightweight Python script, that can also be used as a module.

## 🎬 Usage

To use the `fps_converter.py` script from the command line, follow these steps:

1. **Install app**: If you haven’t already, make sure you have installed the app and located at the same folder

2. **Run the script**: You can use the command line to run the script with the required arguments:
   ```bash
   fps_converter --input input_video --fps 60
   ```
      
   ### Arguments:
   - `--input` (required): Name of the input video file (excluding the file extension, e.g., `.mp4`).
   - `--fps`: Desired frames per second (FPS) for the output video. If not provided, the default FPS will be 60.
   - `--output` (optional): Name to save the output video file excluding the file extension. If not provided, the default name `{input_video_name}_out` will be used.
   - `--threshold` (optional): A value to set a threshold for detecting significant changes in frames. You can skip this argument if you don't need it.
   - `--disable_logging` (optional): Use this flag to disable logging/interface output. It will be enabled by default unless you specify this flag.

## 🔧 Usage as a Module

You can use the `fps_converter.py` as a Python module in your own script by importing the `FPS_Converter` class and calling its methods directly. This can be useful if you'd like to integrate the functionality into a larger project.

1. **Install dependencies**: If you haven’t already, make sure you have installed the necessary dependencies. You can install them via `pip`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Add it to your project**:
    ```python
    from fps_converter import FPS_Converter

    # Convert the video
    FPS_Converter(
        video_name ='input_video', # Input video name without extension.
        video_path = None, # Optional, by default preserves input video is in same directory as the script.
        output_name = 'output_video', # Output video name without extension. Optional, leave blank for {input_video_name}_out.
        output_path = None, # Optional, by default preserves output video is in same directory as the script.
        new_fps_amount = None, # Optional, by default converts video fps to 60.
        threshold = None,  # Optional, set as None if you don't need a threshold.
        enable_default_logging = True # Optional, set to False if you want to disable logging.
    )
    ```

    In this example:
    - `video_name` is the name of your input video file without extension.
    - `video_path` is the path to your input video file (default is `None`).
    - `output_name` is the name of the desired output video file without extension. If not used, set to `{input_video_name}_out`.
    - `output_path` is the path to the desired output video file (default is `None`).
    - `new_fps_amount` is the target FPS you'd like to set for the output video. If not used, set to `60`.
    - `threshold` is a number for detecting significant changes. If not used, set to `500`.
    - `enable_default_logging` controls whether or not logging is enabled (default is `True`).

## 🤝 Contributions
Feel free to contribute by submitting pull requests or opening issues if you encounter any bugs or have suggestions for improvements.

## 📜 License
This project is open-source and available under the MIT License.
