### 7-Write a program to inventory the linux system.

import os
print("\nSystem Inventory in process ....\n")
os.system("sleep 2 && clear")

print("The OS version of your server is:")
os.system("cat /etc/os*")
print("-------------------------\n")

print("The cpu information of your server is:")
os.system("lscpu")
print("-------------------------\n")

print("The memory size of your server is:")
os.system("free -m")
print("-------------------------\n")

print("The Hard Drive Capacity of your server is:")
os.system("lsblk")
print("-------------------------\n")

print("The Kernel information of your server is:")
os.system("uname -r")
print("-------------------------\n")

print(" -------------- End of System Inventory -------------- ")

