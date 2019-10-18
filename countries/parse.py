#!/usr/bin/env python3

import csv

with open('all.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print('("{tag}", "{item}", False),'.format(tag=row[1], item=row[0]))
