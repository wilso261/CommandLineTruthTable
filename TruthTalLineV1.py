class TruthLine():
    
	TheAlf = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","W","w","X","x","Y","y","Z","z"] #Does not contain lowercase v
	TheSybl = ["^","v","¬","<=>","<=","=>","(",")"] #lowercase v is considered a symbol not a letter so is not given a value.
	
	def __init__(self, __Eqline):
		self.__Eqline = __Eqline # The equation as a string
		self.__TheLetters = {}

		self.__Eqlist = __Eqlist = [] # List form of the string equation: Eqline

		self.__ThePowlet = {} # List of each letter with values of powers of 2 This will not be edited once it is made.
		self.__Count = 0 # Used to incrementally increase powers
		
		
		for I in __Eqline:
			__Eqlist.append(I)
			
			if I not in self.__TheLetters and I in TruthLine.TheAlf: #places each letter in __TheLetters as a dictonary with value 1
				self.__TheLetters[I]="1"
				self.__ThePowlet[I]= 2 ** self.__Count
				self.__Count += 1

		self.__CThePowlet = dict(self.__ThePowlet) # The one edited later
		self.__ItterLen = 2 ** len(self.__TheLetters) # This is how many times it must loop






		
	def linePrinter(self):
		"""returns an individual line of the equation replacing
		   letters with there dictonary values, either 1 or 0"""

		Line = []
		Index1 = 0
		LenOfEql = len(self.__Eqlist)

		while Index1 < LenOfEql:
			
			if self.__Eqlist[Index1] in TruthLine.TheAlf:
				Line.append(str(self.__TheLetters.get(self.__Eqlist[Index1])) + " ")

			elif self.__Eqlist[Index1] == " ":
				Index1 += 1
				continue

			elif self.__Eqlist[Index1] == "<" and self.__Eqlist[Index1 + 2] != ">": # check for left implies
				Line.append("<= ")
				Index1 += 1

			elif self.__Eqlist[Index1] == "<": # check for equivalent sign
				Line.append("<=> ")
				Index1 += 2

			elif self.__Eqlist[Index1] == "=": # check for right implies
				Line.append("=> ")
				Index1 += 1

			else:
				Line.append(self.__Eqlist[Index1] + " ")
				#self.Line.append(" ")

			Index1 += 1

		Line.append(" = ")
		
		return Line





	def spacelessLine(self,callist):
		"""returns the line but with no spaces and with <= replaced with <,
		   => replaced with >, the negation sign replaced with - (if encoding is only ASCII) and <=> replaced with =.
		   This is to make it easier to calculate. Not for printing!"""
		__callist = callist
		SPLine = []
		IndexLine = 0
		while IndexLine < len(__callist):

			if __callist[IndexLine] == " ":
				pass

			elif __callist[IndexLine] == "<" and __callist[IndexLine + 2] != ">": # check for left implies
				SPLine.append("<")
				IndexLine += 1


			elif __callist[IndexLine] == "<": # check for equivalent sign
				SPLine.append("=")
				IndexLine += 2


			elif __callist[IndexLine] == "=": # check for right implies
				SPLine.append(">")
				IndexLine += 1

			#If negation sign is not working then use - instead, other changes will need to be made to look for - instead of ¬
			#elif __callist[IndexLine] == "¬": # check for negation sign
			#	SPLine.append("-")


			elif __callist[IndexLine] in TruthLine.TheAlf:
				SPLine.append(self.__TheLetters.get(__callist[IndexLine]))


			else:
				SPLine.append(__callist[IndexLine])

			IndexLine += 1

		return SPLine


				
	#Next section contains the logic calculator methods
#-----------------------------------------------------------------------------------------------------------------------------
	

	def logic_and(self,num1,num2):
		"""num1 ^ num2"""
		num1 = int(num1)
		num2 = int(num2)
		return int(num1 and num2)

	
	def logic_or(self,num1,num2):
		"""num1 v num2"""
		num1 = int(num1)
		num2 = int(num2)
		return int(num1 or num2)

		
	def logic_not(self,num1):
		""" ¬ num1"""
		num1 = int(num1)
		return int(not num1)

		
	def logic_equivalent(self,num1,num2):
		"""num1 <=> num2"""
		num1 = int(num1)
		num2 = int(num2)
		return int(num1 == num2)

		
	def logic_impliesLeft(self,num1,num2):
		"""num1 <= num2"""
		num1 = int(num1)
		num2 = int(num2)
		return int(num1 or (not num2))

	
	def logic_impliesRight(self,num1,num2):
		"""num1 => num2"""
		num1 = int(num1)
		num2 = int(num2)
		return int((not num1) or num2)
		
		
		

#-----------------------------------------------------------------------------------------------------------------------------



	def calcualteLine(self,calList):

		__calList = calList
		__CalcLine = TruthLine.spacelessLine(self,__calList)
		
		CurrentIndex = 0
		
		while CurrentIndex < len(__CalcLine): # The () loop

			
			if __CalcLine[CurrentIndex] == "(": # First checking for brackets
				#print("Brackets")
				indexNum = CurrentIndex # index of first open bracket and soon first element after that bracket
				lenLess = len(__CalcLine) - 1


				while __CalcLine[lenLess] != ")": # Used to find last enclosing bracket and its index
					lenLess -= 1


				del __CalcLine[lenLess] # Removes last bracket from list
				del __CalcLine[indexNum] # Removers first bracket from list
				
				BracketList = [] # list of elements inside found brackets
				lenLess -= 2

				while indexNum != lenLess: # Appends everything inbetween the two, now deleted, brackets to BracketList
					BracketList.append(__CalcLine[indexNum])
					indexNum += 1

				CalInBrackets = TruthLine.calcualteLine(self,BracketList) # end result of calculaing what was inside the found brackets
				__CalcLine.insert(CurrentIndex, CalInBrackets)

			CurrentIndex += 1



		IndexNot = 0
		while IndexNot < len(__CalcLine) - 1: # The - loop
			
			if __CalcLine[IndexNot] == "¬":	
				#print("Not")
				TheNot = __CalcLine[IndexNot + 1]
				AnsN = TruthLine.logic_not(self,TheNot)
				del __CalcLine[IndexNot + 1]
				del __CalcLine[IndexNot]
				__CalcLine.insert(IndexNot,AnsN)
				IndexNot -= 1

			IndexNot += 1



		IndexAnd = 0	
		while IndexAnd < len(__CalcLine) - 1: # The ^ loop

			if __CalcLine[IndexAnd] == "^":
				#print("And")
				TheAnd1 = __CalcLine[IndexAnd + 1]
				TheAnd2 = __CalcLine[IndexAnd - 1]
				AnsA = TruthLine.logic_and(self,TheAnd1,TheAnd2)
				del __CalcLine[IndexAnd + 1]
				del __CalcLine[IndexAnd]
				del __CalcLine[IndexAnd - 1]
				IndexAnd -= 1
				__CalcLine.insert(IndexAnd,AnsA)
				IndexAnd -= 1

			IndexAnd += 1

		IndexOr = 0
		while IndexOr < len(__CalcLine) - 1: # The v loop

			if __CalcLine[IndexOr] == "v":
				#print("Or")
				TheOr1 = __CalcLine[IndexOr + 1]
				TheOr2 = __CalcLine[IndexOr - 1]
				AnsOr = TruthLine.logic_or(self,TheOr1,TheOr2)
				del __CalcLine[IndexOr + 1]
				del __CalcLine[IndexOr]
				del __CalcLine[IndexOr - 1]
				IndexOr -= 1
				__CalcLine.insert(IndexOr, AnsOr)
				IndexOr -= 1

			IndexOr += 1

		IndexImpliesR = 0
		while IndexImpliesR < len(__CalcLine) - 1: # The > loop (Or Right implies)

			if __CalcLine[IndexImpliesR] == ">":
				#print("ImpR")
				TheIm1 = __CalcLine[IndexImpliesR - 1]# -
				TheIm2 = __CalcLine[IndexImpliesR + 1]# +
				AnsImR = TruthLine.logic_impliesRight(self,TheIm1,TheIm2)
				del __CalcLine[IndexImpliesR + 1]
				del __CalcLine[IndexImpliesR]
				del __CalcLine[IndexImpliesR - 1]
				IndexImpliesR -= 1
				__CalcLine.insert(IndexImpliesR, AnsImR)
				IndexImpliesR -= 1

			IndexImpliesR += 1


		IndexImpliesL = 0
		while IndexImpliesL < len(__CalcLine) - 1: # The < loop (Or left implies)

			if __CalcLine[IndexImpliesL] == "<":
				#print("ImpL")
				TheIm3 = __CalcLine[IndexImpliesL - 1]
				TheIm4 = __CalcLine[IndexImpliesL + 1]
				AnsImL = TruthLine.logic_impliesLeft(self,TheIm3,TheIm4)
				del __CalcLine[IndexImpliesL + 1]
				del __CalcLine[IndexImpliesL]
				del __CalcLine[IndexImpliesL - 1]
				IndexImpliesL -= 1
				__CalcLine.insert(IndexImpliesL, AnsImL)
				IndexImpliesL -= 1

			IndexImpliesL += 1


		IndexEq = 0
		while IndexEq < len(__CalcLine) - 1: # The = loop (Or equivelent) equivalent

			if __CalcLine[IndexEq] == "=":
				#print("Eq")
				TheEq1 = __CalcLine[IndexEq - 1]
				TheEq2 = __CalcLine[IndexEq + 1]
				AnsEq = TruthLine.logic_equivalent(self,TheEq1,TheEq2)
				del __CalcLine[IndexEq + 1]
				del __CalcLine[IndexEq]
				del __CalcLine[IndexEq - 1]
				IndexEq -= 1
				__CalcLine.insert(IndexEq, AnsEq)
				IndexEq -= 1

			IndexEq += 1
		Answer = str(__CalcLine[0])
		return Answer


#TODO: blocks of loops change to one block of code using inbedded while loop and numbers.


#------------------------------------------------------------------------------------------------------------------------
#The Method that pulls it all together
	
	def alltogether(self):
		"""This is the one that is called to use the others."""
		Persistent = 0
		TheWholeLst = ["\n\n"]
		while Persistent < self.__ItterLen:

			for I in self.__CThePowlet:

				if self.__CThePowlet[I] == 0:
					self.__CThePowlet[I] = self.__ThePowlet[I]
					self.__TheLetters[I]= int(not(self.__TheLetters[I]))
		
				self.__CThePowlet[I] -= 1
			
			
			Line1 = TruthLine.linePrinter(self)
			for elm in Line1:
				TheWholeLst.append(elm)
			#TheWholeLst.append(TruthLine.linePrinter(self))
			TheWholeLst.append(TruthLine.calcualteLine(self,self.__Eqlist))
			TheWholeLst.append("\n")
			Persistent += 1
		
		TheWholeStr = ''.join(TheWholeLst)
		return TheWholeStr


# order of operations = brackets, not, and, or, implies, equivalent
	
