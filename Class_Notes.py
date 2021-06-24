# noinspection PyUnresolvedReferences

print('Ignore this line.')

"""
------------
NEW DOCUMENT --> Class Notes: Python
------------
Flow of the go:
-> Number
-> String
-> Lists
-> Tuple
-> Dictionary
-> Sets
-> Flow Control
-> Looping
-> Function
-------------------------------------------
Content List
===========================================
0. Introduction
1. Data Types
	a. Number
		i> Integer
		ii> Float
		iii> Complex
	b. String
	c. List
	d. Tuple
	e. Dict
	f. Sets
2. Conditional statements
3. Loops
	a. For
	b. For else
	c. While
4. Functions
===========================================
-------------------------------------------
0. Introduction

Python: Python, founded by Guido Van Rossum in 1980s, is a general purpose programming language, and is also called
Interpreted language.
So, Python is a programming as well as scripting language.

Interpreted:- Means that we can run standalone commands, we need not declare a headerfile or main function or
so, we can just get the output we want by simply typing it on interpreter. When we interpreted line by
line, it is called interpreted mode.

But, when we run multiple line at the same time, it is called batch mode or scripting mode.
Python can virtually run on every machine that has an interpreter in it.

Python is a OOPS based language.
OOPS:- Object Oriented Programming structure.

Q: Difference between Program and Scripting language.
Ans:    +-------------------------------+-------------------------------+
		| 	     Program 		        |	     Script		            |
		|-------------------------------+-------------------------------|
		|A program is executed, i.e	    |A script is interpreted	    |
		|source code is first compiled	|So, it is a programming	    |
		|then it is executed then only	|language in which we write	    |
		|we see the result of the  	    |code to control another  	    |
		|compilation.			        |software.			            |
		|Therefore it tells computer 	|				                |
		|to perform certain tasks	    |				                |
		+-------------------------------+-------------------------------+

Standard IO: The method in which we can input or output data directly from Keyboard or Console
respectively is called standard Input Output.

Linker: A linker is useful in programming language where after compilation an output file (.o) is
generated which holds all necessary function for execution & links (.o) file to (.exe) file.

But Python is interpreted line by line without conversion into .output file.

Features of Python:
>Object Oriented
	>Supports Polymorphism
	>operation overloading etc.

>Indentation
	>Python uses spaces and tabs for indent, not curly braces.

>It's Powerful
	>Dynamic typing
		>On the spot error recognition
	>Library utilities
	>Automated memory management

>It's Portable
	>It can run on almost every machine with right interpreter installed.

>It's mixable
	>Python can be linked to components written in other languages easily.

>Easy to Use
	>Python Programs are compiled automatically to an intermediate form called
	 byte code, which interpreter then reads.

Python code execution
					 Runtime
	|-------|	    |-------|	    |=======|
	| A.py	| ----> | A.pyc | ---->	|  PVI	|
	|-------|	    |-------|	    |=======|
	Source		    Byte Code	    Python
	Code				            Virtual
									Interpreter

------------------------------------------------------------------------------------------------------------------------
** 	'is' is an Identity operator. -> Returns True if both the variable are the same object.
	'in' is an membership operator.
	'>,<,==,!=' are value operator.
	Sorted function always returns a list.
	While sorting a nested list, by default it sorts with the first item in the nested lists/tuples etc.
		T = [(0,1),(2,0),(-1,2)]
		therefore sorted(T) will be [(-1,2),(0,1),(2,0)] or we can use the sort method of the list as well.
	Iteration is traversing over a sequential data.
"""

"""
map() function in python.
		map function returns a map object after applying the given function to a given iterable [List, Tuple, etc.]
		Syntax:
			map(function, iterable)
"""
lst = [1,2,3,4,5]
n = map(str,lst)
# The map function will pass all the values in lst from str function, making all of
# them string.
print(n) # <map object at 0x03AF3100>

# The returned map object is then transformed into a list, tuple or set for accessing values.

#    ord and chr function
ord('c') # returns ASCII value of the given character.
chr(99)  # returns character of given ASCII value.

"""
I also need to know various other function in basic python such as zip etc.
"""

"""
1. Data Types

Python has several data types.

a. Number: Number is a type of data that deals with numbers, a number is a non segmentation quantity, so you can not
iterate over it.
Number data type is of 3 sub-types.
	i> Integer: This value is represented by int class. It contains positive or negative whole numbers (without fraction
	 or decimal).
		In Python there is no limit to how long an integer value can be, it works as long as your RAM can hold it.
"""
a = 10
type(a)  # <class 'int'>
"""
ii> Float: This value is represented by float class. It is a real number with floating point representation. It is
	 specified by
		a decimal point.
"""
a = 10.6
print(type(a))  # <class 'float'>
"""
iii> Complex: Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j.
		For example – 2+3j
"""
a = 10 + 6j
b = complex(10,6)
type(a)  # <class 'complex'>
type(b)  # <class 'complex'>
"""
**Complex part is usually referred by 'j' because while using python for electrical systems, it would make it
		difficult
		for engineers to identify complex part and current part.
"""
"""
**Sequence: In Python, sequence is the ordered collection of similar or different data types. Sequences allows to store
multiple values in an
	organized and efficient fashion. There are several sequence types in Python –
		b. String
		c. List
		d. Tuple
	Sequential quantities supports indexing.


b. String: In python, every character individually is treated as a string. The default method of input
(i.e. using input()) takes the user
entered value as a string. String is a segmentation quantity therefore we can iterate over it, getting individual
 character as an element.
Python supports 3 types of string
	1. ASCII-7: 128 characters from 0 to 127
	2. ASCII-8: 256 characters from 0 to 255
	3. UNICODE: unicode supports all characters ever made of every language, it also supports emojis etc.
String can be represented by single, double or triple quotes (: multi line string).
"""
a ='hello'
b = input()  # world
print(b) # ' world'
print(a+b)  # 'hello world'

"""
	String has various methods in it.

	''.join(x): this method joins the elements in a sequential datatype and returns a string.
"""

"""
c. List: Lists are just like the arrays, declared in other languages which is a ordered collection of data.
	It is very flexible as the items in a list do not need to be of the same type.
	To define a list we use comma separated values inside square braces. In List, ID does not change as list is
		a mutable quantity, so we can change the data inside list without changing it's ID.
	Lists in python are far more different than arrays in C, as in C, array stores element, but in Python particularly,
	rather than storing the data directly Lists stores the references to those values, so in Python 1st element of list
	acts as a variable holding the ID of the element stored in it.
"""

lst = [1,2,3,4,'hello']
type(lst)  # <class 'list'>
print(id(lst))  # 55732424
print(id(lst[0]))  # 9072768
print(lst[0])  # 1
lst[0] = 5
print(lst) # [5, 2, 3, 4, 'hello']


"""
d. Tuple: Just like list, tuple is also an ordered collection of Python objects. The only difference between type and
	list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by tuple 
	class. Tuples are defined using parenthesis '('data')', and once assigned, the data inside a tuple cannot be 
	changed, and ID of tuple is fixed.
"""

tup = lst
tup  # [5, 2, 3, 4, 'hello']
tup= tuple(tup)
tup  # (5, 2, 3, 4, 'hello')
print(type(tup))  # <class 'tuple'>
id(tup)  # 52821960
tup[0]  # 5
# tup[0] = 10
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     tup[0] = 10
# TypeError: 'tuple' object does not support item assignment.

"""
e. Dictionary: A Data structure in Python, Mutable, Unordered. Each item is a pair of Keys and Values.
	Dictionaries are also known as Associative Arrays or Hash tables.
	{key1:value1, key2:value2, } -> So the Item is called by using the key or the value.

	Ex: info = {'name':'Aryan','Class':'BTech'}
	info['name'] # 'Aryan' # If key not present then Key error prints.
	The data is fetched using key, think of them as Index in an Ordered Collection.

	Key and Value are separated using colon (:), items are separated using comma (,).
	Empty Dictionary is declared by empty braces {}.
	** Keys in a dictionary must be unique while values may or may not be. Keys must be of immutable data type [string,
	tuples, numbers].

	**Methods in Dictionary:
	To reduce length: clear, pop, popitem
	1. dict.clear(): Removes all the Item from the dictionary.
	Here we are emptying the dictionary rather than deleting it. To delete it we use delete function.
	2. dict.pop(): To remove the item of given key one. Pop also returns the data.
	3. dict.popitem(*No Argument*): To remove the item ( key and value pair ) last occurrence from dictionary. Return the
	 key and value in a tuple.
		Gives Error if the dictionary is empty. In Python 2 it would remove the alphabetically last element.

	>> What is deletion statement?
	Ans: We use del keyword to delete the object. If item is used after deletion it would raise NameError.

	>> Item Deletion, we delete the item in a mutable data type using del keyword.
	Dictionary also supports item deletion using del keyword.

	To increase the length of dictionary: update, setdefault, fromkeys
	4. dict.update(temp): To update the dictionary.
		We need to add data in temp dictionary using keys and values.
		Then we update the previous dictionary using temp
		dict.update(temp)
		if key is present in old then the value will be updated, if key is previously not present then new key is added.

	5. dict.setdefault(): set default value of key and value.
		If key is previously present then value is not updated.
		If key is not present then default value is added.
		dict.setdefault('marks',0) : Key and Value

	6. dict.fromkey(): Create dictionary with keys present in a List. Create a dictionary from a List of keys with Values
		'None' or given.
"""

K = ['name', 'Class', 'Sec', 'Roll']
# dct = [{}/dict].fromkeys(K,Value[one to all])
# returns a dictionary type object by name dct.
dct = {}.fromkeys(K,'Value')
dct # {'name' : Value, 'Class' : Value, 'Sec' : Value, 'Roll' : Value}

"""
	7. dict.copy(): Returns the copy of the dictionary.
		This function creates a new copy of the data which is not interconnected ( by default in python when have the
			same object )
		dc = dict.copy()
		dc will have exactly the same value as of dict but will not be connected.

	8. dict.get(): return the value using key search.
		return the value of the key if key is present or else returns None if not found.
		The direct key search raises error if key not found but get does not do that.

		The environment where single evaluation takes place ',' spaced data generates a tuple only.
		 # using direct key search over a tuple.
"""

dct = {(2, 4): 10, (3, 6): 23, 3: 100}
v = dct[(2, 4)]
v # 10

v = dct[2, 4]
v # 10
""" 
	   This also returns the value as a tuple hinting that inside square braces of dict we have single evaluation
		environment.
"""

dct.get((2, 4)) # This also works as same when searched by direct method.
10

# ++but but when inside parenthesis, ',' separated values are not data but arguments.

dct.get(3, 6)
100

# prints 100 as key associated with 100 is '3'.
#       if not found the key in 1st argument it returns the second argument, as it is the default data.

"""
	9. dict.items(): returns the list of items in form of tuple.
"""
dct = {'1':'a','2':'b','3':'c'}
v = dct.items()
print(v) # dict_items([('1', 'a'), ('2', 'b'), ('3', 'c')])
# type of v is dict_items
"""
	10. dict.keys(): return the list of keys.
		return type is dict_keys.

	11. dict.values(): return the list of values.
		return type is dict_values.

	Q: How to sort a dictionary using values?
	Ans: Program to do sort according to values in a dictionary.
		>>> dct = {'1':'a','2':'b','3':'c'}
		>>> itm = list(dct.items())
		>>> itm.sort(key = lambda x: x[1])
		>>> print(itm) # [('1', 'a'), ('2', 'b'), ('3', 'c')]
"""
"""	
    Q: Write a Python Program to check given list is sorted or not?
	Ans: Program
"""

ls = list(map(int,input().split()))
print('sorted') if ls == sorted(ls) else print('Not Sorted')

"""
f. Sets: Data structure supported by python, Mutable, unordered. It does not have the concept of Indexing, 
    and does not contain duplicate elements. They are denoted by {} 'Curly Braces'.
	s = {1,2,3} # Defines a set. ** By default using s = {} will not make an empty set, rather an empty dictionary.
	Therefore empty Set is denoted by s = set() # Constructor of Set class. 
	when we print an empty set, it prints 'set()'.
	We can not include a set inside a set, as set are mutable but we cannot include mutable types into a set.
	Hash [A Number for a variable] can only be found of elements having fixed length.
"""

hash('aryan')
-858164902
hash([1,2]) # TypeError: un hashable type: 'list'

"""	
	How to access the value in a set, as it is an unordered quantity, we use iteration to get the data.

	** The elements of sets must be immutable but set itself is mutable. Only immutable elements could be stored in set.

	** Only Mutable data type in Python in which Modification is not possible, but updation or addition of elements is
	possible.
	Sets are Mutable:
"""

s = {1,2}
s.add(10)
print(s)
{2,1,10} # elements can be in any order.

"""	
	2> we can also use update method, which adds more than one element in a single turn.
	s2 = {11,12} or s2 = [11,12] or s2 = (11,12) or s2 = 'abcd' #in case of string every character is added one by one.
"""
s2 = [11,12]
s.update(s2)
print(s)  # {2,1,11,10,12}

"""	
    While using update it is to remember that we can use any datatype to iterate the values but, even in those values
	all elements must be of immutable type.

	To remove elements we use pop and remove methods.
	3> Where pop will delete arbitrary element from the set.
"""

s.pop()
print(s)
{2,1,11,12}

" 4> Remove will delete a specified element. "
s.remove(11)
print(s)
{2,1,12} # If element is not found then it raises a KeyError.

"""	
	5> There's also another method called discard which functions the same as remove but, Unlike remove it does not
	raises an exception if the element is not found.
"""

s.discard(5)
print(s)
{2,1,12}

" 6> clear method empties the Set. "

s.clear()
print(s)
set()

# Operations on Set.
s = {1,2,3,4}
s2 = {1,2,3,4,5}

"""
	len(s) -> Length of set 's' : 4
	x in s -> Membership of 'x' in 's'
	
	2 in x: True					                                -----Equivalent Expression----
	s.issubset(s2): Checks whether s is a subset of s2 or not. 		        [s<=s2]
	s.issuperset(s2): Checks whether s2 is superset of s or not. 		    [s>=s2]
	s.union(s2): Gives the union of s and s2. 				                [s|s2]
	s.intersection(s2): Gives the intersection elements of s and s2. 	    [s&s2]
	s.difference(s2): Returns elements which are in s but not in s2.	    [s-s2]
	s.symmetric_difference(s2): (Union - Intersection) elements. 		    [s^s2]
	s.copy(_): A new copy of s.
	s.intersection_update(s2): Does not return but add the missing data in s.
	s.difference_update(s2): Similar difference is updated in s.
	s.symmetric_difference_update(s2): Terms which are not in s and s2 are then assigned to s.
	s.isdisjoint(s2): Tells whether s and s2 are disjoint sets. (No Common Elements)

	max,min,sum and sorted functions also work on sets.

	** frozenset : A set which is immutable.
		s = {1,2,3}
		s = frozenset(s)
	-- Now none of the methods which could either add or remove elements from the set will not work. --

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

"""
Functions:
	Function is a group of related statements that perform a specific task.
	Function breaks the program into modules and help us to make it more readable and understandable.
	It also helps us to reduce the size of program as we can use a function to do same thing at multiple places without
	actually writing the whole code multiple times.
	Function making helps us to identify the bug easily in the code, as bug in a function is easily catched.

	There are 69 built in functions in Python.

	def function_name(parameters): # Function definition
		code or function body

	function_name(parameters) # Function call

	def keyword is used to define functions.
	Function definition is only called when function is called.

	   Parameter		Return Type
	1. No param 		No Return
	2. Param 		    Return
	3. No Param 		Return
	4. Param 		    No Return

	If function does not return anything it returns 'None', default return type.

	Examples:
	1. def fun():
		print('hello')

	2. def fun(a,b):
		return a+b

	3. def fun():
		a = int(input())
		return a*5

	4. def fun(a,b)
		print(a*b)

	Arguments which are given during the function call are called Actual Parameters or Actual Arguments.
	Arguments which are given during the function definition are called Formal Parameters or Formal Arguments.
	No. of Formal parameters must match No. of Actual Parameters.
		If this does not comply, error occurs ' Required positional Arguments '.

"""
"""
Types of Arguments:
		1. Positional Arguments
			Every argument having fixed position.
"""

def sm(x,y):  # Function Header
	return x**2+y**3

H = sm(3,6) # Function Calling
print(H)

# Here the result matters over the value at position given during the function calling.

# a. Variable Length Arguments or optional positional arguments
#     ** Handling more than required.

def sm(x,y, *d): # Function Header # Here x,y are required positional argument but *d is
	# optional positional arguments. d stores the values as a tuple.
	# we can use values in d as
	return x**2+y**3 + sum(d)
H = sm(3,6,2,3,4,5,77) # Function Calling
print(H) # 316
"""
				here the 3,6 are required positional arguments so they are the values given to power function but the
				other arguments given will stored in d and have sum using sum function.
				The important thing to understand is that if there are required argvs given after optional, they will
					not get the values as values are stored in optional argument.
				In order to do that we give them by name, Keyword Argument.
"""

def sm(*d, x, y): # Function Header # Here x,y are required positional argument but *d is
	# optional positional arguments. d stores the values as a tuple.
	# we can use values in d as
	return x**2+y**3 + sum(d)
H = sm(3,6,2,3,4,x=5,y=77) # Function Calling
print(H) # 456576

# b. Default Arguments
# Handling less than required.
def display(*x,sep=' ',end='\\n',q):
	st_list = list(map(str,x))
	h = sep.join(st_list)
	print(h, end=end)


# noinspection PyArgumentList
display('a',1,2,3,'b',sep='*')  # a*1*2*3*b\n
# Non Default arguments cannot follow default arguments.
# def display(sep=' ', end='\n',x)  # This type of syntax will generate error.

"""      
        2. Keyword Arguments
			Call parameter by name.
			When we call a function with some values, these values get assigned to the arguments according to their
			position. They also follow positional arguments.
"""
def sum_num(x,y,z):
	return x**1+y**2+z**3

a,b,c = map(int,input().split())
s = sum_num(a,b,c)
r = sum_num(a,c,b)
print(s,r)

# both s and r will have different values. To deal with this we use keyword arguments.

def student_info(name, section, roll_number, subject):
	info = f'''
		Name : {name}
		Section : {section}
		Roll Number: {roll_number}
		subject : {subject}
	'''
	return info
k = student_info('aryan','D',5,'Python') # here info is given in the form of positional argvs.
print(k)
V = student_info( roll_number=34,  section='E', subject='Python Programming', name='ravi')  # function

# calling using keyword argvs.
"""
			In Keyword arguments it does not matter what is the order of the argument is what matters is that if we are
			supplying enough data using the correct keywords.

			a. Optional Keyword Arguments ( Variable Length Argument )
				In optional keyword arguments the data stored in formal parameter is stored as the same type of
				dictionary. Where the correct key refers to the required data.

"""

def student_info( **dct):
	info = f'''
		Name : {dct.get('name')}
		Section : {dct.get('section')}
		Roll Number: {dct.get('roll_number')}
		subject : {dct.get('subject')}
	'''
	return info
V = student_info( subject='Python')  # function calling
print(V)
# If nothing is passed then the default value is None.

"""
		Q: WAP to get every keyword argument correctly if letter are not in the same case?
		A:  Solution Code Below:
"""
def student_info(**dct):
	ndct = {} # Creating a new temporary dictionary.
	for q in dct.keys():
		val = dct[q] # Temporarily storing thr value associated with key 'q' from the dictionary dct.
		q = q.lower() # changing 'q' to lower case.
		ndct[q] = val # Assigning a new lowered key 'q' and old value val to the new dictionary ndct.
	dct = ndct.copy() # copying new dictionary to the old one for no more variable change.
	del ndct # Deleting new dictionary to reduce space usage.
	info = f'''
		Name : {dct.get('name')}
		Section : {dct.get('section')}
		Roll Number: {dct.get('roll_number')}
		subject : {dct.get('subject')}
	'''
	return info

print(student_info(Name='Aryan', secTiOn='A'))

"""
	Variable in a Function:
		1. Local: Variable inside a function.
		2. Global: Variable outside a function.
		3. Non-Local: Variable inside a function of function (nested function)
"""
def info():

	def second():
		var = 0 # Local Variable of function second().

	def third():
		# global is a key word which gives permission to function make changes in Global variable
		# by the same name.
		global var
		var = 22

	def fourth():
		# The keyword nonlocal gives the function the ability to change the value of local variable of
		# parent function, which is info in this case, therefore the value of val in info will now be 1.
		nonlocal var
		var = 1 # Non local variable of info function.

	var = 10 # Local Variable of info function
	second()
	print(var) # as variable is in info function then prints 10
	third()
	print(var) # prints 10
	fourth()
	print(var) # prints 1

var = 100 # Global Variable
print(var) # prints 22
"""
		VVIP: In a function we can only declare one type of environment.
		Flow of the example code:
			> first a global environment is set up and a variable var is initialized having value 100.
			> then a local environment of info is set up, a local variable of info, var is initialized having value 10.
			> again local environment of function second inside function info is set up having a local variable of
				second, var with value 0.
			> then a function third is defined but having a global environment as var in third is actually the var in
				global environment.
			> then a function fourth is defined but having a non local environment which means it will have the variable
				var but the var is associated to the function just parent of fourth function, which is info function.
			> After this we print different values.

	If by default no variable is declared in function but read operation takes place, then it takes the value from the
	global scope.
"""
def fun():
	print(k)

k = 100
fun() # prints 100

# but, problem occurs when:
def fun():
	# print(k) # Global k
	k = 23 # This will generate error as we are declaring var as local variable but we've used it as global.

k = 100
fun()

# Scope of variable:
def fun(k): # k = k # here k is assigned as local variable.
	# global k # Raises error as both scope clash in same function.
	print(k)

k = 100
fun(1)

"""
	Formal Parameters are by default local variables.

	Anonymous Function [Lambda Function]
		This is a function without a function name.
		This type of function is defined using the keyword lambda, hence it is also called lambda function.
		Can have any number of arguments but only one expression.

		syntax
			var_name = lambda arg1, arg2: expression(return statement)

		Ex:
		>>> sum_num = lambda a, b: a**2 + b**2 # here sum_num is not a function name, yet a variable name.
		>>> v = sum_num(2,5)
		>>> print(v) # 29

"""
"""
	Uses of lambda
		1. with map():
"""

lst = [10, 20, 98, 45, 23]
nls = list(map(lambda x: x-2,lst))
print(nls) # [8, 18, 96, 43, 21]

"""
		2. list.sort() method
			sort according ascii weight [ sum of ascii values ].
"""

lst = ['ravi','aman','chaman','chayanika','aniket','ankit']
lst.sort(key = lambda x: sum([ord(z) for z in x]) )
lst # ['aman', 'ravi', 'ankit', 'chaman', 'aniket', 'chayanika']

"""
		3. filter(): Filter the items based on expression logic
			Syntax:
				filter ( expression or function which returns in True or False, iterator )
"""

lst = [10, 20, 98, 45, 23]
# Filter items less than 30
nls = list(filter(lambda x: x<30,lst)) # Reduces the length of list.
print(nls) # [10, 20, 23]

"""    
	Q: Write a Python program to detect the number of local variables declared in a function?
	Ans: So if we define a function we can use a private method.
		suppose if a function fun has local variable a,b then
		>>> def fun():
		>>>     a=10; b=20
		>>> print(fun.__code__.co_argcount) # 2 no. of local variables
		**something.__(anything)__ these type of methods are private class methods and are not used regularly.
"""
"""
	Documentation:
		__doc__ -> Docstring
		Every function has this doc string which is the first thing written after function declaration line
		It could be a multi or a one line string, and holds information about the function, it tells what is the work
		of function and what is the function calling format. It is very important when we do, professional programming.

"""
def example(*x):
	"""
	This function takes input of any amount numbers and return their sum.
	example(*variable) <- Input format
	"""
	return sum(x)

"""
		Now for knowing what is the docstring of that function or class or any module.
		we have a private method.
		function/class/module_Name.__doc__
		>>> example.__doc__
			This will print the docstring of this function.
"""
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

File Handling:
	Reading and writing operation with local files.
	Standard I/O
		Was data inputted with the help of keyboard and output of data using screen.
		we used print() and input()

	Q: What is a file?
	Ans: An information stored permanently in our memory, it can be path Active [ Currently in use ] or Passive
		[ not in use ].

	> Write the first data in file:
		open(filename, mode): built-in function for file handling to open the file.
		mode-> 'w' to write if file does not exist.
		default location: if we run the python code in interpreter mode than the file is saved where the interpreter is
			installed. If we run the file in PyCharm and run a complete code then the file is saved in the directory
			in which the code is saved.

	> modes:
		'r': default value of mode, open file in read mode. Generates error if file not found.
		'w': open file in write mode, creates a file if not found and never adds on, completely new.
			This mode truncates the file, which means, it deletes the previous file and then re writes it.
		'a': open file in append mode, adds on the data previously existed in file.

		'rb': read mode but for binary file.
		'wb': write mode for binary file, new file generation everytime.
		'ab': append previous file in binary mode.

		'r+': read and write mode, (file not truncated)
		'w+': read and write mode, (file always truncated, File is deleted first then it's written)
		'a+': write and read mode, we can slo append file.
		'rb+': read and write in binary ( file not truncated )
		'wb+': read and write in binary ( file truncated )
		'ab+': write and read mode, with append, in binary.

"""

# Ex: Simple File formation.
f = open('E:\\FileHandling\\addition.txt','w') # creates a file in the given directory and give all permission to f.
num1 = 10; num2 = 20
f.write(f'The addition of {num1} and {num2} is {num1+num2}.') # writes in the file.
f.close() # closes the file.

"""
	The return type of write method is int, it return the number of characters entered in a file.
	That can also be used in execution of some programs.

	Extension:  Giving the extension is not necessary, the extension just defines that by which application the windows
				will open the file by default. We can give absolutely any extension to the file.

"""
""" 
	Q: WAP to display the table of 1 to 10 in a file.
	A: Program
		>>> ls = [ [ q for q in range(p,p*10+1,p) ] for p in range(1,11) ]
		>>> f = open('E:\\FileHandling\\table.txt','w')
		>>> for q in ls:
		>>>     ff.write('\t'.join(list(map(str,q))))
		>>>     f.write('\\n')
		>>> f.close()
"""
	# Ex: Open file in read mode.
f = open('E:\\FileHandling\\table.txt','r')
data = f.read() # reads entire data of the file in form of a string.
print(data)
f.close()
"""
	If file does not exist then it'll give error as FileNotFound.

	Ex: Reading the specific data
	f.read(<int>) > No. will represent that it'll read 10 characters from the file, from the beginning.
"""
f = open('E:\\FileHandling\\table.txt','r')
data1 = f.read(10) # reads starting 10 characters of the file in form of a string.
print(data1) # print only 10 starting characters.
data2 = f.read(5) # this reads the next 5 characters from the file.
data3 = f.read() # this will read the entire remaining data.
f.close()
"""
	So the read method of file takes the cursor with it.
	once if we did f.read() and complete data is read, then we cannot read anything else,
	we cannot seek in the data, seeking is only available in binary.

"""

# > readline(): Reading single line from the file, till it does not reads a '\n', works in read mode.
f = open('E:\\FileHandling\\table.txt','r')
L1 = f.readline() # reads the first line of the file.
print(L1) # print only 10 starting characters.
L2 = f.readline() # reads the second line of the file.
f.close()

"""
	f.readline(argv) the argument gives the number of character to read in a line, if it gets
		'\n' before then it'll stop, or if we have more than that, then it'll stop after number of characters.
		Now in the case where there is data remaining the first line, then the cursor will be at that point in
		line, and from that point to the next '\n'.

"""
f = open('E:\\FileHandling\\table.txt','r')
L1 = f.readline(10) # reads the first line till given chars or '\\n' .
print(L1) # print only 10 starting characters.
L2 = f.readline() # reads from the last cursor location to the next '\\n.
print(L2)
f.close()

	# > readlines(): Read the entire lines in the text in form of list of lines.

f = open('E:\\FileHandling\\table.txt','r')
Data = f.readlines()
print(Data) # Data is in the form of list.
f.close()

	# f.readlines(argv): The argument in here represents the number of lines to be read.

f = open('E:\\FileHandling\\table.txt','r')
Data = f.readlines()
print(Data)
f.close()

"""
	The object of file < variable in which we open file > also iterates over its data line by line.

	Q: What would be the output of the following code snippet.
				q = iter([1,2,3,4])
				for i in q:
					print(i)
					next(q)
	Ans:1
		3
		This output would come as we are skipping the quantities in q by using next. And if we had an odd number of data
		then we might face StopIteration as the data in the iterator might as well get exhausted.

	UnsupportedOperation Error occurs when we open file in one mode and performs operation of other mode.
"""
""" 
	Writing in file.
		using basic f.write:
		we use 'w' mode to write in a file.
"""

f = open('E:\\FileHandling\\texts.txt','w')
f.write('Hello World!') # Current Location 0
f.write('\\nWe are not fine') # Current Location Starting of Line 2.
f.close()

# Now, If we are using f.writelines()
# This we use when we want to type a data from sequential data type to a file.
f = open('E:\\FileHandling\\texts.txt','w')
lst = [' Problems are:',' Global Warming',' Coronavirus',' Etc..']
f.write('Hello World!') # Current Location 0
f.write('\\nWe are not fine') # Current Location Starting of Line 2.
f.writelines(lst)
f.close()

"""
		** Important to learn : 'Pagination' to show a particular data in a form having particular number of data in a line,
		then we change the line so as we do not need to scroll left.

	Q: WAP to write odd numbers in given range by user into a file.
	A: Steps while doing a file...
		1. open the file, if new then we create the file.
		2. do the process, read or write or append.
		3. close the file.
		Code:
"""
# Solution Code:
f = open('E://FileHandling//Odd.txt','w')
C = 0 # Length of line.
for q in range(1,101,2):
	f.write(f'{q} ')
	C+=1
	if C==10:
		f.write('\n')
		C = 0
		f.close()
"""
	Appending a file
		Adding an extra data to a previously existing file.
		This method adds on the data from the previous cursor point.

"""

f = open('E://FileHandling//texts.txt','a')
f.write('\\n nut He wants to become better.')
f.close()

"""
	Binary file:
		mp3, mp4, jpg, etc..

		'\r\n' is also a new line, but in Linux.
"""
# Writing in binary file.
f = open('E://FileHandling//new_binary','wb')
# f.write('Hello World') # This would generate error as while writing binary file we need byte data.
f.write(b'Hello World') # encoding string data into binary.
f.close()
"""
			To convert data into binary we can either use
				1. make string as b'string'
				2. using encode method of string
					st = 'aryan'
					st = st.encode()
					this would make the string binary.

"""

# Reading a binary file.
f = open('E://FileHandling//new_binary','rb') # rb is read binary mode.
data = f.read()
print(data)
f.close()

# To convert the data into a normal file, we use decode method of string.

# f.read(argv) -> tells about no. of characters to read.

f = open('E://FileHandling//new_binary','rb') # rb is read binary mode.
data = f.read(5) # reads first 5 characters. Cursor is at 6th Character.
print(data)
data = f.read(5) # reads 5 more characters from last cursor point.
f.close()

"""
			f.tell() tells where the cursor is at in the file currently.

			f.seek(offset, origin) # used to take cursor at a particular point.
				offset -> any integer
				origin:
					0: beginning # when seeking from the beginning, we do not use negative offset.
					1: current
					2: last
			By default when we open a file, the position of cursor is 0.

"""

# Using seek method:
f = open('E://FileHandling//new_binary','rb')  # rb is read binary mode.
f.seek(-5,2)  # Cursor goes to -5 from the end.
data = f.read()  # reads all characters from last cursor point.
print(data)
f.close()

# Appending a binary File.
f = open('E://FileHandling//new_binary','ab')
f.write(b'\nNew data Edit')
f.close()

"""
Editing Files in Hybrid Mode:
	w+ : Write and Read permission.
		In any operation of w [w, w+, wb, wb+] file is always truncated.
		the w+ mode is used when we make a new file and we constantly edit the file and we 
		also want to preview it.
		
"""

f = open('E://FileHandling//texts.txt','w+')  # Even if the file was existing, it'll delete it and create a new one.
f.write('Hello, How are you?')  # Writing the line.
f.seek(0, 0)  # Seeking at the beginning of file.
data = f.read()
print(data)
f.write('\nNow Adding more data to it.')  # Now adding one more line.
f.seek(0, 0)  # Seeking again at the beginning of file.
data = f.read()
print(data) # This will print both of the lines.
f.close()

"The best function of w+ mode is that we do not need to close the file to see the changes we make throughout."

"""
	r+ : Read and Write mode
		This will not truncate the file yet, it'll read the file and will also edit it.
		We can also overwrite the previously existing data.
"""

f = open('E://FileHandling//texts.txt','r+')  # Even if the file was existing, it'll delete it and create a new one.
# By default it'll add data in the starting.
f.write('Some Extra data')  # Writing the line.
f.seek(0, 0)  # Seeking at the beginning of file.
data = f.read()
print(data)
f.close()


# Program to read a number of lines entered by the user.
f = open('E://FileHandling//table.txt','r')
for i in range(int(input('Enter no. of lines: '))): print(next(f))
"Try Writing the python solutions in minimal way possible."
"That shows how efficient as a coder you are, it will also increase your syntactical knowledge."


