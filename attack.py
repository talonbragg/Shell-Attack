import click
import src/bruteftp
import src/brutessh

class printcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[36m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

intro_text = """

 ,---.  ,--.            ,--.,--.      ,---.    ,--.    ,--.                ,--.
'   .-' |  ,---.  ,---. |  ||  |     /  O  \ ,-'  '-.,-'  '-. ,--,--. ,---.|  |,-.
`.  `-. |  .-.  || .-. :|  ||  |    |  .-.  |'-.  .-''-.  .-'' ,-.  || .--'|     /
.-'    ||  | |  |\   --.|  ||  |    |  | |  |  |  |    |  |  \ '-'  |\ `--.|  \  \
`-----' `--' `--' `----'`--'`--'    `--' `--'  `--'    `--'   `--`--' `---'`--'`--'

"""

credits_text = "© Talon Bragg 2018 under the MIT License"

print (printcolors.OKGREEN + intro_text + printcolors.ENDC)
print("\n" + printcolors.OKBLUE + credits_text + printcolors.ENDC + "\n")
