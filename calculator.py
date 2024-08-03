def add(a, b):
    answer = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(answer) + '\n' )

def sub(a, b):
    answer = a - b
    print(str(a) + ' - ' + str(b) + ' = ' + str(answer) + '\n' )
    
def mul(a, b):
	answer = a * b
	print(str(a) + ' * ' + str(b) + ' = ' + str(answer) + '\n' )
 
def div(a, b):
    answer = a / b
    print(str(a) + ' / ' + str(b) + ' = ' + str(answer) + '\n' )


while True:
	print('MASSA AWUKS CALCULATOR' + '\n' + 'A - Addition' + '\n' + 'B - Subtraction' + '\n' + 'C - Multiplication' + '\n' + 'D - Division' + '\n' + 'E - Exit' + '\n')
 
	operation = input('What are we doing today? ').lower()
 
	if operation == 'a':
		print('Addition')
		a = int(input('First number? '))
		b = int(input('Second number? '))
		add(a, b)
	elif operation == 'b':
		print('Subtraction')
		a = int(input('First number? '))
		b = int(input('Second number? '))
		sub(a, b)
	elif operation == 'c':
		print('Multiplication')
		a = int(input('First number? '))
		b = int(input('Second number? '))
		mul(a, b)
	elif operation == 'd':
		print('Division')
		a = int(input('First number? '))
		b = int(input('Second number? '))
		div(a, b)
	elif operation == 'e':
		print('See ya aligators')
		exit()
	
