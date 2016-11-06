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

1. --type
    
    Type of script operation, possible values: 
    
* Single host performance test(default value)
    
     
    python Performance_test.py --type single
    
* Multiple hosts simultaneous performance test
    
     
    python Performance_test.py --type multi
    
* Both types of tests

   
    python Performance_test.py --type both
    
2. --udp

    UDP bandwidth value used for performance test; default value = 100M
    
* Usage:

    
    python Performance_test.py --udp 100M
    python Performance_test.py --udp 3000000000
    
3. --time
    
    Test time for each thread(TCP_upload, TCP_download, UDP_upload, UDP_download); default value = 10 seconds
    
* Example & usage:

    
    python Performance_test.py --time 30
    
4. --freq

    Wi-fi frequency choice ; default value=2.4 GHz
    
* Usage:


    python Performance_test.py --freq 24
    
or

    python Performance_test.py --freq 5
    
5. Examples

    Runs script with default options values:
    
        python Performance_test.py
         
    Runs script with all options available:
        
        python Performance_test.py --type multi --freq 5 --udp 200M --time 20

## 3. Error handling

Following error codes are used when script crashes:

1. 1011 - BadAuthenticationType --> 
2. 1012 - AuthenticationException -->
3. 1013 - unknown problem with SSH connection

                         1011: ('Exception: BadAuthenticationType,\n'
                                'Class: SshConnection '
                                'Method: connect_to_host.', 2),
                         1012: ('Exception: AuthenticationException,\n'
                                'Class: SshConnection '
                                'Method: connect_to_host', 2),
                         1013: ('Exception: unknown,\n '
                                'Class: SshConnection '
                                'Method: connect_to_host.', 1),
                         1021: ('Exception: AuthenticationException,\n '
                                'Class: SshConnection '
                                'Method: connect_to_cpe.', 2),
                         1022: ('Exception: unknown,\n '
                                'Class: SshConnection '
                                'Method: connect_to_cpe', 1),
                         2011: ('Exception: RuntimeError,\n '
                                'Class: Main '
                                'Method: run_thread', 1),
                         2012: ('Exception: unknown,\n '
                                'Class: Main '
                                'Method: run_thread', 1),
                         2021: ('Exception: RuntimeError,\n '
                                'Class: Main '
                                'Method: write_description', 1),
                         2031: ('Exception: IOError,\n '
                                'Class: Main '
                                'Method: write_description', 1),
                         2032: ('Exception: unknown,\n '
                                'Class: Main '
                                'Method: write_description', 1),
                         2041: ('Exception: RuntimeError,\n '
                                'Class: Main '
                                'Method: one_host', 2),
                         2042: ('Exception: unknown,\n '
                                'Class: Main '
                                'Method: one_host', 2),
                         2051: ('Exception: RuntimeError,\n '
                                'Class: Main '
                                'Method: multiple_hosts', 2),
                         2052: ('Exception: unknown,\n '
                                'Class: Main '
                                'Method: multiple_hosts', 2),
                         3011: ('Exception: IOError,\n '
                                'Class: AnalyzeLog '
                                'Method: get_all_data', 1),
                         3012: ('Exception: unknown,\n '
                                'Class: AnalyzeLog '
                                'Method: get_all_data', 1),
                         3021: ('Exception: IOError,\n '
                                'Class: AnalyzeLog '
                                'Method: get_mean_value', 1),
                         3022: ('Exception: ValueError,\n '
                                'Class: AnalyzeLog '
                                'Method: get_mean_value', 1),
                         3023: ('Exception: ValueError,\n '
                                'Class: AnalyzeLog '
                                'Method: get_mean_value', 2),
                         4011: ('Exception: ValueError,\n '
                                'Class: Configuration '
                                'Method: validation', 2),
                         4012: ('Exception: unknown,\n '
                                'Class: Configuration '
                                'Method: validation', 2),
                         4013: ('Exception: KeyError,\n '
                                'Class: Configuration'
                                'Method: validation ', 2),
                         4021: ('Exception: LookupError,\n '
                                'Class: Configuration '
                                'Method: change_data_struct', 2),

    