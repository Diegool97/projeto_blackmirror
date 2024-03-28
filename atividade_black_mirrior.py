# DESENVOLVA UM PROGRAMA QUE O

# USUÁRIO IRÁ INFORMAR UMA
# PERGUNTA (UTILIZANDO

# EXATAMENTE AS PERGUNTAS NDO
# QUESTIONÁRIO ANTERIOR) E O
# SISTEMA DEVERÁ DAR A RESPOSTA.

pergunta1 = "[1] QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO?"
pergunta2 = "[2] QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO?"
pergunta3 = "[3] QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO?"
pergunta4 = "[4] COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA?"
pergunta5 = "[5] QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA?"
pergunta6 = "[6] QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR?"
pergunta7 = "[7] O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE."

pergunta =f''' 
=========================================================================================================
                 ESCOLHA UMA DAS PERGUNTAS DA SÉRIE PARA SABER A RESPOSTA:
 
        {pergunta1}

        {pergunta2}

        {pergunta3}

        {pergunta4}

        {pergunta5}

        {pergunta6}

        {pergunta7}
                 
  INFORME A OPÇÃO ESCOLHIDA: 
'''
voltar = "Deseja realizar uma nova pergunta? (S/N)"

while True:
     opcaoEscolhida = input(pergunta)   
     if opcaoEscolhida == "1":
         print(f"{pergunta1} O nome da protagonista é Joan")
     elif opcaoEscolhida == "2": 
         print(f"{pergunta2} Moana é quem dirige a vida de Joan")
     elif opcaoEscolhida == "3": 
         print(f"{pergunta3} Streamberry é o serviço de streaming")
     elif opcaoEscolhida == "4": 
         print(f"{pergunta4} Joan descobre no sofá de casa")
     elif opcaoEscolhida == "5": 
         print(f"{pergunta5} Uma sensação de Desespero")
     elif opcaoEscolhida == "6": 
         print(f"{pergunta6} Traição, trabalho e emoção são os temas explorados")
     elif opcaoEscolhida == "7": 
         print(f"{pergunta7} Não")
         break
     else:
         print("OPÇÃO INVÁLIDA") 