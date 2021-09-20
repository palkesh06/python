string = "hello world "
string = '''I am learning python''' # multiline string 
print ( string [1:5]) # slicing 
del string
String1 = "{} {} {}".format('This', 'is', 'python')
print("Print String in default order: ")
print(String1)
 
# Positional Formatting
String1 = "{1} {0} {2}".format('This ', 'is', 'python')
print("\nPrint String in Positional order: ")
print(String1)
 
# Keyword Formatting
String1 = "{l} {f} {g}".format(g = 'This', f = 'is', l = 'python')
print("\nPrint String in order of Keywords: ")
print(String1)
def reverse(String1):
    string1 = "".join(reversed(String1))
    print(string1) 
del String1