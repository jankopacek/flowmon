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
threads = []
max_area = max_circumference = (0, None)

def parse_file(file):
    with open(file) as fp:
        for line in fp:
            try:
                with threadLock:
                    s = shapes.Shape.get_shape(*line.split())
                    q.put(s)
            except shapes.ValidationException:
                #TODO: log
                pass


def process_queue():
    global max_area
    global max_circumference
    while True:
        item = q.get()
        if not item:
            break
        area = item.calc_area()
        circumference = item.calc_circumference()
        # max values
        #TODO: more equal objects
        if circumference > max_circumference[0]:
            max_circumference = (circumference, item)
        if area > max_area[0]:
            max_area = (area, item)
        print("{id}: {shape}; area: {area}, circumference: {circumference}".format(
            id=item.shape_id, shape=item, area=area, circumference=circumference))
        q.task_done()


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
        t = threading.Thread(target=parse_file, args=(file,))
        t.start()
        threads.append(t)
        # parse_file(file)

    # processing thread
    tw = threading.Thread(target=process_queue)
    tw.start()

    # parsing files stops
    for t in threads:
        t.join()
        q.put(None) # stops processing thread

    # block until all tasks are done
    tw.join()

    print("Max values:")
    print("Area: {} (shape: {})".format(*max_area))
    print("Circumference: {} (shape: {})".format(*max_circumference))

if __name__ == '__main__':
    main()
