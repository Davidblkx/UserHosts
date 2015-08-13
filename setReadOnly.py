import os, stat

current = os.path.dirname(os.path.abspath(__file__))

for(dir, _, files) in os.walk(os.getcwd()):
    for f in files:
        path = os.path.join(dir, f)
        os.chmod(path, stat.S_IREAD)
        print(path)

input();
