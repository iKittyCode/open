from subprocess import *
def open(what):
    call(['/usr/bin/open', what])
open('/Applications/zoom.us.app')