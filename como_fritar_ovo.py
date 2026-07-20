'''
                      🍳🥚 Como fritar um ovo delicioso!🍳🥚
Para fritar um ovo delicioso, é necessário seguir alguns passos. Primeiro, junte os ingredientes: ovos, óleo ou manteiga,
sal e pimenta, e uma frigideira. Em seguida, aqueça a frigideira em fogo médio e adicione um pouco de óleo ou manteiga
para esquentar. Depois, quebre o ovo com cuidado e coloque-o na frigideira, evitando quebrar a gema. Deixe o ovo fritar
por alguns minutos, dependendo de como você gosta da gema (mais mole ou mais dura). Em seguida, tempere com sal e pimenta
a gosto e, se desejar, adicione outros temperos ou ervas para dar mais sabor. Quando o ovo estiver frito ao seu gosto,
use uma espátula para retirá-lo da frigideira e coloque-o em um prato. Agora você pode servir o ovo frito como desejar,
caso queira colocar um acompanhamento, como torradas, bacon ou legumes. Aproveite o seu ovo frito delicioso e saboroso!
'''

def fritar_ovo(opcao_gema):
    
    print('\n--- PASSO A PASSO ---')
    print('1. Junte os ingredientes necessários: ovos, óleo ou manteiga, sal, pimenta e uma frigideira.')
    print('2. Aqueça a frigideira em fogo médio.')
    print('3. Adicione um pouco de óleo ou manteiga para esquentar.')
    print('4. Quebre o ovo com cuidado e coloque-o na frigideira, evitando quebrar a gema.')
    print('5. Deixe o ovo fritar por alguns minutos, monitorando o ponto da gema.')
    print('6. Tempere com sal e pimenta a gosto.')
    print('7. Se desejar, adicione outros temperos ou ervas para dar mais sabor.')
    print('8. Quando o ovo estiver frito ao seu gosto, use uma espátula para retirá-lo da frigideira.')
    print('9. Coloque o ovo frito em um prato.')
    print('10. Sirva com o acompanhamento que preferir (torradas, bacon ou legumes) e aproveite!')


    if opcao_gema == "1":
        resultado = 'Sua gema está mole e perfeita para chuchar um pãozinho, pronta para comer!'
    else:
        resultado = 'Sua gema está durinha e firme, pronta para comer!'

    return resultado


print("Como você prefere o ponto da gema do seu ovo?")
print("1 - Gema mole")
print("2 - Gema dura")

opcao = input("Digite o número da opção (1 ou 2): ")

status_do_ovo = fritar_ovo(opcao)

print("\nResultado:")
print(status_do_ovo)