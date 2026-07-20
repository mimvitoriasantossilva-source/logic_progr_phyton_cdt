'''
Arqquivo do tipo
txt -> arquivo em bloco de notas, texto simples;
csv -> arquivo em excel e google planihas(bloco de notas), texto simples, separado po virgula;
json -> arquivo em formato de dicionário, testo simples, separado por virgula;
'''

arquivo_read = open('arquivo_leitura.txt', 'r', encoding='utf-8')

conteudo_arquivo = arquivo_read.readline()

linhas = arquivo_read.readlines()

print(linhas[4].strip()) 
print(linhas[6].strip())

print(conteudo_arquivo)

arquivo_read.close