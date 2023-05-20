# Script Documentation

The script is designed to search for subtitle files in a specified folder and its subfolders. It copies the subtitle file with the desired language to the parent folder and renames it based on the corresponding video file.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Requirements](#requirements)
- [Installation](#installation)
- [Script Execution](#script-execution)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The script simplifies the process of copying subtitle files from "Subs" subfolder to its specified parent folder for TV Series download from RARBG. It automatically looks for video files in the folder and its subfolders and matches them with the desired language subtitles. The script then copies the subtitle files to the parent folder, renaming them to match the corresponding video file.

> **Note:** This script is intended to facilitate the management of legitimate and legally acquired subtitle files for personal use. It is not intended or endorsed for use in any form of piracy or unauthorized distribution of copyrighted content. Please ensure that you comply with all applicable laws and respect the intellectual property rights of content creators.

## Usage

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `script.py` file is located.
4. Execute the script using the following command:

   ```
   python script.py <path_to_folder>
   ```

   Replace `<path_to_folder>` with the actual path to the folder containing the videos and subtitles.

## Requirements

- Python 3.x

## Installation

1. Ensure you have Python installed on your system. If not, you can download it from the [Python website](https://www.python.org/downloads/).

2. Download the `script.py` file to your local machine.

3. Open a terminal or command prompt.

4. Navigate to the directory where the `script.py` file is located.

5. The script has no additional dependencies, so no installation of external libraries is required.

## Script Execution

To execute the `script.py` script, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the `script.py` file is located.

3. Execute the script using the following command:

   ```
   python script.py <path_to_folder>
   ```

   Replace `<path_to_folder>` with the actual path to the folder containing the videos and subtitles.

4. The script will search for video files with the supported extensions (`".mkv"`, `".mp4"`, `".avi"`, `".mov"`) in the specified folder and its subfolders.

5. For each video file found, the script will search for the corresponding subtitle file in the "Subs" folder within the video's folder. It will check if the subtitle file has the desired language specified (currently set as "English").

6. If a matching subtitle file is found, the script will copy it to the parent folder and rename it to match the video file's name.

7. The script will display a message for each successful copy operation.

## Contributing

Contributions are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please follow these steps:

1. Fork the repository.

2. Create a new branch for your contribution.

3. Make the necessary changes and commit them.

4. Push your changes to

 your forked repository.

5. Submit a pull request to the original repository, describing the changes you have made.

## License

The script is licensed under the [MIT License](LICENSE). You are free to modify, distribute, and use the script in both personal and commercial projects. However, please ensure that you comply with all applicable laws and use the script responsibly and ethically.
