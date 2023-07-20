import os, sys, subprocess

try:
    print("""
    Welcome to CLI-DLP, a command-line helper for YT-DLP!

    Before using this tool, make sure you have yt-dlp installed, as well as ffmpeg.
    You can do this by quitting this program and typing 'yt-dlp --version' and 'ffmpeg --version'.
    If you have these two installed, you will get version information on each. Otherwise, the command won't be recognized.

    You can quit at any time by pressing Ctrl+C.

    Remember, Ctrl+Shift+V to paste into a Linux terminal.
    ----------------------------------------------------------------------------------------------------------------------""")
    print("""
    Do you want to download one video, or multiple?
    Type '1' for one, and anything else for multiple (ignore quotation marks).
    Note: if you have the URL of a playlist, and want to download all videos in the playlist, select '1', and use the playlist URL.
    """)
    final_command = ["yt-dlp"] 

    vid_number = input(">>")
    vid_number = vid_number.replace(" ", "")

    if vid_number != "1":
        print("Input one URL and press enter. Repeat this for each URL in the list of videos you want to download. When you have entered every URL you want to download, type 'X'.")
        vid_list_count = 1

        while True:
            print("Video", str(vid_list_count) + ", press 'X' when you have entered every video you want to download.")
            video_choice = input(">>")
            video_choice = video_choice.replace(" ", "")

            if video_choice == "x" or video_choice == "X":
                print("You want to download", str(vid_list_count - 1), "videos, is this correct? (y/N)")
                vid_list_confirm = input(">>")
                vid_list_confirm = vid_list_confirm.lower()
                if vid_list_confirm == "y":
                    break
                else:
                    continue
                break

            vid_list_count += 1
                
            with open(".vid-list.txt","a") as vidlist:
                vidlist.write(str(video_choice) + "\n")
        
        final_command.append("-a")
        final_command.append(".vid-list.txt")
    
    else:
        print("What is the URL of the video?")
        vid_url = input(">>")
        final_command.append(vid_url)
        print(final_command)

    print("Now downloading...", final_command)
    downloading = subprocess.Popen(final_command, shell=False)
    if os.path.isfile(".vid-list.txt"):
        os.remove(".vid-list.txt")

except (Exception, KeyboardInterrupt):
    if os.path.isfile(".vid-list.txt"):
        os.remove(".vid-list.txt")
    print("\nExiting...\n")
