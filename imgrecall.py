import os
import sys
import time
from shutil import copy2
from threading import Timer
from datetime import datetime


def img_recall(i):
    year_month = get_time()
    image_folder = i + year_month
    print("Starting up... Looking for new files in:", image_folder)
    code = 0
    chopping_list = []
    before = dict([(f, None) for f in os.listdir(image_folder)])
    while 1:
        time.sleep(1)
        after = dict([(f, None) for f in os.listdir(image_folder)])
        added = [f for f in after if not (f in before)]
        removed = [f for f in before if not (f in after)]
        if added:
            chopping_list.extend(added)
            if code == 0:
                temp_path = os.path.join(image_folder, added[0])
                code = get_code(temp_path)
            print("Added: ", ", ".join(added))
            for file in added:
                orig = os.path.join(image_folder, file)
                copy2(orig, output_path)
                t = Timer(310.0, cleaner, [file, chopping_list])
                t.start()
        if removed:
            for file in removed:
                if file in chopping_list:
                    temp_path = os.path.join(output_path, file)
                    image_decode(temp_path, file, code)
                    print("Decoded:", file)
                    chopping_list.remove(file)
                    delete_file(temp_path)
            print("Removed: ", ", ".join(removed))
        before = after


def cleaner(file, chopping_list):
    if file in chopping_list:
        print("Timer up, deleting file:", file)
        temp_path = os.path.join(output_path, file)
        delete_file(temp_path)
        chopping_list.remove(file)


def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)
        print("Deleted:", file)
    else:  # Show an error
        print("Error: %s file not found" % file)


def get_code(f):
    file = open(f, "rb")
    for a in file:
        for byte in a:
            code = byte ^ 0xFF
            return code


def image_decode(f, fn, code):
    file = open(f, "rb")
    out = output_path + "\\" + fn + ".png"
    png = open(out, "wb")
    for a in file:
        for byte in a:
            new_byte = byte ^ code
            png.write(bytes([new_byte]))
    file.close()
    png.close()


def get_time():
    today = datetime.today()
    year_month = datetime(today.year, today.month, 1)
    return str(year_month)[:7]


if __name__ == "__main__":
    global output_path
    output_path = input("output path:")
    if not os.path.isdir(output_path):
        sys.exit("output path is an invalid directory")
    img_folder = input("wechat image folder path:")
    if not os.path.isdir(img_folder):
        sys.exit("the image folder is invalid")
    img_recall(img_folder + "\\")
