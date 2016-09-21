name = "rizwan"
age = 25

str1 = "I am {}, i am {} years old".format(name, age)
print str1

str2 = "I am {name}, i am {age} years old".format(name='rizwan', age=27)
print str2

data = {'name': 'rizwan', 'age': 27}

str3 = "I am {name}, i am {age} years old".format(**data)
str4 = "I am %(name)s, i am %(age)d years old" % data

print str3

link_dict = {'name': 'google', 'url': 'http://www.google.com'}
link_template = "<a href='{name}'>{url}</a>"
print link_template.format(**link_dict)