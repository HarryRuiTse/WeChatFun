# -*- coding: utf-8 -*-
import itchat
import time
import datetime

def login_in():
	itchat.auto_login(enableCmdQR=True,hotReload=True)

def getUserNameByNickName(name):
	only_one = itchat.search_friends(nickName=name)
	name = only_one[0]['UserName']


def sendMessage(string,name):
	res = itchat.send(string,toUserName=name)
	return res

login_in()
name = getUserNameByNickName('ice')	
i = 0
while True:
		message = u'现在是北京时间%s' % datetime.datetime.now()
		print sendMessage(message,name)
		time.sleep(30)
		i+=1
		if i>10:
			break
