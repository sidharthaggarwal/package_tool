import os
import subprocess
import pathlib as p


#uninstall packages
with open('packages/uninstall.txt') as unpkg_file:
    unpkg_array = unpkg_file.readlines()

 # Strips the newline character
count = 0
for rm_pkg in unpkg_array:
    count += 1
   # print(in_pkg.strip())
    if 1!= os.system("dpkg -l | grep " + rm_pkg):
        os.system("sudo apt-get remove -y " + rm_pkg) # Remove package
        os.system("sudo apt-get autoremove -y ") # Remove packages installed by other packages that aren't needed
        result = subprocess.check_output("dpkg --list |grep '^rc' |awk '{print $2}'", shell=True)
        os.system("sudo apt-get purge -y " + result.decode("utf-8")) # Remove package config files
        os.system("sudo apt-get -y clean") # Removes .deb files no longer installed.


# Install packages
with open('packages/install.txt') as inpkg_file:
    package_array = inpkg_file.readlines()
     
 # Strips the newline character
count = 0
for in_pkg in package_array:
    count += 1
    in_pkg = in_pkg.strip()
    if 0!= os.system("dpkg -l | grep " + in_pkg):
      os.system("sudo apt-get install -y " + in_pkg)
      # Secure our installation by removing insecure defaults
#      if in_pkg == "mysql-server" :
#        os.system('sudo mysql_secure_installation')

#use Metadata
if True == p.Path("/var/www/html/index.html"):
    os.system("sudo rm /var/www/html/index.html")
    os.system("touch /var/www/html/index.php")  
# check file exist and not empty
    path = p.Path("metadata.txt")
    if path.exists() and path.stat().st_size > 0: 
     d = {}
     with open(path) as f:
      for line in f:
       (key, val) = line.split("=")
       d[key]= val.strip()
     os.system("sudo chmod " + d['permissions'] + " " + d['file'])
     os.system("sudo chown " + d['owner'] + " " + d['file'])
     os.system("sudo chgrp " + d['group'] + " " + d['file'])
     os.system("sudo echo '" + d.get('content') + "' " + ">" + " " + d['file'])
     os.system("sudo needrestart")
print("Application setup is complete")

