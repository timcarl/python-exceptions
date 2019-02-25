#!/usr/bin/env python


# Define a function that uses python built-in exceptions.
# The file is on a windows PC, therefore the need for double backslashes ( \\ ) 


def readfile():
    
    try:
        with open('c:\\Users\\tcdig\\Desktop\\test.txt') as f:
            thereadfile = f.read()
            print(thereadfile)
	
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print('Good job Tim')

    else:
        try:
            with open('c:\\Users\\tcdig\\Desktop\\DHT_project.txt') as f:
                readresult = f.read()
                print(readresult)

        except FileNotFoundError as fnf:
            print(fnf)
            print('all done here')

    finally:
        print('cleaning up the job')
