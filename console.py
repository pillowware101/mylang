import basic

if __name__ == '__main__':
    while True:
	    text=input("basic> ")
	    result, error=basic.run('<stdin>', text)

	    if error: 
		    '''
		    try:
		    	exec(text)
		    except:
		    	'''
		    print(error.as_string())
	    elif result: print(result)
