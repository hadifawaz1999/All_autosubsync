# All_autosubsync

Using autosubsync module to sync all videos in a given directory with all its subtitles in an other directory (like having n episodes of a given TV series)

# Usage :

Just run the All_autosubsync.py file ``` python3 All_autosubsync.py ```.

PS: This app will be available as an executable file soon using [PyInstaller](https://pypi.org/project/pyinstaller/)

# Requirements :

* Make sure the directory of the videos only contains the video you want to sync with subtitles (.mkv,.mp4).
* Make sure the directory of the subtitles only contains the subtitles you want to sync with the videos (.srt,.txt)
* This app uses the python module [autosubsync](https://github.com/oseiskar/autosubsync).
* ffmpeg installation :
``` sudo apt-get install ffmpeg ```
