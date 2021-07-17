def principal():
    lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho','julho', 'agosto', 'setembro',
             'outubro', 'novembro', 'dezembro']
    dia, mes, ano = input("Data no formato DD/MM/AAAA?").split('/')
    if int(dia) > 31:
        print(texto())
    elif int(mes) > 12:
        texto()
    elif int(dia) > 30 and (int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11):
        texto()
    else:
        if int(ano) % 4 == 0 and int(ano) % 100 != 0:
            bissexto(dia, mes, ano, lista)
        elif int(ano) % 100 == 0 and int(ano) % 400 == 0:
            bissexto(dia, mes, ano, lista)
        else:
            naoBissexto(dia, mes, ano, lista)
def naoBissexto(dia, mes, ano, lista):
    if int(dia) == 29 and int(mes) == 2:
        texto()
    else:
        a = int(mes) - 1
        print('Retorno da função')
        print('{} de {} de {}'. format(dia, lista[a], ano))
def bissexto(dia, mes, ano, lista):
    a = int(mes) - 1
    print('Retorno da função')
    print('{} de {} de {}'.format(dia, lista[a], ano))
def texto():
    return "Data inválida!"
principal()
