import time                                 

def affine_crypt(realText, stepa, stepb):
	outText = []
	decryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']      # dunno my guy
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']     # ay oy wtf are these??????  they are letters
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	for eachLetter in realText:
		if eachLetter in uppercase: 
			index = uppercase.index(eachLetter)
			crypting = ((index * stepa) + stepb) % 26
			decryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = ((index * stepa) + stepb) % 26
			newLetter = lowercase[crypting]
			outText.append(newLetter)
		
		elif eachLetter in numbers:
			index = lowercase.index(eachLetter)
			crypting = ((index * stepa) + stepb) % 26
			newLetter = lowercase[crypting]
			outText.append(newLetter)
		
		else :
			outText.append(eachLetter)

	
	return outText


numbersa = [1,3,5,7,9,11,15,17,19,21,23,25]
numbersb = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

cryptext = input('input the encrypted text: ')

estText = input('input what you think the word is: ')

for a in range(0,11):
	for b in range(0,25):
		shifta = int(numbersa[a])
		shiftb = int(numbersb[b])
		outText = ''.join(affine_crypt(estText,shifta,shiftb))
		print(outText)
		if(outText == cryptext): 
			print('')
			print('')
			print('the encryption key is probably ', shifta,shiftb)
			break
		
		time.sleep(0.01)
	