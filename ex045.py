print('\033[1;30;107mPedra,Papel,Tesoura!\033[m')
from random import randint
from time import sleep
print('''\033[97;40mSuas Opções:\033[m
\033[97;40m[ 1 ] \033[37mPEDRA\033[m
\033[97;40m[ 2 ] \033[97mPAPEL\033[m
\033[97;40m[ 3 ] \033[35mTESOURA\033[m''')
j = int(input('\033[34;40mQual Você Escolhe?\033[m '))
c = randint(1,3)
i = ('0', '\033[37mPEDRA' , '\033[97mPAPEL', '\033[35mTESOURA')
print('\033[36mJo')
sleep(1)
print('\033[35mKen')
sleep(1)
print('\033[32mPo!!!')
sleep(1)
print("\033[97m-="*30)
print(f'\033[31mO Computador Escolheu\033[m {i[c]}')
print(f'\033[34mO Jogador Escolheu\033[m {i[j]}')
print('\033[30m-='*30)
if j == c:
    print('\033[97mEmpate!')
elif (j== 1 and c== 2) or (j==2 and c==3) or (j==3 and c==1):
    print('\033[31mO Computador Venceu!')
elif (j== 1 and c==3) or (j==2 and c==1) or (j==3 and c==2):
    print('\033[34mO Jogador Venceu!')
else:
    print('JOGADA INVÁLIDA!')
