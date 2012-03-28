#! usr/bin/env/ python

import pickle


story = []

def extract(storyboardfile):
	global story
	try:
		var = pickle.load(storyboardfile)
		if var[0] == 'action':
			if var[1][0] == 1:
				chattext = var[1][1][0]
				chat = ['chat',chattext]
				story.append(chat)
			if var[1][0] == 9:
				text = var[1][1][0]
				text = ['instructions':,text]
				story.append(text)
			if var[1][0] == 7:
				text = var[1][1][0]
				text = ['introduction',text]
				story.append(text)
	except EOFError:
		break

def writetofile(ofile):
	global story
	for i in len(story):
		ofile.write(story[i][0]);		
		#if story[i][0] == 'chat';

storyboardfile = open('storyboard.pkl','rb')
ofile = open('storyboard.txt','wb')

extract(storyboardfile)
writetofile(ofile)

			
		
