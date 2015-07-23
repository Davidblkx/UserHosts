import getpass
import urllib.request
import os
import shutil

user = getpass.getuser()

admins = ["admin", "Admin", "Administrator"]
backOffice = [ "Back Office", "backoffice" ]
prof = [ "Prof", "prof" ]

hostsGeral = r"all.hosts"
hostsProf = r"prof.hosts"
hostsBack = r"back.hosts"
host = r"C:\WINDOWS\system32\drivers\etc\hosts"

path = "http://pastebin.com/raw.php?i=x9j1jCiq"

def is_admin(str):
    for x in admins:
        if x == str:
            return True
    return False

def is_backoffice(str):
    for x in backOffice:
        if x == str:
            return True
    return False

def is_prof(str):
    for x in prof:
        if x == str:
            return True
    return False

if not os.path.exists(hostsGeral): open(hostsGeral, 'w').close()
if not os.path.exists(hostsProf): open(hostsProf, 'w').close()
if not os.path.exists(hostsBack): open(hostsBack, 'w').close() 

print("Running script for user: " + user)

try:
    txt = urllib.request.urlopen("http://pastebin.com/raw.php?i=x9j1jCiq")
    with open(hostsGeral, "w") as text_file:
        print(txt.read().decode(txt.headers.get_content_charset()), file=text_file)

except urllib.request.URLError as err: print(err)

if not is_admin(user):
    shutil.copyfile(hostsGeral, host)
else:
    with open(host, "w") as text_file:
        print("#empty", file=text_file)
    

print("DONE")
input()
