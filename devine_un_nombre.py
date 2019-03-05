#import random as r
#pour importer directement la methode depuis random
from random import randint

mon_nombre=randint(1,100)

nombre_essais=range(5)
for i in nombre_essais:
	essai=input('proposez une nombre ({0} essai) : '.format(i+1))
	if essai<mon_nombre:
		print('le nombre a devine est plus grand que {0}' .format(essai))
	elif essai>mon_nombre:
		print('le nombre a devine est plus petit que {0}'. format(essai))
	else:
		print('Bravo vous avez gagne en {0} essai(s)'.format(i+1))
		break

if essai !=mon_nombre:
	print('vous avez perdu')
	print('le nombre etait : {0} ' .format(mon_nombre))

print('Fin de jeu')