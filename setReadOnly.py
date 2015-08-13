import os, stat, time

fi = "log.txt"
log = open(fi, "w")

log.write("\nStarting: " + time.strftime("%d/%m/%Y - %H:%M:%S"))

for(dir, _, files) in os.walk(os.getcwd()):
    for f in files:
        path = os.path.join(dir, f)
        if f == fi or f == "setReadOnly.py":
            continue
        os.chmod(path, stat.S_IREAD)
        log.write("\n"+path)
        print(path)

log.write("\nEnd: " + time.strftime("%d/%m/%Y - %H:%M:%S"))
log.close();
input();
