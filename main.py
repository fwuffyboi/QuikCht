import rsa
import socket
import platform
import os, time



# get OS so i can clear the terminal correctly
print("Getting OS..")
print(platform.system())
os_platform = platform.system()

if platform.system() == "linux" or "darwin":  # linux, darwin == macos
    clear_cmd = "clear"
    print("clear_cmd = 'clear'.")
elif platform.system() == "Windows":
    clear_cmd = "cls"
    print("clear_cmd = 'cls'.")
else:
    print("clear_cmd unknown, using 'clear'.")
    print("clear_cmd = 'clear'.")
    


# making the public and private keys.
( myPublicKey, myPrivateKey ) = rsa.newkeys(2048, poolsize=8)



print("Done. Made PP Keys.")
