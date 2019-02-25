#!/usr/bin/env python


# Define a function that uses python built-in exceptions.
# The file is on a windows PC, therefore the need for double backslashes ( \\ ) 


def readfile():
    
    try:
        with open('c:\\Users\\<your-username>\\Desktop\\test.txt') as f:
            thereadfile = f.read()
            print(thereadfile)
	
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print('Did you check your code?')

    else:
        try:
            with open('c:\\Users\\<your-username>\\Desktop\\DHT_project.txt') as f:
                readresult = f.read()
                print(readresult)

        except FileNotFoundError as fnf:
            print(fnf)
            print('This will always print, even if this exception is thrown.')

    finally:
        print('Using the finally clause will always print this statement at the end.')
