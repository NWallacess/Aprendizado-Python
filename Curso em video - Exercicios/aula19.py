pessoa={'nome':'gustavo', 'sexo':'M', 'idade':22 }
print(pessoa['nome'])
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos.')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
pessoa['nome']='leandro'
for k in pessoa.keys():
    print(k)