# coding: utf-8

import os
import json


if __name__ == '__main__':
    files = os.listdir('data')

    for file in files:
        with open(os.path.join('data', files[0]), encoding='utf-8') as f:
            data = f.readlines()
        dict = {}

        for line in data:
            ln = line.rstrip().split('\t')
            dict[ln[0]] = ln[1]

        dict['譜面'] = dict['譜面'].split('/')
        for i in range(len(dict['譜面'])):
            dict['譜面'][i] = dict['譜面'][i].split(',')

        print()
        for key in dict.keys():
            print('{}: {}'.format(key, dict[key]))
    
        with open(os.path.join('json', files[0].split('.')[0] + '.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(dict, ensure_ascii=False, indent=4))
