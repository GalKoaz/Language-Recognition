import sys
from os import listdir, makedirs
from os.path import isfile, join, exists
from pydub import AudioSegment

# import required modules
import subprocess

# Author: Gal Koaz
# Date: 2023-04-16
if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print("Usage: python DataConvertor.py path_folder1 path_folder2")
    #     sys.exit(1)
    #
    # input_folder = sys.argv[1]
    # output_folder = sys.argv[2]
    input_folder = r'C:\Users\idank\language_project\Language-Recognition\media\zh_HK_mp3'
    output_folder = r'C:\Users\idank\language_project\Language-Recognition\media\zh_HK_wav'

    if not exists(output_folder):
        makedirs(output_folder)

    files = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    counter = 1
    for file in files:
        if file.endswith(".mp3"):
            file_path = join(input_folder, file)
            # convert mp3 to wav file
            # subprocess.call(['ffmpeg', '-i', file_path,
            #                  'converted_to_wav_file.wav'])
            sound = AudioSegment.from_mp3(file_path)
            new_file_path = join(output_folder, file.replace(".mp3", ".wav"))
            sound.export(new_file_path, format="wav")
            print(counter)
            counter+=1
