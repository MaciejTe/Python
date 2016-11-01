# Wi-fi performance test

### TABLE OF CONTENTS ###

1. USER REQUIREMENTS
    * Modules and programs needed
    * Assumptions
   
2. FUNCTIONALITY DESCRIPTION
    * General description
    * Options and commands
    * Examples

3. ERROR HANDLING



## 1. USER REQUIREMENTS  
    
    Script was created in order to perform Wi-fi bandwidth tests. Script can be also used for LAN hosts.




INSTRUCTIONS
1. Clear output files
2. Set SSH servers on Wi-fi hosts
3. Comment 'StrictHostKeyChecking = yes' line

###### ASSUMPTIONS ######

1. Script doesn't set interfaces to be tested - Master has to be LAN client(default eth0 interface), other hosts - Wi-fi(wlan0 interfaces)

!!!!!!!!!!!!!! 2. Master host has to have paramiko module installed:

sudo pip install paramiko
pip install paramiko
sudo apt-get install python-paramiko

!!!!!! DO OGARNIECIA !!!!!!!!!!!!!!!!!!!!


[Errno None] Unable to connect to port 22 on  or 192.168.10.9


RZECZY DO ZROBIENIA :

1. PARAMIKO INSTALL / MODULE
2. PLIK WYKONYWALNY