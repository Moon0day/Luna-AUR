import subprocess
import sys
import os

def main(): 
    target = input("[+]target: ")
    nmap = f'nmap {target}'
    subprocess.run(nmap, shell=True)

if __name__ == "__main__":
    main()
