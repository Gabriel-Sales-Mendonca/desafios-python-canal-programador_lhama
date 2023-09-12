from time import sleep

class Elevador:

    def __init__(self):
        self.andar_atual = 1

    def chamar_elevador(self, andar_da_pessoa):
        self.andar_da_pessoa = andar_da_pessoa
        if self.andar_da_pessoa != self.andar_atual:
            print(f'Elevador indo para o {self.andar_da_pessoa}º andar')
        self.__abrir_e_fechar_porta()
        self.ir_para()
        print('-'*30)

    def ir_para(self):
        self.novo_andar = int(input('Digite o novo andar: '))
        print(f'Elevador indo para o {self.novo_andar}º andar...')
        self.__abrir_e_fechar_porta()
        self.andar_atual = self.novo_andar

    def __abrir_e_fechar_porta(self):
        sleep(2)
        print(f'Abrindo a porta do elevador...')
        sleep(2)
        print(f'Fechando a porta do elevador...')
        sleep(2)
