from time import sleep
print('=' * 35)
print(f'{"BAR DBA": ^35}')
print('=' * 35)

# DECLARAÇÃO DE VARIAVEL
proximo_fila = respostaP_Acompanhante = ''
Idade = Idade_Acomp = 0
parar_loop = True
# DECLARAÇÃO DE VARIAVEL

while parar_loop:
        Idade = None
        Nome = str(input('Nome: '))
        Idade = int(input('Idade: '))
        sleep(1)
        if Idade >= 18:
            print(f'Olá {Nome}, seja bem vinda(o)') 
            print('=' * 35)
        elif Idade >= 16 and Idade < 18:
            print(f'Olá {Nome}, é necessário estar acompanhado por um adulto para poder entrar !')
            while True: 
                respostaP_Acompanhante = str(input('Deseja chamar algum adulto [S/N]: ')).lower()[0]

                if respostaP_Acompanhante == 's':  
                    Idade_Acomp = int(input('Idade do acompanhante: '))
                    respostaP_Acompanhante = None
                    if Idade_Acomp >= 18:
                        print(f'Olá {Nome}, o acesso a vocês foi liberado pois o ACOMPANHANTE É MAIOR DE IDADE')
                        print('=' * 35)
                        break    
                    else:
                        print('Vocês NÃO poderão entrar pois são menores de idade !')
                        print('=' * 35) 
                        break 

                elif respostaP_Acompanhante == 'n' :
                    print('Infelizmente você não poderá entrar sem um acompanhante')
                    respostaP_Acompanhante = None
                    print('=' * 35)
                    break    
                else:
                    print("Ops parece que você digitou uma opção inválida, tente novamente...")
        else:
            print('Parece que você tem menos 16 anos, volte para casa e vai jogar lol')
            print('=' * 35)        

        while True:
            Prox_Fila = str(input('Ainda há pessoas na fila [S/N]? ')).lower()[0]
            if Prox_Fila == 's':     
               print('=' * 35)          
               print(f'{"PRÓXIMO !": ^35}')
               break
            elif Prox_Fila == 'n':
                print('=' * 35)
                print(f'{"Encerrando o atendimento no BAR DBA !": ^35}')
                print('=' * 35)
                parar_loop = False
                break                    
            else:      
                print('Ops parece que você digitou uma opção inválida, tente novamente...')               