install relavent liberies by using the following scripts

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

