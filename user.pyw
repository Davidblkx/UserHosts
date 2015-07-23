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
    allTemp = urllib.request.urlopen("https://raw.githubusercontent.com/Davidblkx/UserHosts/master/all.hosts")
    profTemp = urllib.request.urlopen("https://raw.githubusercontent.com/Davidblkx/UserHosts/master/prof.hosts")
    backTemp = urllib.request.urlopen("https://raw.githubusercontent.com/Davidblkx/UserHosts/master/back.hosts")
    with open(hostsGeral, "w") as text_file:
        print(allTemp.read().decode(allTemp.headers.get_content_charset()), file=text_file)
    with open(hostsProf, "w") as text_file:
        print(profTemp.read().decode(profTemp.headers.get_content_charset()), file=text_file)
    with open(hostsBack, "w") as text_file:
        print(backTemp.read().decode(backTemp.headers.get_content_charset()), file=text_file)

except urllib.request.URLError as err: print(err)

if is_admin(user):
    with open(host, "w") as text_file:
        print("#empty", file=text_file)
elif is_prof(user):
    shutil.copyfile(hostsProf, host)
elif is_backoffice(user):
    shutil.copyfile(hostsBack, host)
else:
    shutil.copyfile(hostsGeral, host)
    

print("DONE")
input()
