install relavent liberies by using the following scripts


do not install or use vnc server as it constantly runs in the background it uses up presious resources


enable rpi 3.5inch display by using these 

        sudo rm -rf LCD-show
        git clone https://github.com/goodtft/LCD-show.git
        chmod -R 755 LCD-show
        cd LCD-show/
        sudo ./LCD35-show  


for pn532 uart 

       sudo apt-get update
       sudo apt-get install python3 python3-pip
       sudo pip3 install nfcpy


for  ina219 

        sudo pip3 install pi-ina219

need to underclock raspberry pi and remove some unanted features on boot to fastup the boot and reduce temperatures
following parameters need to be set in the /boot/config.txt file 

to access it use this comand

         sudo nano /boot/config.txt

then change and add these following parameters

        dtparam=audio=off  #change
        camera_auto_detect=0   #change

        enable_uart=1           #add if not there
        arm_freq=600            #add
        core_freq=250           #add
        dtoverlay=disable-bt    #add

