# imgrecall

## Introduction

My first side project. Got the inspiration for it when an image I was viewing was recalled and disappeared.

In Wechat, when an image is recalled, Wechat will automatically delete that image from the image folder on your computer.
imgrecall watches your Wechat image folder for automatically downloaded images and creates a backup of anything new it sees.
It also keeps a list of every newly added image within the last 5 minutes. After 5 minutes, photos can no longer be recalled, so it deletes the backup.

Wechat uses XOR encryption for the images it stores, and each computer has a different 'key' that is used to encode these images.
imgrecall will automatically calculate the encryption key value for each user to decode images.
If imgrecall detects a file it has been watching has been deleted/recalled, it will decode the .dat file and replace it with a .png file.

## Features

Copies the .dat file that images are stored as in Wechat to another location.

If the image is recalled, the .dat copy is decoded to give the original image as a .png file.

If the image is not recalled for longer than 5 minutes, the .dat copy is deleted.

## Usage

1. Run imgrecall.py using python 3. A terminal window should open,
2. Enter your desired output folder path into the window
3. Enter your wechat image folder
The format should be similar to : C:\Users\\\{computer username}\Documents\WeChat Files\\\{wechat username}\FileStorage\Image
4. Any photos recalled should now appear in your output folder.

## Versions

* 1.1 - allows users to define folder paths via user input
* 1.0 - created the functional program

## Credits

Credit to MarxCBR's blog post describing wechat's dat file encoding.
https://www.cnblogs.com/marxcbr/p/10616458.html
