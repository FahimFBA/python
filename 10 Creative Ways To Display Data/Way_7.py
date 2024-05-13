# string.Template

# from string import Template
# custom_name = "Eve"
# custom_age = 50
# template = Template("Name: $name, Age: $age")
# result = template.substitute(name = custom_name, age = custom_age)
# print(result)

from string import Template as TP
custom_name = "Eve"
custom_age = 50
template = TP("Name: $name, Age: $age")
result = template.substitute(name = custom_name, age = custom_age)
print(result)