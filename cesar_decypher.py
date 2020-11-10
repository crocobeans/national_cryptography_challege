import time                                 
def caesar_encrypt(realText, step):
	outText = []
	decryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']      # dunno my guy
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]     # ay oy wtf are these?????? they are letters 
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  
	for eachLetter in realText:
		if eachLetter in uppercase: #back up terry, back up. PUT IT IN REVERSE TERRy
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			decryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			newLetter = lowercase[crypting]
			outText.append(newLetter)
		
		elif eachLetter in numbers:
		    index = numbers.index(eachLetter)
		    crypting = (index + step) % 10
		    newLetter = numbers[crypting]
		    outText.append(newLetter)
		
		else :
			outText.append(eachLetter)

	
	return outText, step

print('input first few words')
inputText = input()

for i in range(26):
    code = caesar_encrypt(inputText, i)
    out = str(code)
    print("")
    print(out)
    print("")


print('input which variation it do be thicc doe')
while True:
	try:
		shift = int(input())
		break
	except:
		print('that is not a valid number')

print('input whole text')

inputText = input()

time.sleep(1)
code = caesar_encrypt(inputText, shift)
out = str(code)
print("")
print(out)
print("")
