import pafy
import os
import json
import ffmpy

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoAudiumStreamsError(Error):
    """Raised when the input value is too small"""
    pass

def log_output(msg):
    file = open("download_output.txt", "a")
    file.write(msg)
    file.close()



#urls = ["https://www.youtube.com/watch?v=AYA8DRG8cFs", "https://www.youtube.com/watch?v=q_Pmm_aRnnQ", "https://www.youtube.com/watch?v=q_Pmm_aRnnQ"]

#names = ["Test 1", "Test 2", "Test 3"]

successfully_downloaded = []
failed_downloads = []
to_convert = []


def download(url, name, save_dir, content_type, formatt):
    video_tag = name + " : " + url
    save_dir += "raw/"
    
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        video = pafy.new(url)

        if content_type == "audio":
            audio_streams = video.audiostreams

            if len(audio_streams) == 0:
                raise NoAudiumStreamsError

            content = video.getbestaudio()

        else:
            content = video.getbest()

        file_path = save_dir + name + "." + content.extension

        if os.path.isfile(file_path):
            os.remove(file_path) 


        content.download(quiet=False, filepath=file_path)
        to_convert.insert(0, file_path)
        log_output("\nSUCCESSFULLY downloaded " + video_tag)
    
    except NoAudiumStreamsError:
        print("Could not find any audio only streams")
        log_output("\nFAILD to download " + video_tag)
        log_output("\nCould not find any audio only streams")
        failed_downloads.append(video_tag)

    except:
        print("Failed")
        log_output("\nFAILD to download " + video_tag)
        failed_downloads.append(video_tag)

def convert(input_file, output_dir, filename, extension):
    try:
        print("Converting to a desired format")
        output_file = output_dir + "converted/" + filename + "." + extension
        print(output_file)

        if not os.path.exists(output_dir + "converted/"):
            os.makedirs(output_dir + "converted/")

        ff = ffmpy.FFmpeg(
            inputs={input_file: None},
            outputs={output_file: None}
        )     

        ff.run()
    except Exception as e:
        print("There was an error converting")
        print(filename)
        print(e)


def run_downloader(urls, names, config):

    open('download_output.txt', 'w').close() #clean the log file
    open('output.txt', 'w').close() #clean the log file

    mode = "video"
    if config["audio_only"]:
        mode = "audio"

    if config["save_dir"][-1] != "/":
        config["save_dir"] += "/"



    for i in range(0, len(urls)):
        print("Downloading " + names[i] + " ({}/{})".format(str((i + 1)), str(len(urls))))
        download(urls[i], names[i], config["save_dir"], mode, config["file_type"])
        convert(to_convert[0], config["save_dir"], names[i], config["file_type"])

    print("\nAll done!")

    if len(failed_downloads) == 0: 
        output = "\nAll videos downloaded successfully"
        print(output)

    else:
        score = "(" + str(len(failed_downloads)) + "/" + str(len(urls)) + ")"
        print("\nFailed to download " + score + ":")

        output = ""

        for entry in failed_downloads:
            output += entry

        print(output)


    file = open("output.txt", "w")
    file.write(output)
    file.close()


#process input data
with open("config.json", "r") as config_file:
    config_raw = config_file.read()

config = json.loads(config_raw)

with open(config["urls_filepath"], "r") as urls_raw:
    urls = urls_raw.readlines()

for i in range(len(urls)):
    urls[i] = urls[i].strip()

with open(config["names_filepath"], "r") as names_raw:
    names = names_raw.readlines()

for i in range(len(names)):
    names[i] = names[i].replace("/", "-")
    names[i] = names[i].replace("\\", "-")

for i in range(len(names)):
    names[i] = names[i].strip()

run_downloader(urls, names, config)





    







