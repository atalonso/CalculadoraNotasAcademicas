from helpers import alunos,calcula_media_total,atribuir_letra_nota,nota_media_classe

if __name__ == '__main__':

    for aluno, detalhes in alunos.items():
        print(f"\n {alunos[aluno]['nome']}")
        print('----------')
        media_total_aluno = round(calcula_media_total(alunos[aluno]),1)
        print(f"A média de notas do(a) {alunos[aluno]['nome']} é {media_total_aluno}")
        print(f"A nota final do aluno {alunos[aluno]['nome']} é {atribuir_letra_nota(media_total_aluno)}")
#Calcula a media da classe
    media_classe = nota_media_classe()
    print("----------")
    print(f"\nA media da turma toda é: {round(media_classe,1)}")
    print(f"A nota final da turma toda é: {atribuir_letra_nota(media_classe)}")
