#!/usr/bin/env python
#importing packages

import subprocess

#program_info 
print("Version 1.0.0")
print("Made by hemcker_mufid")

#Taking input from user
interface = raw_input("interface > ")
new_Mac = raw_input("new Mac > ")

print(" [+] Changing Mac address for " + interface + " to " + new_Mac) 


#main program
subprocess.call("ifconfig " + interface + " down ", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_Mac , shell=True)
subprocess.call("ifconfig " + interface + " up ", shell=True)