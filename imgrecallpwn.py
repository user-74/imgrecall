from shutil import copy2

import os, time
import decoder


def img_recall(path_to_watch):
    chopping_list = []
    output_path = "D:\\Documents\\Random\\21588\\output"
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while 1:
        time.sleep(1)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not (f in before)]
        removed = [f for f in before if not (f in after)]
        if added:
            print("Added: ", ", ".join(added))
            for file in added:
                orig = path_to_watch + "\\" + file
                copy2(orig, output_path)
                temp_path = os.path.join(output_path, file)
                decoder.imageDecode(temp_path, file)
                print("Converted", file)
                # chopping_list.add(file)
        if removed:
            for file in removed:
                if file not in chopping_list:
                    delete_file(file)
            print("Removed: ", ", ".join(removed))
        before = after


def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)
    else:  # Show an error
        print("Error: %s file not found" % file)


if __name__ == "__main__":
    img_recall("D:\\Documents\\WeChat Files\\wilsongao-\\FileStorage\\Image\\2020-04")
