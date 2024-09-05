arg2 =open("arquivos/arquivo2.txt","w")
arg2.write("Aprendendo a programar em Python.")
arg2.close()
arg2 = open("arquivos/arquivo2.txt","a")
arg2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado.")
arg2.close
arg2 = open("arquivos/arquivo2.txt","r")
print(arg2.read())