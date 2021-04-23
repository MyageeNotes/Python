import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import glob
import cv2


def conv_video(target):
    img_array = []
    for filename in sorted(glob.glob("images_caption/{}/*.jpg".format(target))):
        im = cv2.imread(filename)
        img_array.append(im)

    name = 'images_video/{}.mp4'.format(target)
    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'MP4V'), 24.0, (480, 480))

    max_img = len(img_array)
    print('\nConvert started... MAX:{}'.format(max_img))
    for i in range(len(img_array)):
        out.write(img_array[i])
        if i % 100 == 0:
            print('\rWritten {}/{}'.format(i, max_img), end='')
    out.release()
    print('\nFinished!')


def add_text_to_image(img, text, font_path, font_size, font_color, pos_y, pos_x, max_length=740):
    position = (pos_x, pos_y)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    if draw.textsize(text)[0] > max_length:
        while draw.textsize(text + '…', font=font)[0] > max_length:
            text = text[:-1]
        text = text + '…'

    draw.text(position, text, font_color, font=font)

    return img


dirs = os.listdir('images_bak')
dir_max = len(dirs)
print(dir_max)
dir_now = 0
for dir in dirs:
    dir_now += 1
    print('# DIR{}: ({}) {}'.format(dir_now, dir, '-' * 10))
    if int(dir[:2]) >= 8 and int(dir[2:]) >= 15:
        if not os.path.isdir('images_caption/' + dir):
            os.makedirs('images_caption/' + dir)
        images = os.listdir('images_bak/' + dir)
        img_max = len(images)
        print(img_max)
        img_now = 1
        for path in images:
            print('\r{}% {}'.format(img_now / img_max, path), end='')
            text = '{}-{}-{} {}:{}'.format(path[:4], path[4:6], path[6:8], path[9:11], path[11:13])
            image = Image.open(os.path.join('images_bak', dir, path)).copy()
            img = add_text_to_image(image, text, r'C:\Windows\Fonts\Ubuntu-R.ttf', 60, (255, 255, 255), 1500, 1100)
            img = img.resize((480, 480))
            img.save(os.path.join('images_caption', dir, path))
            img_now += 1
        conv_video(os.path.join(dir))