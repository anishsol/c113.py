import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the directory to monitor
directory_to_watch = "F:\ADDANISH\coding\pythonprojects\c113\lucky"

class FileChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"File {event.src_path} has been created")
        elif event.event_type == 'modified':
            print(f"File {event.src_path} has been modified")
        elif event.event_type == 'deleted':
            print(f"File {event.src_path} has been deleted")
        # Add more conditions as needed

if __name__ == "__main__":
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, directory_to_watch, recursive=True)
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
