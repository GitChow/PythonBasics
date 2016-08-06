# function

## define a function 
```python
# define a function
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]

# example
def printme( str ):
   "This prints a passed string into this function"
   print str
   return
```

## call a function
```python
# the normal way
printme("calling the function")

# keyword argument
def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

printinfo( age=50, name="miki" )

# default argument
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

printinfo( age=50, name="miki" )
printinfo( name="miki" )

# Variable-length arguments
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

printinfo( 70)
#result: 70
printinfo( 70, 60, 50 )
#result: 70, 60,50
```

## the return
```python
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print "Inside the function : ", total
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total 
```