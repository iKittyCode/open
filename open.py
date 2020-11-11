
from subprocess import *
openWhat = input('What app do you want to open')
def open():
    call(['/usr/bin/open', '/Applications/' + openWhat + ".app"])
open()