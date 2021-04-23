# coding: utf-8
import time
import datetime
import picamera
from fractions import Fraction


class Camera:
    def __init__(self):
        self.count = 0
        self.dt_now = 99
        self.hour = 99
        self.min = 99
        self.sec = 99
        self.last_shot_min = 99
        self.filename = ""
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1600, 1600)
        self.camera.rotation = 180
        self.camera.iso = 80
        self.camera.framerate = 24
        self.camera.shutter_speed = 400

    def get_time(self):
        self.dt_now = datetime.datetime.now()
        self.hour = self.dt_now.hour
        self.min = self.dt_now.minute
        self.sec = self.dt_now.second

    def set_file_name(self):
        d, t = str(self.dt_now).split(' ')
        d = "".join(d.split('-'))
        t = "".join(t.split('.')[0].split(':')[:2])
        self.filename = "./{}_{}.jpg".format(d, t)

    def set_shot_speed(self, speed):
        if speed < 5 ** 6:
            self.camera.framerate = 24
        else:
            self.camera.framerate = Fraction(1, 6)
        self.camera.shutter_speed = speed

    def capture(self):
        list_ex = ['off', 'auto', 'night', 'backlight']
        list_awb = ['off', 'auto', 'sunlight', 'cloudy', 'shade']
        for ex in list_ex:
            for awb in list_awb:
                self.camera.exposure_mode = ex
                self.camera.awb_mode = awb

                self.filename = str(self.dt_now) + '_' + ex + '_' + awb + '.jpg'
                stt = time.time()
                self.count += 1
                # print('#{:04d} capture_started {}'.format(cam.count, str(self.dt_now)))
                print('capture_started {}'.format(self.filename))
                self.camera.capture(self.filename)
                edt = time.time() - stt
                print('Captured', edt)
                self.last_shot_min = self.min
        return edt


if __name__ == '__main__':
    cam = Camera()
    cam.get_time()
    if cam.sec < 5 and cam.min == cam.last_shot_min:
        time.sleep(30)

    while 5 < cam.sec:
        cam.get_time()
        time.sleep(0.5)
    cam.set_file_name()

    if 55 < cam.min or cam.count == 0:
        # Night
        if 17 < cam.hour:
            cam.set_shot_speed(6 * 1000000)
            print("Night mode")
        # Afternoon II
        elif 16 < cam.hour:
            cam.set_shot_speed(3200)
            print("PM2 mode")
        # Afternoon I
        elif 15 < cam.hour:
            cam.set_shot_speed(800)
            print("PM1 mode")
        # Morning
        elif 4 < cam.hour:
            cam.set_shot_speed(400)
            print("morning mode")

    # SUNRISE
    if cam.hour == 4:
        oclock = 6000000
        # cam.set_shot_speed(oclock - cam.min * 99990)
        cam.set_shot_speed(1666 * ((cam.min - 60) ** 2) + 400)
        print("sunrise mode")
    # SUNSET
    if cam.hour == 19:
        # cam.set_shot_speed(oclock - cam.min * 99990)
        cam.set_shot_speed(1666 * ((cam.min - 60) ** 2) + 400)
        print("sunset mode")

    print(cam.camera.shutter_speed)
    spend_time = cam.capture()
    time.sleep(1)
