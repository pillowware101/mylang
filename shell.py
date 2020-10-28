import basic
import sys

if len(sys.argv)>1:
	fn=sys.argv[1]
	result, error=basic.run('<stdin>', f'RUN("{fn}")')
	if error: print(error.as_string())
	elif result: print(result)
	sys.exit()

while True:
	text=input("basic> ")
	result, error=basic.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)