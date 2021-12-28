import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

filelist = set()

class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        filename = event.src_path.split("\\")[-1]
        print("File created: " + filename)
    def on_modified(self, event):
        filename = event.src_path.split("\\")[-1]
        global filelist
        filelist.add(filename)

folder_to_track = r"C:\Users\ASUS\Desktop\Watchdog\folder1"
folder_dest = r"C:\Users\ASUS\Desktop\Watchdog\folder2"

event_handler = EventHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
        if(len(filelist)!= 0):
            for files in filelist:
                src = folder_to_track + "\\" + files
                dest = folder_dest + "\\" + files
                os.rename(src, dest)
                print("File moved: " + files)
            filelist = set()
except KeyboardInterrupt:
    observer.stop()
    observer.join()