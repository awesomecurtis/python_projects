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
	print('A - Addition' + '\n' + 'B - Subtraction' + '\n' + 'C - Multiplication' + '\n' + 'D - Division' + '\n' + 'E - Exit' + '\n')
 
	operation = input('What are we doing today? ').lower()
 
	if operation == 'a':
		print('Addition')
		a = float(input('First number? '))
		b = float(input('Second number? '))
		add(a, b)
	elif operation == 'b':
		print('Subtraction')
		a = float(input('First number? '))
		b = float(input('Second number? '))
		sub(a, b)
	elif operation == 'c':
		print('Multiplication')
		a = float(input('First number? '))
		b = float(input('Second number? '))
		mul(a, b)
	elif operation == 'd':
		print('Division')
		a = float(input('First number? '))
		b = float(input('Second number? '))
		div(a, b)
	elif operation == 'e':
		print('See ya aligators')
		exit()
	
