unique_str = "AbCDefG"
non_unique_str = "non Unique STR"
#whether a given string is unique or not
#strings here have upper + lower mixture

def normalize(input_str):
#preprocess_the-string
#preprocessing is basically we change everything to lower case and remove the spaces, atleast in this context
	input_str = input_str.replace(" ", "")
#to remove the spaces with nothing 
	return input_str.lower()
	#will convert all alphabets to lowercase

#step 2: how to figure out whether they're unique or not
#approach here is we are going to use hash table
#check whether the char is present in the dictionary, if it isn't then input it into the dicF
#First we loop through the input string to see what chars are present, then we check whether that character is present in the dictionary
    def is_unique_1(input_str):
    	#checking whether the char is present in the dict using loops
    	d = dict() 
    	for i in input_str: #looping through the contents of input string
    		if i in d: #if i the character is in the dictionary, then it's going to loop through
    			return False #cause we have already encountered that character because its in that particular dictionary
    		else:
    			d[i] = 1 #d[i] is basically the character, maybe A , maybe B can be anything we give
    			return True #denote that we've  indeed encountered a unique string

unique_str = normalize(unique_str)
non_unique_str = normalize(non_unique_str)

print(unique_str)
print(non_unique_str)

---------------------------------------------

#approach_2

#set function gives you all the unique characters

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"
#whether a given string is unique or not
#strings here have upper + lower mixture

def normalize(input_str):
#preprocess_the-string
#preprocessing is basically we change everything to lower case and remove the spaces, atleast in this context
	input_str = input_str.replace(" ", "")
#to remove the spaces with nothing 
	return input_str.lower()
	#will convert all alphabets to lowercase

#step 2: how to figure out whether they're unique or not
#approach here is we are going to use hash table

    def is_unique_1(input_str):
    	#checking whether the char is present in the dict using loops
    	d = dict() 
    	for i in input_str: #looping through the contents of input string
    		if i in d: #if i the character is in the dictionary, then it's going to loop through
    			return False #cause we have already encountered that character because its in that particular dictionary
    		else:
    			d[i] = 1
    			return True

#approach 2
def is_unique_2(input_str):
	return len(set(input_str)) == len(input_str))

unique_str = normalize(unique_str)
non_unique_str = normalize(non_unique_str)

print(unique_str)
print(non_unique_str)

----------------------------------------

#loopthrough
#take n from the alphabet, move to o, then take o and so on, basically go one by one in the string
def is_unique_3(input_str):
alpha = "abcdefghijklmnopqrstuvwxyz"
#loop through input string
#if the character is in in input_str, then lets take that letter out of the alphabet
#then we are replacing the character with nothing

for i in input_str:
	if i in alpha:
		alpha = alpha.replace(i,"")
		#replacing with nothing
	else:
		return False
		#we use else because if we have already taken out the alphabet
		