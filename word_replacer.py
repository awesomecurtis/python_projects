def word_replacer():
	text = 'This is the text for the man. He is here for'
	print(text)
	word = input('Word to replace? ')
	replacement = input('Replacement word? ')
	print(text.replace(word, replacement))

word_replacer()
