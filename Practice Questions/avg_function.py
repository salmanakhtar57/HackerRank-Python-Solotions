"""
Python script to calculate the average of numbers provided as command-line arguments and write the result to a specified output file.
"""

import os
import sys

def average(*args):
    return sum(args) / len(args)

if __name__ == '__main__':
    if 'OUTPUT_PATH' not in os.environ:
        sys.exit("OUTPUT_PATH environment variable not set.")

    output_path = os.environ['OUTPUT_PATH']

    nums = list(map(int, sys.argv[1:]))
    res = average(*nums)

    with open(output_path, 'w') as fptr:
        fptr.write('%.2f\n' % res)