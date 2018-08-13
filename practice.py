unique_str = "ABcDefG"
non_unique_str = "Hello this is me"

def normalize(input_str):
	input_str = input_str.replace(" ", "")
	#replacing input string with nothing
	return input_str.lower()

def is_unique(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False
		else:
			d[i] =1 
			return True			


unique_str = normalize(unique_str)
non_unique_str = normalize (unique_str)

print(unique_str)
print(non_unique_str)

---------------------------------

unique_str = "abirkd"
non_unique_str = " jnoidlnmlsk  ksdmd"

#preprocessing, removing blank spaces as well as turning all the alphabets into uppercase
def normalize(input_str):
	input_str = input_str.replace(" ", "")
	return input_str.lower()

def is_unique(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False
		else:
			d[i] =1 
			return True

-------------------------------------------------------------

unique_str = "iemdpodms;"
non_unique_str = "nsk;.  eld;"

def normalize(input_str):
	input_str = input_str.replace(" ", "")
	return input_str.lower()

def is_unique(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False
		else:
			d[i] = 1
			return False

unique_str = normalize(unique_str)
non_unique_str = normalize(non_unique_str)

print(unique_str)
print(non_unique_str)

----------------------------------


unique_str = "urksjl"
non_unique_str "qiwnasokls jldnkfm"

#preprocessing the string, checking and removing blank spaces as well as turning everything to lowercase
def normalize(input_str):
	input_str = input_str.replace(" ", "")
	return input_str.lower()

# #now we are checking whether our character is unique or not. 
# First we loop through the input string, then we check if the character is present in the dictionary, 
# after that if its' present we'll return false as we have already encountered that character. if it isn't then we add it to the dictionary and return true

def is_unique(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False
		else:
			d[i] = 1
			return True #denotes we've encountered a unique_str
-----------------------------------------

unique_str = "sfjdfns"
non_unique_str = "ibsrnodman"

def normalize(input_str):
	input_str = input_str.replace(" ", "")
	return input_str.lower()

def is_unique(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False
		else:
			d[i] = 1
			return False

			
====================================================

unique_str = "rnosd"
non_unique_str = " idnkl sdino"

input_str = input_str.replace(" ", "")
return input_str.lower()

def is_unique(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False
		else:
			d[i] == 1
			return True

---------------------------------------

unique_str = " ihkjbjk"
non_unique_str = "yhjl, tugbhn  pijmm"

input_str = input_str.replace(" ", "")
return input_str.lower()

def is_unique(input_str):
	d = dict()
	for i in input_str:
		if i in d:
			return False 
		else:
			d[i] == 1
			return True