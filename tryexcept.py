#!/usr/bin/env python


# Define a function that uses python built-in exceptions.
# The file text file is located on a Windows PC, therefore the need for double backslashes ( \\ ) 


def readfile():
	
    # The 'assert' statement is used for debugging code . The word 'ansible' will throw a built-in AssertionError.
    # The assert statement 'in'. We make a 'list' with string literal's for testing assert.
    # The assert statement results in an AssertionError and HALTS the program; it does not continue. 
    # Not a good approach if you want the program to continue!
	
    # The list	
    test_list = ['python', 'apple', 'linux', 'cisco']
    # The assert statement used to test if the string 'ansible' is in the test_list.
    assert( 'ansible' in test_list), 'Ansible is not in the list'
	
    # A try and except block: used to catch and handle exceptions.
    # The code block that follows the 'try' statement executes as normal.
    try:
        with open('c:\\Users\\<your-username>\\Desktop\\test.txt') as f:
            thereadfile = f.read()
            print(thereadfile)
		
		
    # The code block that follows the 'except' statement is the program's response.
    # Will execute this code when there is an exception.
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
