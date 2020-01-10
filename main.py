# !/usr/bin/python3
import argparse
import os
import sys
import glob
import threading
import shapes
import queue

threadLock = threading.Lock()
q = queue.Queue()


def parse_file(file):
    with open(file) as fp:
        for line in fp:
            try:
                s = shapes.Shape.get_shape(*line.split())
                print(s)
            except shapes.ValidationException as e:
                print(e)


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', type=dir_path, required=True)
        args = parser.parse_args()
    except NotADirectoryError as e:
        print("Not a directory: {}".format(e))
        sys.exit()

    for file in glob.glob(os.path.join(args.path, '*.txt')):
        parse_file(file)
    # s = shapes.Shape.get_shape('square', 2)
    # s3 = shapes.Shape.get_shape('square', 3)
    # s2 = shapes.Shape.get_shape('circle', 2)
    # print(s.calc_area())
    # print("{}, {}".format(s.shape_id, s2.shape_id))


if __name__ == '__main__':
    main()
