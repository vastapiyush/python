import subprocess

proc1 = subprocess.Popen(['python3', 'main.py'])
proc2 = subprocess.Popen(['python3', 'game.py'])

proc1.wait()
proc2.wait()