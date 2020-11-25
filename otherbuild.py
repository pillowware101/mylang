import os, sys

if "pyinstaller" not in sys.modules:
    os.system("pip3 install pyinstaller")
    os.system("pyinstaller --onefile ~/Documents/mylang/shell.py")
    exit()

else:
    os.system("pyinstaller --onefile ~/Documents/mylang/shell.py")
    exit()