#imports
import dialogs
import time

#variables
player_location_save = ''
player_race = ''
player_class = ''
location = 'spawn'
save_password = ''
save_username = ''
correct_pass = 0
tutorial_needed = 1
save_game_yn = ''
save_game_yn_correct_response = 0
action = ''
travel_locations = ['the toot orial']
traveling_to = ''
valid_answer = 0

#game_code
while save_game_yn_correct_response == 0 :
 save_game_yn = input('do you have a saved game? y/n\n')
 if save_game_yn =='y' :
 	 username_input = input('enter username\n')
 	 file1 = open('aery_saved_password_'+username_input+'.txt','r')
 	 save_password = file1.read()
 	 file1.close()
 	 file1 = open('aery_saved_race_'+username_input+'.txt','r')
 	 player_race = file1.read()
 	 file1.close()
 	 file1 = open('aery_saved_class_'+username_input+'.txt','r')
 	 player_class = file1.read()
 	 file1.close()
 	 save_username = username_input
 	 save_game_yn_correct_response = 1
 	 while correct_pass == 0 :
 	  if input('enter password\n') == save_password :
 	 	  correct_pass = 1
 	 	  tutorial_needed = 0
 	 	  time.sleep(0.3)
 	 	  print('.')
 	 	  time.sleep(0.3)
 	 	  print('.')
 	 	  time.sleep(0.3)
 	 	  print('.')
 	 	  time.sleep(0.3)
 	 	  print("you're in!")
 	  else :
 	  	time.sleep(0.3)
 	  	print('.')
 	  	time.sleep(0.3)
 	  	print('.')
 	  	time.sleep(0.3)
 	  	print('.')
 	  	time.sleep(0.3)
 	  	print('incorrect password')
 elif save_game_yn == 'n' :
 	 save_game_yn_correct_response = 1
 	 time.sleep(0.5)
 	 save_username = input('enter a username\n')
 	 time.sleep(0.5)
 	 print("your username is "+save_username)
 	 save_password = input('enter a password for your game\n')
 	 print('your password is '+save_password)
 	 file1 = open('aery_saved_password_'+save_username+'.txt','w')
 	 file1.write(save_password)
 	 file1.close
 	 valid_answer = 0
 	 while valid_answer == 0 :
 	  player_race = input('what race are you, '+save_username+'? please choose out of elf, human, dwarf, or dragonborn.\n')
 	  if player_race == 'elf' or player_race == 'human' or player_race == 'dwarf' or player_race == 'dragonborn' :
 	   valid_answer = 1
 	   file1 = open('aery_saved_race_'+save_username+'.txt','w')
 	   file1.write(player_race)
 	   file1.close()
 	   time.sleep(0.5)
 	   print("your race is "+player_race)
 	 valid_answer = 0
 	 while valid_answer == 0 :
 	  player_class = input('what class are you, '+save_username+'? please choose out of warrior, archer, wizard, or paladin.\n')
 	  if player_class == 'warrior' or player_class == 'archer' or player_class == 'paladin' or player_class == 'wizard'  :
 	   valid_answer = 1
 	   file1 = open('aery_saved_class_'+save_username+'.txt','w')
 	   file1.write(player_class)
 	   file1.close()
 	   time.sleep(0.5)
 	   print("your class is "+player_class)
 	 file1 = open('aery_current_location_'+save_username+'.txt','w')
 	 file1.close()
 	 valid_answer = 0
 else :
 	print('please enter either "y" or "n"')
if tutorial_needed == 1 :
	time.sleep(0.3)
	print('Welcome to aery, '+save_username+' the '+player_race+' '+player_class)
	time.sleep(0.8)
	print('Seeing as this is your first time playing you might want to know how!')
	time.sleep(0.8)
	print('type "t" and select "the toot orial" to travel to the tutorial')
else :
	time.sleep(0.5)
	print('Welcome back to aery, '+save_username)
	file1 = open('aery_current_location_'+save_username+'.txt','w')
	location = file1.read()
	travel_locations.remove(location)
	travel_locations.append('spawn')
while True :
	time.sleep(0.5)
	action = input('what do you do?\n')
	if action == 'check' :
		print('you are '+save_username+' the '+player_race+' '+player_class)
	if action == 't' or action == 'travel' :
		traveling_to = input('choose a location : '+str(travel_locations)+'\n')
		if traveling_to in travel_locations :
			travel_locations.append(location)
			location = traveling_to
			travel_locations.remove(location)
			time.sleep(0.5)
			print('.')
			time.sleep(0.5)
			print('.')
			time.sleep(0.5)
			print('.')
			time.sleep(0.5)
			print('you have arrived at '+traveling_to)
			file1 = open('aery_current_location_'+save_username+'.txt','w')
			file1.write(traveling_to)
			file1.close()
		else :
			print(traveling_to+' is not in your travel list.\n')
	if location == 'the toot orial' :
		time.sleep(0.5)
		print('you are confronted by a very shouty floating trumpet')
		time.sleep(0.5)
		valid_answer = 0
		while valid_answer == 0 : 
		 action = input('do you talk to it or ignore it?')
		 if action == 'ignore' or action == 'ignore it' :
		 	valid_answer = 1
		 	print('you ignored it')
		 if action == 'talk to it' or action == 'talk' :
		 	valid_answer = 1
		 	print('you ask it if it knows were the toot orial is.')
		 	time.sleep(0.5)
		 	print('it replies with "I AM THE TOOT ORIAL, FOOL."')
		 	time.sleep(0.5)
		 	action = input('DO YOU HAVE A QUESTION FOR ME?')
		 	if action == 'yes' or action == 'y' :
		 	 valid_answer = 1
		 	 print('you said "yes",')
		 	 time.sleep(1)
		 	 print('you followed up with "how do you play this game?"')
		 	elif action == 'no' or action == 'nevermind' :
		 	 valid_answer = 1
		 	 print('you backed out of the conversation')
