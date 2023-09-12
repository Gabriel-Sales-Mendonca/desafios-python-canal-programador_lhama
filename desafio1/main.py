from elevador import Elevador

contador = 1
pessoa = {'contador': '1'}

while True:
    pessoa['contador'] = Elevador()
    andar_da_pessoa = int(input('Para chamar o elevador você precisa informar em qual andar você está, em qual andar você está ? '))
    pessoa['contador'].chamar_elevador(andar_da_pessoa)
    contador += 1
    pessoa['contador'] = contador

    while True:
        sair = int(input('Para sair do programa digite 1, para continuar digite 2: '))
        if sair == 1 or sair == 2:
            break
    if sair == 1:
        break
    else:
        continue