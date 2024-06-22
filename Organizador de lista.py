import time


# Função de organizar uma lista através de ordenação por flutuação
def bubble_sort(lista):
    for valores in range(len(lista) - 1, 0, -1):
        for i in range(valores):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


# Exibição da introdução ao usuário
print('Seja bem-vindo(a) ao organizador de lista!')
time.sleep(2)
print('A seguir você colocará quaisquer números, e em')
time.sleep(2)
print('seguida o programa organizará eles automáticamente!!')
time.sleep(2)

# Recepção dos valores da lista
pos = 1
lista = []
while True:
    v = int(input(f'Digite o {pos}º número: '))
    lista.append(v)
    pos += 1
    replay = input('Deseja adicionar outro número? (s/n) ').lower()
    while replay not in ['s', 'n']:
        print('Opção inválida.')
        replay = input('Deseja adicionar outro número? (s/n) ')
    if replay == 's':
        print('')
    else:
        print('')
        break

# Organização da lista
bubble_sort(lista)
# Retorno da lista organizada
print('Aqui está sua lista organizada:')
print(lista)
