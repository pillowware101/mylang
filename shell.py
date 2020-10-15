import basic
import sys

def shell():
	while True:
		text = input('basic > ')
		if text.strip() == "": continue
		result, error = basic.run('<stdin>', text)

		if error:
			print(error.as_string())
		elif result:
			if len(result.elements) == 1:
				print(repr(result.elements[0]))
			else:
				print(repr(result))


try:
	basic.run('<stdin>', 'RUN("%s")'%sys.argv[1])
except FileNotFoundError:
	print('\n no such file... \n')
	print('moving on to interactive shell\n')
	shell()
except IndexError:
	shell()