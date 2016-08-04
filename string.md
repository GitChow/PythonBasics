# string
## string
> refer http://www.tutorialspoint.com/python/python_strings.htm

> python treats '' the same as ""

```python
# create string
varString='hello world'

# access string
varSubString=varString[0]
varSubString=varString[1:5]

# update string
print varString[:6] + 'Python'  #hello Python

# escape characters
\b #backspace
\n #newline
\s #space

# string special characters
# refer to http://www.tutorialspoint.com/python/python_strings.htm
+   #concat
*   #repetition
[]  #slice
[:] #range slice
in / not in #membership
%   #format

# string format
print "My name is %s and weight is %d kg!" % ('Zara', 21)

# triple quotes
textBlock="""
this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show u
"""
```