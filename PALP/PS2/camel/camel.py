import re
def camel():
    string = input("Write something in camelCase: ")
    res = re.split(r'(?=[A-Z])', string)
    res = ' '.join(filter(None,res))
    new_str = res.lower().replace(" ", "_")
    print(new_str)

camel()
