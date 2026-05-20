#RESPOSTAS DA ATIVIDADE 4:

#PERGUNTA 1:

# Solicita o nome do usuário
nome_usuario = input("Digite o seu nome: ")

# Cria o arquivo chamado 'usuarios.txt' e abre no modo de escrita ('w'), o 'encoding="utf-8"' é para que os acentos e caracteres especiais sejam salvos corretamente
with open("usuarios.txt", "w", encoding="utf-8") as arquivo:

    # Salva o nome digitado dentro do arquivo
    arquivo.write(nome_usuario)
arquivo.close()

#PERGUNTA 2:
# Permite que o usuário digite
mensagem = input("Digite a mensagem para o chatbot: ")


# Cria ou abre o arquivo 'chatbot.txt' no modo de escrita ('w')
with open("chatbot.txt", "w", encoding="utf-8") as arquivo:

    # Salva a mensagem que foi digitada pelo usuário dentro do arquivo
    arquivo.write(mensagem)
arquivo.close()

#PERGUNTA 3:
# Pede para o usuário digitar suas notas
nota1 = input("Digite a 1° nota: ")
nota2 = input("Digite a 2° nota: ")


# Cria o arquivo 'notas.txt' no modo de escrita ('w')
with open("notas.txt", "w", encoding="utf-8") as arquivo:

    # Salva as notas no arquivo
   # Usamos o 'f' antes das aspas (f-string) para misturar texto com as variáveis de forma fácil
    # O 'f' serve para mostrar mostrar números e texto na mesma saída
    arquivo.write(f" 1° Nota: {nota1}\n")
    arquivo.write(f" 2° Nota: {nota2}\n")
arquivo.close()

#PERGUNTA 4:
Resposta:
# Abre o arquivo 'dados.txt' no modo de leitura ('r'), o'r' é para especificar o modo
with open("dados.txt", "r", encoding="utf-8") as arquivo:

    # Lê o conteúdo do arquivo
    conteudo = arquivo.read()
arquivo.close()
# Exibe as informações na tela
print("############ O QUE ESTÁ ESCRITO NO ARQUIVO É ISTO: ############\n\n")
print(conteudo)
print("\n\n")
print("###################### FIM DO CONTEÚDO DO ARQUIVO #############")

#PERGUNTA 5

# Digite o nome do usuário
nome = input("Digite o seu nome de usuário: ")

# Abre o arquivo no modo append, que serve para acrescentar o que o usuário digitar no final do arquivo
with open("acessos.txt", "a", encoding="utf-8") as arquivo:
    # Acrescenta no final do arquivo o que o usuário digitou e pula uma linha
    arquivo.write(nome + "\n")
arquivo.close()

#PERGUNTA 6:
# Digite a mensagem
resposta_usuario = input("Digite uma mensagem: ")

# Abre o arquivo no modo append, que serve para acrescentar o que o usuário digitar no final do arquivo
with open("respostas.txt", "a", encoding="utf-8") as arquivo:

    # Salva a mensagem no arquivo e pula uma linha
    arquivo.write(resposta_usuario + "\n")
arquivo.close()

#PERGUNTA 7:

# Cria o arquivo 'tarefas.txt' no modo de escrita ('w')
with open("tarefas.txt", "w", encoding="utf-8") as arquivo:

    print("--- Aqui está a Lista de Tarefas ---")

    # Cria um laço que vai se repetir 3 vezes
    for i in range(1, 4):
        # Exibe a mensagem para que o usuário possa digitar suas mensagens
        tarefa = input(f"Digite a {i}ª tarefa: ")

        # Salva a tarefa no arquivo e pula uma linha
        arquivo.write(tarefa + "\n")

arquivo.close()

#PERGUNTA 8:

palavra_digitada = input("Digite uma palavra: ").strip().lower()

palavras_boas = ["bom", "ótimo", "otimo"]
palavras_ruins = ["ruim", "péssimo", "pessimo"]

# Verifica as listas para ver onde a palavra está:
if palavra_digitada in palavras_boas:
    resultado = "Positivo"

elif palavra_digitada in palavras_ruins:
    resultado = "Negativo"

else:
  resultado = "Palavra não reconhecida"

with open("sentimentos.txt", "a", encoding="utf-8") as arquivo:
      arquivo.write(f"{resultado} -> Palavra: {palavra_digitada}\n")

arquivo.close()

#PERGUNTA 9:

genero = input("Digite o seu gênero de filme favorito? (ex: ação, aventura, fantasia): ").strip().lower()

if genero in ["ação", "acao"]:
    filme_recomendado = "O legado Bourne"

elif genero in ["aventura"]:
    filme_recomendado = "O senhor dos anéis"

elif genero in ["fantasia"]:
    filme_recomendado = "Harry Potter"

else:
  filme_recomendado = "Triologia Star wars"

with open("recomendacoes.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(filme_recomendado + "\n")

arquivo.close()
