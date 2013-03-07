from sys import exit

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
    return pow(num1, num2)

def mod(num1, num2):
    return num1 % num2

def engine(operator, num1, num2):
	dictionary = {'+':'add', '-':'subtract', '*':'multiply', 
	'/':'divide', 'square':'square', 'cube':'cube',
	'pow':'power', 'mod':'mod'}

calculation = raw_input("> ")
tokens = calculation.split(" ")

if str.lower(tokens[0]) == 'q':
    quit(0)

newstring = '%r' % tokens[0]
print newstring

# print dict["%r"] % newstring
