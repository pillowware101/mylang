import os

path=os.getenv("HOME")
with open(f'{path}/.bashrc', "a+") as f:
    f.write("#PATH exports\n")
    f.write("export PATH=$PATH:~/basicbin")    