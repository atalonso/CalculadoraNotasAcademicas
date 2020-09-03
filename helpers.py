alunos = {
        'jeffersons':
            {'nome': 'Jefferson Santos',
             'trabalhos': [90, 95, 80, 100],
             'provas': [90, 80],
             'laboratorio': [70, 85.2],
             },
        'pedrop':
            {'nome': 'Pedro Pinheiro',
             'trabalhos': [50, 75, 70,95],
             'provas': [90, 80],
             'laboratorio': [50,55.2],
             },
        'brunop':
            {'nome': 'Bruno Pinheiro',
             'trabalhos': [60, 45, 70, 90],
             'provas': [90, 50],
             'laboratorio': [50, 55.2],
             },
        'adrianoa':
            {'nome': 'Adriano Alonso',
             'trabalhos': [88, 95, 79, 94],
             'provas': [90, 70],
             'laboratorio': [60, 75.2],
             },
}
def obter_media(notas):
    """
    Função que obtem as medias das notas dos alunos
    :param notas:
    :return: retorna a media das notas
    """
    total_soma = sum(notas)
    total_soma = float(total_soma)
    return total_soma / len(notas) #len nesse caso para pegar a quantidade de notas da lista para fazer a media

def calcula_media_total(aluno):
    """
    Função que calcula a media das notas do aluno
    :param aluno:
    :return: retorna a media dos notas do aluno
    """
    trabalhos = obter_media(aluno['trabalhos'])
    provas = obter_media(aluno['provas'])
    laboratorio = obter_media(aluno['laboratorio'])
    return (0.25*trabalhos + 0.55*provas + 0.20*laboratorio)

def atribuir_letra_nota(nota_final_aluno):
    """
    Função que converte a nota (numero) em letra
    :param nota_final_aluno: 
    :return: Retorna a nota do aluno em forma de letra
    """
    if nota_final_aluno >= 90:
        return "A"
    elif nota_final_aluno >= 80:
        return "B"
    elif nota_final_aluno >= 70:
        return "C"
    elif nota_final_aluno >= 60:
        return "D"
    else:
        return "F"

def nota_media_classe():
    """
    Função que retorna a media geral da turma
    :return: Retorna a media final da turma
    """
    resultado_lista = []
    for aluno, detalhes in alunos.items():
        media_aluno = calcula_media_total(alunos[aluno])
        resultado_lista.append(media_aluno)

        return obter_media(resultado_lista)
