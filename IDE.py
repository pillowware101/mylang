import basic, os
from tkinter import *
from tkinter.ttk import *
import subprocess
from threading import Thread
import tkinter.scrolledtext as scrolledtext
import queue

class CustomScrolledText(scrolledtext.ScrolledText):
    '''A text widget with a new method, highlight_pattern()
    example:
    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")
    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        scrolledtext.ScrolledText.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern
        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count =IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")

class Console(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.createWidgets()

        # get the path to the console.py file assuming it is in the same folder
        consolePath = os.path.join(os.path.dirname(__file__),"console.py")
        # open the console.py file (replace the path to python with the correct one for your system)
        # e.g. it might be "C:\\Python35\\python"
        self.p = subprocess.Popen(["python3",consolePath],
                                  stdout=subprocess.PIPE,
                                  stdin=subprocess.PIPE,
                                  stderr=subprocess.PIPE)

        # make queues for keeping stdout and stderr whilst it is transferred between threads
        self.outQueue = queue.Queue()
        self.errQueue = queue.Queue()

        # keep track of where any line that is submitted starts
        self.line_start = 0

        # make the enter key call the self.enter function
        self.ttyText.bind("<Return>",self.enter)

        # a daemon to keep track of the threads so they can stop running
        self.alive = True
        # start the functions that get stdout and stderr in separate threads
        Thread(target=self.readFromProccessOut).start()
        Thread(target=self.readFromProccessErr).start()

        # start the write loop in the main thread
        self.writeLoop()

    def destroy(self):
        "This is the function that is automatically called when the widget is destroyed."
        self.alive=False
        # write exit() to the console in order to stop it running
        self.p.stdin.write("exit()\n".encode())
        self.p.stdin.flush()
        # call the destroy methods to properly destroy widgets
        self.ttyText.destroy()
        Frame.destroy(self)
    def enter(self,e):
        "The <Return> key press handler"
        string = self.ttyText.get(1.0, END)[self.line_start:]
        self.line_start+=len(string)
        self.p.stdin.write(string.encode())
        self.p.stdin.flush()

    def readFromProccessOut(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.p.stdout.raw.read(1024).decode()
            self.outQueue.put(data)

    def readFromProccessErr(self):
        "To be executed in a separate thread to make read non-blocking"
        while self.alive:
            data = self.p.stderr.raw.read(1024).decode()
            self.errQueue.put(data)

    def writeLoop(self):
        "Used to write data from stdout and stderr to the Text widget"
        # if there is anything to write from stdout or stderr, then write it
        if not self.errQueue.empty():
            self.write(self.errQueue.get())
        if not self.outQueue.empty():
            self.write(self.outQueue.get())

        # run this method again after 10ms
        if self.alive:
            self.after(10,self.writeLoop)

    def write(self,string):
        self.ttyText.insert(END, string)
        self.ttyText.see(END)
        self.line_start+=len(string)

    def createWidgets(self):
        self.ttyText = Text(self, wrap=WORD)
        self.ttyText.pack(fill=BOTH,expand=True)

root=Tk()
editor=CustomScrolledText(root)
main_console = Console(root)
editor.pack(side=TOP, fill=BOTH, expand=True)
main_console.pack(fill=BOTH,expand=True, side='bottom')
root.mainloop()