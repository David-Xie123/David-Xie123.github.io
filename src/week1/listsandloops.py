# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "David",  
               "LastName": "Xie",  
               "DOB": "October 8",  
               "Residence": "San Diego",  
               "Email": "david.l.xie@gmail.com",  
               "Family_Members":["David Xie","Rui Zhang","Jianjun Xie","April Xie", "Joann Xie"]  
              })  

InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Mortensen",  
               "DOB": "October 21",  
               "Residence": "San Diego",  
               "Email": "jmortensen@powayusd.com",  
               "Family_Members":["A","B","C"]  
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Family: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Family_Members"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
## hack 2b: def while_loop(0)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
## hack 2c : def recursive_loop(0)
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester1():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester2():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling for invalid input
def recur_fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibonacci(n-1) + recur_fibonacci(n-2))  
# take input from the user  
nterms = int(input("Enter a number for a Fibonacci sequence: "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("The Fibonacci sequence for that number does not exist")  
else:  
   print("The Fibonacci sequence for that number is")  
   for i in range(nterms):  
       print(recur_fibonacci(i))
