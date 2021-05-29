from librec import *
from os import system

def main():
	rec = Recorder()
	name = str(input("enter the file name without sufix: ")+".wav")
	with rec.open(name, 'wb') as recfile:
  		recfile1.start_recording()
  		input("hit enter to exit")
  		recfile1.stop_recording()

	system(f"ffmpeg -i {name} ~/{name}.mp3")
	system(f"rm -rf {name}")
