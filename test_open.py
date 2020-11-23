from subprocess import *

openWhat = input('What app do you want to open ')
def main():
    call(['/usr/bin/open', '/Applications/' + openWhat + ".app"]) 
if __name__ == "__main__":
     main()
     print("Running program")