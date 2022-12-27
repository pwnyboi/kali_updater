import subprocess

with open("commands.txt", "r") as fh:
    cmds = fh.readlines()
    for item in cmds:
        print(f"Executing: {item}")
        subprocess.run(item.split(" "))