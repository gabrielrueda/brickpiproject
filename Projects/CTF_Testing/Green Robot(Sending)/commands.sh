#!/bin/bash

echo Hello World!

dos2unix connectSSH.py

dos2unix Robot.py

chmod 755 connectSSH.py

chmod 755 Robot.py

sudo python main.py

# function killcommand1() {
#     python emergencyKill.py
# }

# sleep 5s

# killcommand1

# python testSSH.py &
# python Robot.py &