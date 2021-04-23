import glob

import cv2

for t in range(13, 32):
    if t != 9 and t != 10:
        target = "08{:02d}".format(t)
        img_array = []
        size = (480, 480)
        for filename in sorted(glob.glob("images_bak/{}/*.jpg".format(target))):
            img = cv2.imread(filename)
            height, width, layers = img.shape
            img = cv2.resize(img, size)
            img_array.append(img)

        name = 'images_bak/project_{}.mp4'.format(target)
        out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'), 24.0, size)

        max_img = len(img_array)
        print('\nConvert started... MAX:{}'.format(max_img))
        for i in range(len(img_array)):
            out.write(img_array[i])
            if i % 100 == 0:
                print('\rWritten {}/{}'.format(i, max_img), end='')
        out.release()
        print('\nFinished!')
