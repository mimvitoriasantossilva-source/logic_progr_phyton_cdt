'''
                         🍟🍟🍟fazer uma batata frita deliciosa!🍟🍟🍟
Para fazer uma batata frita deliciosa, é necessário seguir alguns passos. Primeiro, junte os ingredientes: batatas, óleo para fritar
sal e uma frigideira, fritadeira ou airfryer. Em seguida, descasque as batatas e corte-as em palitos ou rodelas, dependendo da sua 
preferência. Depois, aqueça o óleo em uma frigideira ou fritadeira a uma temperatura média-alta. Em seguida, coloque as batatas 
cortadas no óleo quente e frite-as até que fiquem douradas e crocantes, mexendo ocasionalmente para garantir que cozinhem de maneira
uniforme. Depois de fritar, retire as batatas do óleo e coloque-as em um prato forrado com papel toalha para absorver o excesso de óleo.
Em seguda, tempere as batatas fritas com sal a gosto e, se desejar, adicione outros temperos ou ervas para dar mais sabor, ou adicionar
outro complemento como queijo cheddar, bacon ou molho de sua preferência. Agora você pode servir as batatas fritas como acompanhamento
de um lanche, prato principal ou petisco, aproveitando a deliciosa batata frita crocante e saborosa que preparou com tanto carinho!
'''
def fazer_batata(opcao_adicional):

    print('\n--- PASSO A PASSO ---')
    print('1. Junte os ingredientes necessários: batatas, óleo para fritar, sal e os utensílios.')
    print('2. Descasque as batatas e corte-as em palitos ou rodelas.')
    print('3. Aqueça o óleo em uma frigideira ou fritadeira a uma temperatura média-alta.')
    print('4. Coloque as batatas cortadas no óleo quente para fritar.')
    print('5. Frite até que fiquem douradas e crocantes, mexendo ocasionalmente.')
    print('6. Retire as batatas do óleo com cuidado.')
    print('7. Coloque-as em um prato forrado com papel toalha para absorver o excesso de óleo.')
    print('8. Tempere as batatas fritas com sal a gosto.')
    print('9. Se desejar, adicione outros temperos, ervas, queijo cheddar ou bacon.')
    print('10. Sirva como acompanhamento ou petisco e aproveite sua batata crocante!')


    if opcao_adicional == "1":
        resultado = 'Suas batatas fritas estão tradicionais, bem crocantes e prontas para comer!'
    else:
        resultado = 'Suas batatas ganharam um upgrade com cheddar e bacon, prontas para comer!'

    return resultado



print("Como você prefere finalizar a sua batata frita?")
print("1 - Apenas com sal (Tradicional)")
print("2 - Com adicionais (Cheddar, bacon ou molhos)")

opcao = input("Digite o número da opção (1 ou 2): ")

status_da_batata = fazer_batata(opcao)

print("\nResultado:")