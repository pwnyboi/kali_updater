import subprocess

with open("commands.txt", "r") as ku:
    cmds = ku.readlines()
    for item in cmds:
        print(f"Executing: {item}")
        subprocess.run(item.split(" "))
        print(f"{item} was a success!")