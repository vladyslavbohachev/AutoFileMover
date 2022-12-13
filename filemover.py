import os
import shutil
import time
from threading import Thread

# Set the directory you want with the files in
directory = r'C:/source/test'
# Set the directory you want to move the files in
pathtomove = r'C:/source/edit'


def run_service():
    while True:
        # Do something here
        # run over the directory and search for items that match the criteria
        # in this case we search for a pdf file that start with an _
        for filename in [filename for filename in os.listdir(directory) if filename.startswith('_') and filename.endswith('.pdf')]:
            # every file that met the requirements will be moved to another directory.
            shutil.move(os.path.join(directory, filename), os.path.join(pathtomove, filename))
        # Sleep for 10 seconds
        time.sleep(10)
        print('MOVED')
        # Get a list of all files in the directory
        files = os.listdir(directory)
        # Print the number of files in the directory
        print(len(files))


def start_srvice():
    # Create a new thread
    thread = Thread(target=run_service)
    # Start the thread
    thread.start()


if __name__ == '__main__':
    start_srvice()
