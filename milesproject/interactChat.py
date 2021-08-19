import pexpect
import sys

child = pexpect.spawn('/usr/bin/python3 /home/milesproject2021/chatbot.py')
child.logfile_read = sys.stdout
