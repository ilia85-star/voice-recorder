from librec import *
from os import system

rec = Recorder()
name = str(input("enter the file name without sufix: ")+".wav")
with rec.open(name, 'wb') as recfile2:
    recfile2.start_recording()
    input("hit enter to exit")
    recfile2.stop_recording()

system(f"ffmpeg -i {name} ~/{name}.mp3")
system(f"rm -rf {name}")
