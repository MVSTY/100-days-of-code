import random as rnd
choice='yes'
movies=[]
movies.append('Legally Blonde')
movies.append('Get Out')
movies.append('A Perfect Getaway')
movies.append('Everest')
movies.append('Never Back Down')
while(choice=='yes'):
	moviename=rnd.choice(movies);
	print('Following are the choice of movies:')
	print('\n'.join(movies))
	guess=input('Enter the name of the movie you think has been chosen:')
	if(guess==moviename):
		print('You Win')
	else:
		print('Try again')
	print('\nDo you want to try again??')
	choice=input('Enter yes or no: ')		
#print(moviename)
