num=input('Digite seu nome: ').strip()
separacao=num.split()
ultimonome=len(separacao)-1
print('Muito prazer te conhecer!\nSeu primeiro nome: {}'.format(separacao[0]))
print('Seu ultimo nome: {}'.format(separacao[ultimonome]))