import os
import re

# define the folder path
folder_path = "./data/"

# iterate over all files in the folder
for filename in os.listdir(folder_path):
    # check if the file name contains #
    if "#" in filename:
        # remove the # character using regular expression
        new_filename = re.sub(r'#', '', filename)
        # construct the full file path
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        # rename the file
        os.rename(old_filepath, new_filepath)
