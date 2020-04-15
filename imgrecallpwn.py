import os
import time
from shutil import copy2
from threading import Timer

output_path = "D:\\Documents\\Random\\21588\\output"


def img_recall(image_folder):
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
    dat_read = open(f, "rb")
    out = output_path + fn + ".png"
    png_write = open(out, "wb")
    for now in dat_read:
        for byte in now:
            new_byte = byte ^ code
            png_write.write(bytes([new_byte]))
    dat_read.close()
    png_write.close()


if __name__ == "__main__":
    img_folder = "D:\\Documents\\WeChat Files\\wilsongao-\\FileStorage\\Image\\2020-04"
    img_recall(img_folder)
