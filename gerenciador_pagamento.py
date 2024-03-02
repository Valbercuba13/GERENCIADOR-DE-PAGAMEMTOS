import os
from time import sleep

def clear_terminal():
    # Verifica o sistema operacional para usar o comando de limpeza apropriado
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_terminal()
        print('{:=^40}'.format(' CUBATECH 2024 PAYMENT SYSTEM  '))
        preço = float(input('Preço das compras: R$'))

        print(''' FORMAS DE PAGAMENTO 
        [ 1 ] à vista dinheiro/pix 
        [ 2 ] à vista no cartão debito ou credito
        [ 3 ] 2x no cartão credito
        [ 4 ] 3x ou mais no cartão de credito  ''')

        opção = int(input('Qual é a opção ?'))

        if opção == 1:
            total = preço - (preço * 10 / 100)
        elif opção == 2:
            total = preço - (preço * 5 / 100)
        elif opção == 3:
            total = preço
            parcela = total / 2
            print('A compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
        elif opção == 4:
            total = preço + (preço * 20 / 100)
            totalParcela = int(input('Qual a quantidade de parcelas ?'))
            parcela = total / totalParcela
            print('A compra será parcelada em {}x de R${:.2f} COM JUROS '.format(totalParcela, parcela))
        else:
            print('OPÇÃO INVÁLIDA TENTE NOVAMENTE OU ACIONE O SUPORTE TÉCNICO CUBATECH NO WTS (14)996503034')
            print('RECOMEÇANDO...')
            sleep(3)
            continue

        print('A compra de R${:.2f} vai custar R${:.2f} '.format(preço, total))

        reiniciar = input('Digite R para recomeçar ou X para concluir e sair: ')
        if reiniciar.upper() != 'R':
            break

if __name__ == "__main__":
    main()
