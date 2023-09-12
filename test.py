# a = {"a", "b" , "c"}
# b = {1, 2, 3}
# c = a.union(b)
# print(c)

# a = {1, "a", "b" , "c"}
# b = {1, 2, 3}b
# print(a.intersection(b))

# a = {"a", "b" , "c"}
# b = {1, 2, 3, "a", "b" , "c"}
# c = a.issubset(b)
# print(c)

# lista = [1, 2, 3]
# vazio = set(lista)
# vazio.discart(2)
# print(vazio)

# a = {"a", "b" , "c"}
# b = {1, 2, 3}
# c = a | b
# print(c)

# A = {1,2,3}
# potencias = {frozenset({x for x in A if (i & (1 << A.index(x))) != 0}) for i in range(1 << len(A))}
# print(potencias)

compras = ()

while True: 
    print('Menu Lindo')
    print('')
    print('1- Comprar')
    print('2- Remover do carrinho ')
    print('3- sair')
    print('')
    menu = int(input('Escolhe: '))
    match menu:
        case 1:
            while True:
                print('Menu compras')
                print('')
                print('1- Lista de compras')
                print('2- Comprar')
                print('3- Sair')
                print('')
                menu_compras = int(input('Escolhe: '))
                match menu_compras:
                    case 1:
                        print(compras)
                    case 2:
                        print('Produtos')
                        print('')
                        print('Leite')
                        print('Ovos')
                        print('Farinha')
                        print('')
                        produtos = input('Oque quer comprar? ')
                        if 
                    case 3:
                        break
                    case _:
                        print('')
                        print('Ta errado!')
                        print('')
        case 2:
            print('')
        case 3:
            break
        case _:
            print('')
            print('Ta errado!')
            print('')