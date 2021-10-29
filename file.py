from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
#pip install watch for these package work 

import os
import json
import time

class Myhandler(FileSystemEventHandler):
    i=1
    def on_modified(self, event ):
        for fielname in os.listdir(folder_to_track):
            scr = folder_to_track+ "/" +fielname
            new_destination = folder_to_destination + "/" + fielname
            os.rename(scr, new_destination)

folder_to_track = 'C:/Users/user/Desktop/my folder' # give your Tracker folder full Path 
folder_to_destination = 'C:/Users/user/Desktop/newFolder' # give your Destination folder full Path
event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
