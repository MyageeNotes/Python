# -*- coding: utf-8 -*-
# Created by MyageeNotes 2019.01.31

import os,math

# SET DIRECTORY PATH
target = os.path.join("C:","Users")
dirs = os.listdir(target)
dict = {}

# CHECK DIRECTORY MODIFY TIME
for folder in dirs:
    path = os.path.join(target,folder)
    try:
        # 3T1_xx -> xx
        fname = folder.split('_')[1]

        # EPOCH time
        time = os.path.getmtime(path)
        dict[fname] = time

    except Exception as e:
        pass

rank = 1
for k, v in sorted(dict.items(), key=lambda x: -x[1]):
    print("#{0}. {1}". format(rank,str(k)))
    rank += 1
