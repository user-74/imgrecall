# imgrecall

## Introduction

My first side project. 
In Wechat, when an image is recalled, Wechat will automatically delete that image from the image folder on your computer.
imgrecall watches your Wechat image folder for automatically downloaded images and creates a backup of anything new it sees.
It also keeps a list of every newly added image within the last 5 minutes. After 5 minutes, photos can no longer be recalled, so it deletes the backup.

Wechat uses XOR encryption for the images it stores, and each computer has a different 'key' that is used to encode these images.
imgrecall will automatically calculate the 'key' value for each user to use to decode images.
If imgrecall detects a file it has been watching has been deleted/recalled, it will decode the .dat file and replace it with a .png file.

## Features

Copies the .dat file that images are stored as in Wechat to another location.

If the image is recalled, the .dat copy is decoded to give the original image as a .png file.

If the image is not recalled for longer than 5 minutes, the .dat copy is deleted.

## Usage

1. Change 'output_path' in imgrecall.py to the folder you want to store your images
2. Change 'img_folder' to wherever your wechat image folder is, 
    - e.g.
"C:\\Users\\(your username)\\Documents\\WeChat Files\\(your wechat username)\\FileStorage\\Image\\" 
Be sure to include the trailing slash
3. Run wechat and run imgrecall.py.


## Credits

Credit to MarxCBR for the image decoding code, which I adapted for this program.
https://www.cnblogs.com/marxcbr/p/10616458.html