#!/usr/bin/python
import glob
import sys

def create_labels(read_dir, write_dir):
	#Reading files
	onlyfiles = glob.glob(read_dir + "*.jpeg")

	#Label file
	labels = open(write_dir + "labels.txt", "w")
	print("starting...")
	#Create the labels
	for file in onlyfiles:
		answer = file.replace('.jpeg','').split('\\')[-1]
		labels.write(file + ' ' + answer + '\n')
		print("processed: " + answer)

	labels.close()

if __name__ == "__main__":
	print("Usage: ./label_generating_script.py <directory where CAPTCHAs are stored> <directory to store label file>")
	try:
		read_dir = sys.argv[1]
		write_dir = sys.argv[2]
		create_labels(read_dir, write_dir)
	except:
		print("Please provide the directory where the labeled CAPTCHAs are stored as well as the directory to store the label file in")
