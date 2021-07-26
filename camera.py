#from time import time
import csv



class Camera(object):
    def __init__(self):
        filenames = []
        for i in range(5003):
            filenames += ['frames_with_pose/frame_{}.jpg'.format(i)]
        self.frames = [open(frame, 'rb').read() for frame in filenames]

    def get_frame(self):
        # open the file in the write mode
        with open('time.txt', 'w', encoding='UTF8') as f:
            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow(row)

        return self.frames[int(time()) % 5003]