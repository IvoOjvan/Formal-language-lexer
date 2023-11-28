import main

text = input("basic > ")
result, separators, identificators, operators, comments = main.run(text)

for res in result:
    print(res)

ident = "".join("'{}'[{}], ".format(k,v) for k,v in identificators.items())
print(f"identifikatori [{len(identificators)}]: " + ident)

oper = "".join("'{}'[{}], ".format(k,v) for k,v in operators.items())
print(f"operatori [{len(operators)}]: " + oper)

com = "".join("'{}'[{}], ".format(k,v) for k,v in comments.items())
print(f"komentari [{len(comments)}]: " + com)

sep = "".join("'{}'[{}], ".format(k,v) for k,v in separators.items())
print(f"separatori [{len(separators)}]: " + sep)


