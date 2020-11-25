#create binaries
python3 ~/Documents/mylang/otherbuild.py
mkdir ~/basicbin
rm -r build/*
rmdir build
cd dist
mv shell basic
mv basic ~/basicbin
cd ..
rmdir dist
rm shell.spec

#add basicbin to your path
export PATH=$PATH:~/basicbin
python3 ~/Documents/mylang/build.py