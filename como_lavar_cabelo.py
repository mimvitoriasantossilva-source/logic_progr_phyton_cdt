'''
Commo fritar um ovo;
Como fazer um bolo;
Como fritar batata frita;
Como trocar um pneu;
Como fazer um hamburguer;


COMO LAVAR O CABELO?    
Para lavar o cabelo, siga os seguintes passos:
A primeira coisa a fazer é molhar o cabelo com agua fria ou agua morna, depois que o cabelo estiver molhado,
aplique uma quantidade adequada de shampoo na palma da mão e espalhe no couro cabeludo do cabelo,
massageando suavemente com as pontas dos dedos, sem passar as unhas para não machucar o couro cabeludo, 
logo depois de um tepo massageando, enxague o cabelo com agua fria ou morna ate sair todo o produto do 
cabelo, se necessario repita o processo novamente, depois de enxauar o cabelo, de preferencia da pessoa,
apliqe uma mascara de tratamento no cabelo, massageando suavemente o couro cabeludo e espalhando a 
maascara por todo o cabelo, depois de deixar a mascara agir por alguns minutos, exague o cabelo
novamente, tirando todo o produto do cabelo, depois de enxaguar o cabelo, aplique um condicionador no cabelo,
massageando o couro cabeludo e espalhando o condicionador por todo o cabelo, depois de alguns minutos,
enxague o cabelo novamente, tirando todo o produto do cabelo, logo que enxaguar, com cuidado, retire o
excesso de agua do cabelo, apertando devagar com as maos ou com uma toalha, depois que retirar o excesso
de agua do cabelo, penteie o cabelo com um pente que nao quebre os fios do cabelo e pronto, cabelo linpo
e completamente cheiroso!
'''

def lavar_cabelo():
    print("Passos para lavar o cabelo: 🧴")
    print("1. Molhe o cabelo com água fria ou morna.")
    print("2. Aplique shampoo na palma da mão e massageie suavemente o couro cabeludo.")
    print("3. Enxágue o cabelo com água fria ou morna até remover todo o shampoo.")
    print("4. Se necessário, repita o processo.")
    print("5. Aplique uma máscara de tratamento e massageie suavemente.")
    print("6. Deixe a máscara agir por alguns minutos e enxágue novamente.")
    print("7. Aplique condicionador, massageie e deixe agir por alguns minutos.")
    print("8. Enxágue o cabelo novamente para remover todo o condicionador.")
    print("9. Retire o excesso de água do cabelo com cuidado.")
    print("10. Penteie o cabelo com um pente que não quebre os fios.")

    if lavar_cabelo() == 'shampoo':
        resultado = 'Pode passar o condicionador'
    else:
        resultado = 'Não pode passar o condicionador'

        return resultado
    
    meu_cabelo = lavar_cabelo(shampoo=True)
    print(f'Resultado: {meu_cabelo}')