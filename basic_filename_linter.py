import os
import sys
from pathlib import Path

def check_number_of_arguments():
    if len(sys.argv) != 2:
        if len(sys.argv) <= 1:
            raise Exception('Too few arguments.')
        else:
            raise Exception('Too many arguments.')

def check_for_help_flag():
    if sys.argv[1] in ['-h', '--help']:
        print('\nCommand to run: py basic_filename_linter.py {directory path}')
        print('\nFiles in the given directory will be renamed to:\n1. Be all lowercase\n2. Have spaces and hyphens replaced with underscores')
        return True
    return False

def check_if_argument_is_a_directory(path):
    if not path.is_dir():
        raise Exception('Argument is not a directory path.')

def rename_files_in_directory(directory_path):
    for path in directory_path.iterdir():
        if not path.is_file():
            continue
        current_file_name = os.path.basename(path)
        current_file_path = path.absolute()
        new_file_name = current_file_name.lower().replace(' ', '_').replace('-', '_')
        new_file_path = os.path.join(directory_path.absolute(), new_file_name)
        os.rename(current_file_path, new_file_path)

def main():
    check_number_of_arguments()
    if check_for_help_flag():
        return
    directory_path = Path(sys.argv[1])
    check_if_argument_is_a_directory(directory_path)
    rename_files_in_directory(directory_path)

if __name__ == '__main__':
    main()
