def linha():
   print("__"*20)

arg1 = open("arquivos/arquivo1.txt","r")

print(type(arg1))
linha()
print(arg1.read())
linha()
print(arg1.tell())
linha()
print(arg1.read())
linha()
print(arg1.seek(0,0))
print(arg1.read(32))
linha()
print(arg1.read())



