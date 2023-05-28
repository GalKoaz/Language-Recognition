# This is a sample Python script.
import os
import random
import shutil
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def delete_files(directory_path, num_files):
    # get a list of all files in the directory
    files = os.listdir(directory_path)
    # if there are fewer files than the desired number, return without deleting anything
    if len(files) <= num_files:
        return
    # determine how many files to delete
    num_files_to_delete = len(files) - num_files
    # randomly choose files to delete
    files_to_delete = random.sample(files, num_files_to_delete)
    # delete the chosen files
    for file in files_to_delete:
        file_path = os.path.join(directory_path, file)
        os.remove(file_path)



def split_files(directory_path, validation_ratio, test_ratio):
    # create subfolders for train, validate, and test
    os.makedirs(os.path.join(directory_path, 'train'), exist_ok=True)
    os.makedirs(os.path.join(directory_path, 'validate'), exist_ok=True)
    os.makedirs(os.path.join(directory_path, 'test'), exist_ok=True)

    # get a list of all mp3 files in the directory
    mp3_files = [f for f in os.listdir(directory_path) if f.endswith('.mp3')]
    # shuffle the list of files
    random.shuffle(mp3_files)

    # calculate the number of files for validation and test
    num_files = len(mp3_files)
    num_validation = int(num_files * validation_ratio)
    num_test = int(num_files * test_ratio)

    # move validation files to the validate subfolder
    validation_files = mp3_files[:num_validation]
    for file in validation_files:
        src_path = os.path.join(directory_path, file)
        dest_path = os.path.join(directory_path, 'validate', file)
        shutil.move(src_path, dest_path)

    # move test files to the test subfolder
    test_files = mp3_files[num_validation:num_validation + num_test]
    for file in test_files:
        src_path = os.path.join(directory_path, file)
        dest_path = os.path.join(directory_path, 'test', file)
        shutil.move(src_path, dest_path)

    # move remaining files to the train subfolder
    train_files = mp3_files[num_validation + num_test:]
    for file in train_files:
        src_path = os.path.join(directory_path, file)
        dest_path = os.path.join(directory_path, 'train', file)
        shutil.move(src_path, dest_path)


def split_files_in_subfolders(directory_path, validation_ratio, test_ratio):
    # get a list of subdirectories in the specified directory
    subdirectories = [f.path for f in os.scandir(directory_path) if f.is_dir()]

    # loop through the subdirectories and split the files in each one
    for subdir in subdirectories:
        split_files(subdir, validation_ratio, test_ratio)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # delete_files(r'C:\Users\gabi\Desktop\asian\cv-corpus-12.0-delta-2022-12-07\zh-CN\clips',994)
    split_files_in_subfolders(r'C:\Users\gabi\Desktop\same_size_lang', 0.2, 0.1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
