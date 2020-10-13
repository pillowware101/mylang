import basic
import sys
try:
	filetorun=sys.argv[1]
	basic.run("RUN", filetorun)
except IndexError:
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