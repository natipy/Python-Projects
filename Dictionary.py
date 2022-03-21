import json
from difflib import get_close_matches

DICTIONARY = json.load(open("simple_english_dictionary.json"))
text="""
***********************************************
*        WELCOME TO MY DICTIONARY       	*
*\tI HAVE MORE THAN 100k WORDS         		*
*****************************************
	"""
print(text.format(len(DICTIONARY)))
def Translate(word):
	keys = [key for key in DICTIONARY]
	if word in DICTIONARY:
		return DICTIONARY[word]
	elif get_close_matches(word, keys):
		i = input("Did you mean %s ? [Y/N]"%get_close_matches(word,keys))
		if i in ['Y','y','yes',"Yes"]:
			word = get_close_matches(word, keys)
			return DICTIONARY[word[0]]
		elif i in ["N",'n','no',"No"]:
			return "Sorry This word doesn't exists here"
		else:return "I don't understand your command"
	else:
		return "Sorry This word doesn't exists here"
while True:
	user_input = input("*******\tFIND WORD ")
	print(Translate(user_input))
