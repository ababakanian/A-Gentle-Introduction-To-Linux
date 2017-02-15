#!/usr/bin/python

import os
import sys
import Image
import glob
import random
import string

def create_thumb():

    # get current working dir
    t_pwd = os.getcwd()

	# image size
    size = 250, 250

    for infile in os.listdir(t_pwd):

		# if this is a thumb file, move to the next item
		if infile.find("thumb_") != -1:
			continue

		if infile.find(".py") != -1:
			continue

		# create infile path
		outfile_path = "thumb_" + infile

		try:
			im = Image.open(infile)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(outfile_path, "JPEG")
		except IOError:
			print "cannot create thumbnail for", infile


def rename_files():

    # get current working dir
    t_pwd = os.getcwd()

    counter = 1

    # traverse all the images
    for image in os.listdir(t_pwd):

		if image.find(".py") != -1:
			continue

		new_name = "{0}.jpg".format(counter)
		os.rename(image, new_name)
		counter += 1


if __name__ == '__main__':
    rename_files()
    create_thumb()


