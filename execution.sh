#!/bin/bash
#調べるウェブページのURLを指定
url=https://yahoo.co.jp
#保存先を指定
export saveTo=/Users/itouryuunosuke/project/Screenshot/screenshot/screenshot.png

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --disable-gpu --screenshot=$saveTo --window-size=1280,1080 $url
python3 imageComparison.py