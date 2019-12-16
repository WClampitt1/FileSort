#! /usr/bin/python3

import sys
import os
import shutil
from progress.bar import Bar


def main(argv):
    if len(argv) == 2:
        infile = os.path.abspath(argv[0])
        outfile = os.path.abspath(argv[1])

        check(infile, outfile)
        sort(infile, outfile)
    else:
        print('Please use valid syntax: FileSort.py <infile> <outfile>')


# Checks if the input and output directories exist.
# If the output directory doesn't exist, it makes the corresponding directory.
def check(infile, outfile):
    # checks if the input directory exits
    if os.path.exists(infile) and os.path.isdir(infile):
        if not (os.path.exists(outfile) and os.path.isdir(outfile)):
            os.mkdir(outfile)
            print('Output directory \'' + outfile + '\' was created.')
    else:
        print('The input directory does not exist.')


# Sorts the files from the input directory into folders in the output directory
# that correspond to the file extension of the files
def sort(infile, outfile):
    numfiles = sum([len(files) for r, d, files in os.walk(infile)])
    with Bar('Sorting Files', max=numfiles) as bar:
        for (root, dirs, files) in os.walk(infile):
            for file in files:
                full_name = os.path.join(root, file)
                file_ext = os.path.splitext(full_name)[1]
                target = os.path.join(outfile, file_ext[1:])
                if not (os.path.exists(target) and os.path.isdir(target)):
                    os.mkdir(target)
                try:
                    shutil.copy(full_name, target)
                except IOError as e:
                    print("Unable to copy file. %s" % e)
                bar.next()


if __name__ == "__main__":
    main(sys.argv[1:])
