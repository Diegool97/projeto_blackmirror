# DESENVOLVA UM PROGRAMA QUE O

# USUÁRIO IRÁ INFORMAR UMA
# PERGUNTA (UTILIZANDO

# EXATAMENTE AS PERGUNTAS NDO
# QUESTIONÁRIO ANTERIOR) E O
# SISTEMA DEVERÁ DAR A RESPOSTA.

pergunta =''' 
=========================================================================================================
                 ESCOLHA UMA DAS PERGUNTAS DA SÉRIE PARA SABER A RESPOSTA:
 
        [1] QUAL É O NOME COMPLETO DA PROTAGONISTA DO EPISÓDIO? 

        [2] QUEM DIRIGE A VIDA DE JOAN EM TEMPO REAL PARA UMA SÉRIE DE TELEVISÃO? 

        [3] QUAL É O NOME DO SERVIÇO DE STREAMING FICTÍCIO QUE PARODIA A NETFLIX NO EPISÓDIO? 

        [4] COMO JOAN DESCOBRE A EXISTÊNCIA DA SÉRIE SOBRE SUA VIDA? 

        [5] QUAL É A REAÇÃO INICIAL DE JOAN AO DESCOBRIR A SÉRIE E O QUE ELA FAZ EM RESPOSTA? 

        [6] QUAIS SÃO OS TEMAS PRINCIPAIS EXPLORADOS NESTE EPISÓDIO DE BLACK MIRROR? 

        [7] O EPISÓDIO TERMINA DE MANEIRA TÍPICA PARA A SÉRIE BLACK MIRROR? EXPLIQUE.        
                 
  INFORME A OPÇÃO ESCOLHIDA: 
'''


while True:
     opcaoEscolhida = input(pergunta)   
     if opcaoEscolhida == "1":
         print("O nome da protagonista é Joan")
     elif opcaoEscolhida == "2": 
         print("Moana é quem dirige a vida de Joan")
     elif opcaoEscolhida == "3": 
         print("Streamberry é o serviço de streaming")
     elif opcaoEscolhida == "4": 
         print("Joan descobre no sofá de casa")
     elif opcaoEscolhida == "5": 
         print("Uma sensação de Desespero")
     elif opcaoEscolhida == "6": 
         print("Traição, trabalho e emoção são os temas explorados")
     elif opcaoEscolhida == "7": 
         print("Não")
         break
     else:
         print("OPÇÃO INVÁLIDA") 