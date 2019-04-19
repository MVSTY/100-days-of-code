import random as rnd
choice=1
movies=[]
movies.append('Legally Blonde')
movies.append('Get Out')
movies.append('A Perfect Getaway')
movies.append('Everest')
movies.append('Never Back Down')
#while(choice=='yes'):
moviename=rnd.choice(movies);
num=len(moviename)
guess=''

#print(len(guess))
while(choice<10):
	fail=10
	#print(guess)
	for i in moviename:
		if i in guess:
			#guess+=guesss
			print(i)

		else:
			print('_')
		
	guesss=input('guess the character: ')
	guess+=guesss
	for a in guess:
		if a not in moviename:
			fail-=1
			if fail==0:
				exit()
		
	print(fail)			

	
