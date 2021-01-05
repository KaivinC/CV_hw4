# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 19:55
# @Author  : LeeHW
# @File    : Prepare_data.py
# @Software: PyCharm
from glob import glob
from flags import *
import os
from scipy import misc
import numpy as np
import datetime
import imageio
from multiprocessing.dummy import Pool as ThreadPool

starttime = datetime.datetime.now()
save_dir = "/home/kschen/CV_hw4/SRFBN_CVPR19/data/dataset/spec_val"
train_HR_dir = "/home/kschen/CV_hw4/SRFBN_CVPR19/data/dataset/spec_val_hr_images"
save_HR_path = os.path.join(save_dir, 'HR_x3')
save_LR_path = os.path.join(save_dir, 'LR_x3')
os.mkdir(save_HR_path)
os.mkdir(save_LR_path)
file_list = sorted(glob(os.path.join(train_HR_dir, '*.png')))


def save_HR_LR(img, path):
	HR_img = modcrop(img, 3)
	x3_img = misc.imresize(HR_img, 1 / 3, interp='nearest')

	img_path = path.split('/')[-1].split('.')[0] + '.png'
	x3_img_path = path.split('/')[-1].split('.')[0] + '.png'

	misc.imsave(save_HR_path + '/' + img_path, HR_img)
	misc.imsave(save_LR_path + '/' + x3_img_path, x3_img)


def modcrop(image, scale=3):
	if len(image.shape) == 3:
		h, w, _ = image.shape
		h = h - np.mod(h, scale)
		w = w - np.mod(w, scale)
		image = image[0:h, 0:w, :]
	else:
		h, w = image.shape
		h = h - np.mod(h, scale)
		w = w - np.mod(w, scale)
		image = image[0:h, 0:w]
	return image


def main(path):
	print('Processing-----{}/0800'.format(path.split('/')[-1].split('.')[0]))
	img = imageio.imread(path)

	save_HR_LR(img, path)

items = file_list
pool = ThreadPool()
pool.map(main, items)
pool.close()
pool.join()
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)
