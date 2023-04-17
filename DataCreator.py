import os
import sys

# Author: Gal Koaz
# Date: 2023-04-16

if len(sys.argv) != 4:
    print('Usage: (python or py) DataCreator.py input_folder output_txt number')
    print('Example: py DataCreator.py c:\\users\\desktop\\clips text.txt 0')
    sys.exit(1)

input_directory = sys.argv[1]
output_file_name = sys.argv[2]
number = sys.argv[3]

with open(output_file_name, 'w') as f:
    for filename in os.listdir(input_directory):
        if os.path.isfile(os.path.join(input_directory, filename)):
            f.write(os.path.join(input_directory, filename) + ' ' + number + '\n')
