'''
javascript object notation (JSON) é um formato livre de troca de dados, facil para humanos lerem
e escreverem, é facil para maquinas analisarem e gerarem.
'''


import json

with open('arquivo_leitura_em_json_yasmimvssilva.json', 'r') as arquivo:
    dados_arquivo = json.load(arquivo)

dados_formatados = []


for item in dados_arquivo:
    aluno_formatado = {
        "Nome completo": item.get("nome") or item.get("Nome completo"),
        "Idade": item.get("Idade"),
        "CEP": item.get("cep") or item.get("CEP"),
        "ResgMatr": item.get("RestMatr") or item.get("ResdMatr"),
        "E-Mail": item.get("email") or item.get("E-Mail")
    }
    dados_formatados.append(aluno_formatado)


with open('Alunos_indicadores.json', 'w', encoding='utf-8') as novo_arquivo:
    json.dump(dados_formatados, novo_arquivo, ensure_ascii=False, indent=2)

print("Novo arquivo 'alunos_indicadores.json' criado com sucesso!")