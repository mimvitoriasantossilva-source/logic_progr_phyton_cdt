'''
                                🎂🍰 Como Fazer um Bolo Delicioso! 🎂🍰
Para fazer um bolo delicioso, é necessário seguir alguns passos. Primeiro, junte os ingredientes: farinha de trigo, açúcar,
ovos, leite, fermento em pó e manteiga. Em seguida, pré-aqueça o forno a 180°C e unte uma forma com manteiga para começarmos 
a fazer a massa. Para fazer a massa, será necessário pegar 2 ovos, quebrá-los num recipiente e misturá-los, pegar num pouco de 
farinha de trigo e leite para misturar tudo e fazer a sua massa. Com a massa feita, coloque-a no forno que aquecemos há 
algum tempo e deixe lá por 30 min para crescer, sem esquecer de verificar se o bolo está pronto antes! Quando o bolo estiver pronto,
retire-o do forno e deixe arrefecer por alguns minutos. Depois de arrefecer, você pode desenformar o bolo e decorá-lo com cobertura,
frutas ou confeitos da sua preferência. Agora você pode cortar o bolo em fatias e servir aos seus amigos e familiares, aproveitando
a deliciosa sobremesa que preparou com tanto carinho!
'''

def fazer_bolo(opcao_cobertura):

    print('\n--- PASSO A PASSO ---')
    print('1. Junte os ingredientes necessários: farinha, açúcar, ovos, leite, fermento e manteiga.')
    print('2. Pré-aqueça o forno a 180°C e unte uma forma com manteiga.')
    print('3. Quebre 2 ovos num recipiente e misture-os bem.')
    print('4. Adicione a farinha de trigo e o leite para misturar tudo e fazer a massa.')
    print('5. Coloque a massa no forno pré-aquecido e deixe cozer por 30 minutos.')
    print('6. Verifique se o bolo está pronto e retire-o do forno com cuidado.')
    print('7. Deixe o bolo arrefecer por alguns minutos antes de mexer.')
    print('8. Desenforme o bolo com cuidado para não o partir.')
    print('9. Decore o bolo com uma cobertura, frutas ou confeitos da sua preferência.')
    print('10. Corte em fatias e sirva aos seus amigos e familiares!')

    if opcao_cobertura == "1":
        resultado = 'O seu bolo está simples e fofinho, perfeito para acompanhar um café!'
    else:
        resultado = 'O seu bolo ganhou uma cobertura incrível e caprichada, pronto para uma festa!'

    return resultado



print("Como deseja finalizar o seu bolo delicioso?")
print("1 - Bolo simples (Sem cobertura / Tradicional)")
print("2 - Bolo recheado (Com muita cobertura e confeitos)")

opcao = input("Digite o número da opção (1 ou 2): ")

status_do_bolo = fazer_bolo(opcao)

print("\nResultado:")
print(status_do_bolo)
