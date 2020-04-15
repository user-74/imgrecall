# -*- coding: utf-8 -*-
# @Time    : 3/27/2019 21:54
# @Author  : MARX·CBR
# @File    : 微信Dat文件转图片.py

import os

import os

out_path = r"D:\\Documents\\Random\\21588\\output\\"


def imageDecode(f, fn, code):
    dat_read = open(f, "rb")
    # out='P:\\'+fn+".png"
    out = out_path + fn + ".png"
    png_write = open(out, "wb")
    for now in dat_read:
        for nowByte in now:
            newByte = nowByte ^ code
            png_write.write(bytes([newByte]))
    dat_read.close()
    png_write.close()


# def findFile(f):
#     fsinfo = os.listdir(f)
#     for fn in fsinfo:
#         temp_path = os.path.join(f, fn)
#         if not os.path.isdir(temp_path):
#             print('File Path: {}'.format(temp_path))
#             print(fn)
#             imageDecode(temp_path, fn)
#         else:
#             ...

# path = r'D:\\Documents\\WeChat Files\\wilsongao-\\FileStorage\\Image\\2020-04'
# findFile(path)
