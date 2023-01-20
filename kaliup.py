import subprocess
import time
import os

print("updating kali")
subprocess.run("sudo apt update")
print("upgrading kali")
subprocess.run("sudo apt full-upgrade")
print("auto removing old dependancies")
subprocess.run("sudo apt auto-remove")
time.sleep(1)
print("process complete!")
print("auto closing ;) ")
time.sleep(1)

quit()
