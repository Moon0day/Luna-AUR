import os
import sys
import subprocess

def main():
    target = input("[+]target: ")
    sql = f'sqlmap -u "{target}" --batch --dbs --forms'
    subprocess.run(sql, shell=True)

if __name__ == "__main__":
    main()
