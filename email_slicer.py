def main():
	print('Welcome To SliceX')
	email = input('What is your email address?: ')
	(username, domain) = email.split('@')
	(domain, extension) = domain.split('.')
	print('Email: ' + email)
	print('Username: ' + username)
	print('Domain: ' + domain)
	print('Extension: ' + extension)
	print('Thank you!' + '\n')

while True:
	main()

