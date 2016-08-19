__author__ = 'Drew'

import math

singleDigits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

thousands = ['', 'thousand', 'm', 'b', 'tr', 'quadr', 'quint', 'sext', 'sept', 'oct', 'non', 'dec', 'undec', 'duodec', 'tredec', 'quattuordec', 'quinquadec', 'sedec', 'septendec', 'octodec', 'novendec', 'vigint', 'unvigint', 'duovigint', 'tresvigint', 'quattuorvigint', 'quinquavigint', 'sesvigint', 'septemvigint', 'ovtovigint', 'novemvigint', 'trigint', 'untrigint', 'duotrigint']

illion = 'illion'

def convert100s ( number ) :
	if 0 < number and number < 20 :
		return singleDigits[number]
	elif number < 100 :
		tensDigit = int(number / 10)
		onesDigit = number % 10
		return tens[tensDigit - 2] + '-' + singleDigits[onesDigit]
	else :
		hundredsDigit = int(number / 100)
		tensDigit = int(( number % 100 ) / 10)
		onesDigit = number % 10
		return singleDigits[hundredsDigit] + ' hundred ' + tens[tensDigit - 2] + '-' + singleDigits[onesDigit]

def convertNumber ( number ) :
	if number < 1000 :
		return convert100s( number )
	else :
		newNumber = ''
		numDigits = len(str(number))
		numberOfChunks = int(math.log(number, 1000)) + 1
		chunkNumber = 0
		while chunkNumber < numberOfChunks and number >= 0 :
			truncateNum = 3
			if len(str(number)) < 3 :
				truncateNum = len(str(number))

			if chunkNumber >= 2 :
				newNumber = convert100s( int(str(number)[-truncateNum:]) ) + ' ' + thousands[chunkNumber] + illion + ' ' + newNumber
			else :
				newNumber = convert100s( int(str(number)[-truncateNum:]) ) + ' ' + thousands[chunkNumber] + ' ' + newNumber

			if str(number)[:-truncateNum] == '' :
				number = 0
			else :
				number = int(str(number)[:-truncateNum])
			chunkNumber += 1
		return newNumber


num = input( 'Enter a number to convert: ')
print( convertNumber(int(num)))