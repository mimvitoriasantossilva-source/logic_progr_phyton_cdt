'''
🍔🍟🥤 Como fazer um hambúrguer artesanal delicioso!🍔🍟🥤

COMO FAZER UM HAMBURGUER: Para fazer um hamburguer é necessário seguir alguns
COMO FAZER UM HAMBÚRGUER: Para fazer um hambúrguer é necessário seguir alguns
passos. Primeiro, junte seus ingredientes: carne moída, sal, pimenta e pão de 
hamburguer, salada, queiijo e molho. Em seguida, molde a carne moída em m formato
de bola e tempere com sal e pimenta a gosto. Depois, prepare seu pão de hamburguer,
hambúrguer, salada, queijo e molho. Em seguida, molde a carne moída em formato
de bola e tempere com sal e pimenta a gosto. Depois, prepare seu pão de hambúrguer,
cortando ele e colocando manteiga na parte interna. Em seguida, esquente uma frigideira
e coloque o pão para tostar na manteiga. Depois de tostado você deve colocar a carne moída que você 
moldou em bolinhas na frigideira, amasse a bolinha fazendo um formato de hamburguer e 
moldou em bolinhas na frigideira, amasse a bolinha fazendo um formato de hambúrguer e 
deixe fritar por alguns minutos de cada lado, em seguida adicione uma fatia de queijo 
em cima de cada hamburguer e deixe-a derreter esperando alguns minutos. Depois de derretido,
retire o hamburguer da frigideira e coloque-o no pão tostado para fazer o seu lanche,
pegue uma salada para complementar e deixe seu lanche um pouco mais saudavel!
para montar seu lanche você ira usar o seu pão tostado aberto, adicionar a sua carne com
em cima de cada hambúrguer e deixe-a derreter esperando alguns minutos. Depois de derretido,
retire o hambúrguer da frigideira e coloque-o no pão tostado para fazer o seu lanche,
pegue uma salada para complementar e deixe seu lanche um pouco mais saudável!
Para montar seu lanche você irá usar o seu pão tostado aberto, adicionar a sua carne com
queijo derretido, colocar uma maionese ou outro molho de sua preferência, adicionar a salada
e colocar algum adicional que você queira, como bacon, ovo frito ou outro ingrediente de sua
preferência. Depois de adicionar todos os ingredientes, feche o pão e seu hamburguer estará pronto,
preferência. Depois de adicionar todos os ingredientes, feche o pão e seu hambúrguer estará pronto,
agora pegue uma bebida para acompanhar seu lanche, um prato de entrada como batata frita e 
aproveite seu lanche delicioso artesanal!
No maximo 10 print!
'''

def fazer_hamburguer(ponto_da_carne):
    print('🍔 Como fazer um hamburguer - Artesanal')
    print('1.Pegue seu pão e uma frigideira e sele ele com manteiga')
    print('2.Fazer uma bolinha de carne moida temperado com sal e pimenta')
    print('3.Fritar sua carne da hamburguer no ponto que você deseja')
    print('4.Adicione uma fatia de queijo por cima da sua carne para derrete-la')
    print('5.Corte um pedaço de salada, tomate e repolho')
    print('6.Monte seu lanche com o seu pão dourado, sua carne com queijo derretido')
    print('7.Coloque sua salada e seus molhos a gosto para terminar de montar seu lanche')
    print('8.Terminar de montar seu lanche para poder come-lo')
    print('9.Pegue algum acompanhamento como refri, batatas e etc')
    print('10.Comer seu hamburguer delicioso!')


    if ponto_da_carne() == 'tempo de 15min' :
        resultado = 'Carne mal passaada se for 15min ou menos'
    print('1. Pegue seu pão e uma frigideira e sele ele com manteiga')
    print('2. Fazer uma bolinha de carne moída temperada com sal e pimenta')
    print('3. Fritar sua carne de hambúrguer no ponto que você deseja')
    print('4. Adicione uma fatia de queijo por cima da sua carne para derretê-la')
    print('5. Corte um pedaço de salada, tomate e repolho')
    print('6. Monte seu lanche com o seu pão dourado, sua carne com queijo derretido')
    print('7. Coloque sua salada e seus molhos a gosto para terminar de montar seu lanche')
    print('8. Terminar de montar seu lanche para poder comê-lo')
    print('9. Pegue algum acompanhamento como refri, batatas e etc')
    print('10. Comer seu hambúrguer delicioso!')


    if ponto_da_carne <= 15:
        resultado = 'Sua carne está mal passada, pronta para comer!'
    else:
        resultado = 'Carne tostada no com alguns queiados se for 15min ou mais'
        resultado = 'Sua carne está bem passada e tostada, pronta para comer!'

    return resultado


print("Escolha uma opção de tempo para fritar a carne:")
print("1 - Menos tempo (15 minutos ou menos)")
print("2 - Mais tempo (Mais de 15 minutos)")

opcao = input("Digite o número da opção (1 ou 2): ")

if opcao == "1":
    minutos = 15  
else:
    minutos = 16  

status_da_carne = fazer_hamburguer(minutos)

print("\nResultado:")
print(status_da_carne)