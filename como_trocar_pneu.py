'''
                  🚗🔧🔩 Como trocar um pneu com segurança! 🔩🔧🚗
Para trocar um pneu com segurança, é necessário seguir alguns passos fundamentais. Primeiro, estacione o veículo em um local plano e seguro,
ligue o pisca-alerta e puxe o freio de mão. Em seguida, pegue as ferramentas necessárias no porta-malas: o estepe, o macaco e a chave de roda.
Depois, use a chave de roda para afrouxar as porcas do pneu furado levemente, mas sem retirá-las ainda. Em seguida, posicione o macaco no local
correto do chassi do carro e levante o veículo até que o pneu saia do chão. Agora sim, remova completamente as porcas e retire o pneu furado.
Depois, encaixe o pneu estepe no lugar e rosqueie as porcas com as mãos até encostar. Em seguida, desça o carro com o macaco com cuidado até
que o pneu toque o chão e retire o macaco. Por fim, use a chave de roda para dar o aperto final e firme nas porcas. Guarde o pneu furado e
as ferramentas no porta-malas, e seu carro estará pronto para seguir viagem com total segurança e tranquilidade!
'''

def trocar_pneu(opcao_ajuda):

    print('\n--- PASSO A PASSO ---')
    print('1. Estacione em local plano, ligue o pisca-alerta e puxe o freio de mão.')
    print('2. Pegue as ferramentas necessárias no porta-malas: estepe, macaco e chave de roda.')
    print('3. Use a chave de roda para afrouxar as porcas levemente, sem retirá-las.')
    print('4. Posicione o macaco no local correto sob o chassi do carro.')
    print('5. Levante o veículo com o macaco até que o pneu furado saia do chão.')
    print('6. Remova completamente as porcas soltas e retire o pneu furado.')
    print('7. Encaixe o pneu estepe no eixo e rosqueie as porcas com as mãos.')
    print('8. Desça o carro com o macaco cuidadosamente até o pneu tocar o chão e remova o macaco.')
    print('9. Use a chave de roda para dar o aperto final e firme em todas as porcas.')
    print('10. Guarde o pneu furado e as ferramentas no porta-malas para finalizar.')


    if opcao_ajuda == "1":
        resultado = 'Você trocou o pneu sozinho com maestria! Seu carro está pronto para rodar com segurança!'
    else:
        resultado = 'Você trocou o pneu com a ajuda de alguém e foi super rápido! Seu carro está pronto para rodar!'

    return resultado


print("Você vai realizar a troca do pneu sozinho ou tem alguém para ajudar?")
print("1 - Vou trocar sozinho")
print("2 - Tenho companhia para ajudar")

opcao = input("Digite o número da opção (1 ou 2): ")

status_do_carro = trocar_pneu(opcao)

print("\nResultado:")
print(status_do_carro)