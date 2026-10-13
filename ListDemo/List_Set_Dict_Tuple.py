myStr1 = "Hello Forward Deployment Engineer 12"
myStr2 = "12345"
print(myStr1.isalnum())  # Check if all characters in the string are alphanumeric --> False
print(myStr2.isalnum())  # Check if all characters in the string are alphanumeric --> True
print(myStr1.isdigit())  # Check if string contains digits --> False
print(myStr2.isdigit())  # Check if string contains digits --> True
print(myStr1.istitle())  # Check if string has title words --> True

print(myStr1.islower())  # Check if string is in lowercase --> False
print(myStr1.isupper())  # Check if string is in uppercase --> False

myStr3 ="FDE 1.0"
print(myStr3.islower())  # Check if string is in lowercase --> False
print(myStr3.isupper())  # Check if string is in uppercase --> True

myStr4 ="fde 1.0"
print(myStr4.islower())  # Check if string is in lowercase --> True
print(myStr4.isupper())  # Check if string is in uppercase --> False

print(myStr1.startswith("Hello F"))  # Check if string starts with a substring --> True
print(myStr1.endswith("r 12"))  # Check if string ends with a substring --> True

print(myStr1.isspace())  # Check if string contains only whitespace --> False
myStr5="    "
print(myStr5.isspace())  # Check if string contains only whitespace --> False

print("** List Demo ***")
lst:list = []
print(type(lst))
lst= ['Math', 'AI', 'Cloud', 'DevOps', 'Python', 3, 4.523]

print(lst[4]) ## --> Python
print(lst[3:6]) ## ->'DevOps', 'Python', 3
print(lst[:4]) ## --> 'Math', 'AI', 'Cloud', 'DevOps'
print(lst[-4]) ## --> Devops
print(lst[-5:-3]) ## --> 'Cloud', 'DevOps'

lst.append(True)
lst.insert(3,'AWS/Azure/GCP')
lst.insert(3, ['Regression', 'Classification', 'Clustering'])
print(lst)

lst.extend(['Kubernetes', 'Docker', 'Terraform'])
print(lst)

# sum(lst) <-- Will not work as the list contains non-numeric values

lst.pop(2)
print(lst)