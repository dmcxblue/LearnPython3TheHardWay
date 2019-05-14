def reverse_function(x):
	return x[::-1]
txt_1 = input('Word1 > ')

txt_1 = reverse_function(txt_1)

txt_2 = input('Word2 > ')

if txt_1 == txt_2:
	print (True)
else:

	print (False)

