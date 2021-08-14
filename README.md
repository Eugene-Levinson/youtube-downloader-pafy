## Setup


### Install dependencies
```
pip install pafy
pip install youtube_dl
pip install ffmpy
```

### Get source
```
curl -LJO https://github.com/Eugene-Levinson/youtube-downloader-pafy/archive/refs/tags/v.2.0.zip
unzip youtube-downloader-pafy-v.2.0.zip
```
or
```
git clone git@github.com:Eugene-Levinson/youtube-downloader-pafy.git
```
<br>

### This script requires ffmpeg.  
On Ubuntu/Debian:
```
sudo apt-get install ffmpeg
```

On Windows:
1. Download ffmpeg from the official website https://ffmpeg.org/download.html
2. Makse sure to add it to PATH

Alternativly, download a compiled binary of ffmpeg https://ffmpeg.org/download.html#build-windows and place it in the folder with all the other files.

<br>

### Usage
1. Place the Youtube URLs into the `urls.txt` file 
2. Place the desired names for each of the downloaded videos into the `names.txt` file
- alternatively change the path to your own names and urls files

3. Run `python app.py`
