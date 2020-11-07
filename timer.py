import time
from time import sleep
import subprocess
import os 
import math

# Functions
def new_file():
    return str(int(time.time()))+'.pcap'

def launch_process(file_name):
    return subprocess.Popen(["tcpdump", "-w",file_name])

# Script
current_file = new_file()
current_process = launch_process(current_file)

print("[i] process : "+str(current_process.pid)+"and file : "+current_file+ " created")

next_file = None
next_process = None

old_file = None

start_time = time.time()
time_precision = 5
time_to_create = round(3,time_precision)
time_to_kill = round(1,time_precision)
time_to_analyse = 1
while time.time() > 0 :
    now_time = time.time() - start_time
    if math.fmod(round(now_time,time_precision),time_to_create) == 0.0:
        print("[i] create process and file")
        next_file = new_file()
        next_process = launch_process(next_file)
        print("[i] process : "+str(next_process.pid)+"and file : "+next_file+ " created")
        sleep(time_to_kill)
        print("[i] old process : "+str(current_process.pid)+" killed")

        old_file = current_file
        os.kill(current_process.pid,9)
        current_file = next_file
        current_process = next_process
        print("[i] analyse the old pcap file : "+old_file)
        # Analyse function
        sleep(time_to_analyse)
        os.remove(old_file)
        print("[i] old pcap file : "+old_file+ "analyzed and deleted")





