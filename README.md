captureprojects
===============
bootscripts and python scripts installation notes

python scripts are deployed in user/local/bin/projects/
bootscripts are deployed in us /etc/init.d/

1) set permissions for bootscript and python script
2) register script with this command:  update-rc.d {nameofscript} defaults 
3) to remove bootscript from list:  update-rc.d -f {nameofscript} remove
