import os
import shutil
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]

    if not os.path.isdir(folder_path):
        print("Invalid folder path")
        sys.exit(1)

    subs_folder = os.path.join(folder_path, "Subs")
    desired_language = "English"
    video_extensions = (".mkv", ".mp4", ".avi", ".mov")

    for video_file in os.listdir(folder_path):
        if video_file.endswith(video_extensions):
            video_name, _ = os.path.splitext(video_file)
            video_folder = os.path.join(subs_folder, video_name)

            if os.path.isdir(video_folder):
                for srt_file in os.listdir(video_folder):
                    if srt_file.endswith(".srt") and desired_language in srt_file:
                        src_path = os.path.join(video_folder, srt_file)
                        dest_path = os.path.join(folder_path, f"{video_name}.srt")
                        shutil.copy(src_path, dest_path)
                        print(f"Copied {src_path} to {dest_path}")
                        break

if __name__ == "__main__":
    main()