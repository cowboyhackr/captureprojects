captureprojects
===============
bootscripts and python scripts installation notes

python scripts are deployed in user/local/bin/projects/
bootscripts are deployed in us /etc/init.d/

		1) set permissions for bootscript and python script
		2) register script with this command:  update-rc.d {nameofscript} defaults 
		3) ensure that python script and bootscript have the correct permissions. (chmod)
		3) to remove bootscript from list:  update-rc.d -f {nameofscript} remove
		
		Testing from command line is possible.  http://www.raspberrypi.org/phpBB3/viewtopic.php?t=62579&p=464520
		1) sudo sh -x /etc/init.d/Daemon start (x is optional)
		2) sudo /etc/init.d/MoonoDaemon start
		
		* followed this shell example in the end.  http://www.pietervanos.net/knowledge/start-python-script-from-init-d/
		Example:   
		

			 #! /bin/sh
			# /etc/init.d/example
			 
			case "$1" in
			  start)
			    echo "Starting example"
			    # run application you want to start
			    python /usr/local/sbin/example.py &
			    ;;
			  stop)
			    echo "Stopping example"
			    # kill application you want to stop
			    killall python
			    ;;
			  *)
			    echo "Usage: /etc/init.d/example{start|stop}"
			    exit 1
			    ;;
			esac
			 
			exit 0
		
project 1-

		1) MotionCapture - captures photos with sensor
		2) FilePoster - Posts images to server
		
project 2-

		1) Sensor to turn on PowerswitchTail for lighting.   


