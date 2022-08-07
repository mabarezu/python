first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder.'

print(message)
print(msg)

#############################

course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course)

print(course.find('Beginners'))
print(course.replace('Beginners', 'absolut Beginners'))

print('Python' in course)
print('python' in course)