x = input("give me a variable in camel case ").strip()
for i in x:
    if i.isupper():
        print("_"+i.lower(), end="")
    else:
        print(i, end="")
    
