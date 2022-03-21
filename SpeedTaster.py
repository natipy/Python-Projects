from time import time
from timeit import default_timer as timer

def get_error_taster(latter):
    global WORD
    error = 0
    garbage = {}
    WORD = WORD.replace('\n', " ")
    for i in range(len(WORD)-1):
    	try:
    		if latter[i] != WORD[i]:
    			error+=1
    			garbage[i+1]={WORD[i]:latter[i],'line':i}
    	except:
    		error+=1
    
    return error,garbage

def get_speed_ratio(start, end):
	return round((end-start)/len(WORD),2)

print("Right the bellow sentence!")

WORD = """Python was created in the early 1990s by Guido van Rossum"""

print(WORD)

def main(user_input):
	return f"Finished in {end-start} second(s)\nErrors: {get_error_taster(user_input)}\n{get_speed_ratio(start, end)} sencond(s) per 1 latter."

if __name__ == "__main__":
	start = time()
	get_input = input("> ")
	end = time()
	print(main(get_input))
