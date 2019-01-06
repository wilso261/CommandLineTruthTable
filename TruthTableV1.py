import os
import sys
from TruthTalLineV1 import *

print("\n\n")
print("""
__        _        ____      _____      _____
| |      (_)      (____)    |__ __|    ( ____)
| |     ( _ )    ( )  (_)     | |     ( )     
| |    ( (_) )  ( )   ____    | |    ( )      
| |__   (   )    ( )_|____]  _| |_    ( )____ 
L____|   (_)	  (_____)   |_____|    (_____)
""")

TheInit = TruthLine("A^A")
TheInit.TheSybl

Lines = "------------------------------------------------------------------------------------------------"

Inpt = ""
def introduction(Inpt):

	Help = "Type in the Boolean equation below and a truth table for it will be generated.\nThe symbols that you are alowed to use are:\n"

	for Sym in TheInit.TheSybl:
		Help = Help + Sym + "  "

	if Inpt != "H" and Inpt != "h":
		Intro = "Welcome to the truth table generator.\n" + Help

		return Intro

	elif Inpt == "H" or Inpt == "h":
		ExtendHelp = "\n\n" + Lines + """\nTruth tables show all possible answers and number arrangements to a Boolean equation.
An example is: AvB, A and B are either 1 or 0 and the v symbol means "and".
Because there are 2 different letters in this equation there will be 4 lines in the truth table.
To generate a truth table type in an equation using letters to substitute as 1 or 0 
and any one of the symbols displayed below as the operators inbetween them.
No spaces are permitted inside the equation and operators must have a letter on either side of it like A<=>BvA
The negation symbol (¬) is the only exception to this rule, it must be placed between a symbol and a letter like Av¬B.\n""" + Lines + "\n\n" + Help


		return ExtendHelp
 
	return Help

Decpt = introduction(Inpt)
print(Decpt)


while Inpt != "Q" and Inpt != "q":

	Inpt = input('Type "H" for help, and Q to quit.\n')
	if Inpt == "Q" or Inpt == "q":
		continue


	elif Inpt == "h" or Inpt == "H":
		print(introduction(Inpt))

	else:
		try:
			TheEquasion = TruthLine(Inpt)
			print(TheEquasion.alltogether())
		
		except:
			print("Invalid_Input:\nType in either a Boolean equation, 'Q' to quit or 'H' for help.")

print("Program closed.")