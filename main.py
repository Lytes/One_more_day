## One More Day
## Everyday Is A Gift. Random 20 Songs Everyday (No Repetitions)

## Lytes - Laitanayoola@gmail.com

import OMDconfig as cfg
import random
import os
from datetime import date
import sys

today = date.today().strftime("%b_%d_%Y")
yt_dload = 'youtube-dl --max-downloads 1 --max-filesize 15m --extract-audio --playlist-random --download-archive {}/downloaded_songs.txt --audio-format mp3 --no-part -q -ciw -o "{}/%(title)s.%(ext)s" {}'

def folder_check():
	global base_path
	global today_path
	try:
		cfg.download_directory
		if os.path.isdir(cfg.download_directory) != True:
			print("[+] Directory supplied in OMDconfig.py isn't valid. Be sure to provide absolute path.")
			sys.exit()
		base_path = str(os.path.join(str(cfg.download_directory),"OMDay"))
		today_path = str(os.path.join(base_path,today))
	except Exception:
		if "com.termux" in str(os.path.expanduser("~")):
			base_path = str(os.path.join("/storage/emulated/0","OMDay"))
			today_path = str(os.path.join(base_path,today))
		elif str(os.name) == "nt":
			print("[+] Kindly add base_path in OMGconfig.py")
			sys.exit()
		else:
			base_path = str(os.path.join(os.path.expanduser("~"),"OMDay"))
			today_path = str(os.path.join(base_path,today))
			basic_checks()
	
	
def basic_checks():
	if type(cfg.source) is not list or len(cfg.source) < 1:
		print("[+] Make sure 'source' variable in config.py is a list of youtube music channels.") 
		sys.exit()
	elif type(cfg.daily_download) is not int or cfg.daily_download < 1:
		print("[+] Make sure 'daily_download' variable in config.py is an integer greater than zero.")
		sys.exit()
	elif os.path.isdir(base_path) != True:
		print("[+] Trying to create OMDay folder in {}".format(base_path))
		try:
			os.mkdir(base_path)
			print("Created")
			random_downloads()
		except Exception:
			print("Folder creation failed")
			sys.exit()
	elif os.path.isdir(today_path):
		if len(os.listdir(today_path)) < cfg.daily_download:
			no_left = cfg.daily_download - len(os.listdir(today_path))
			print("[+] Downloading {} songs to complete the list".format(no_left))
			random_downloads(no_left)
		else:
			print("[+] You already downloaded today's {} songs. Enjoy them for the rest of the day.".format(cfg.daily_download))
			sys.exit()
	else:
		os.mkdir(today_path)
		random_downloads(cfg.daily_download)


def random_downloads(no):	
	source = cfg.source
	for i in range(1,no+1):
		link = random.choice(source)
		dload_link = yt_dload.format(base_path, today_path, link)
		os.system(dload_link)
		print("[+] Downloaded {} of {}".format(i,no))
	

if __name__ == "__main__":
	folder_check()	



