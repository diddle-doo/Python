# Change of Characters
# if the string value is "Happy" h should be changed to next letter i
# if result is vowel then make it caps


def changeLetter(string):
	var="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result=""
	final=""
	vowel="aeiouAEIOU"
	for i in range(0,len(string)):
		if string[i] in var:
			temp = (var.index(string[i]))
			result=result+var[temp+1]
	for i in range(0,len(result)):
		if result[i] in vowel:
			final=final+result[i].upper()
		else:
			final=final+result[i]
	return final




#changeLetter("Happy")
print(changeLetter("happy"))
