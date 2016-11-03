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

MODULES AND PROGRAMS NEEDED / INSTRUCTIONS

1. Clear output files (output.txt, output_full.txt) - optional
2. Set SSH servers on Wi-fi hosts
-  Comment 'StrictHostKeyChecking = yes' line in configuration file
- SSH servers have to be configured in way that no ssh keys will be needed
3. Arbitrarily perform manual SSH connection test first between Master and all hosts.

ASSUMPTIONS

Recommended distros: Ubuntu / Linux Mint.

1. Script doesn't set interfaces to be tested - Master has to be LAN client(default eth0 interface), other hosts - Wi-fi(wlan0 interfaces) or LAN hosts
2. Master host has to have following python modules installed:

* paramiko
    
    
    sudo apt-get install python-paramiko

* click
    
    
    sudo apt-get install python-click
    
* threading

    
    sudo apt-get install python-click
    
* iperf


    sudo apt-get install iperf
    
3. Wi-fi (or LAN) hosts should have following modules installed

* iperf 


    sudo apt-get install iperf
    
    
* SSH server


    sudo apt-get install ssh
## 2. FUNCTIONALITY DESCRIPTION

GENERAL DESCRIPTION

    Bandwidth testing script for LAN / Wi-fi hosts. Single or multiple hosts can be tested. 
    
OPTIONS AND COMMANDS
    
    