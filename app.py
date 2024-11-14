# Definir a string de caracteres usados na codificação Base64
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" 


def xor(string, key):
    # Inicializa uma string vazia para armazenar o resultado da operação XOR
    result = ""
    for i in range(len(string)):
        # XOR entre o código unicode de cada caractere da string e o da key
        character = ord(string[i]) ^ ord(key[i % len(key)])
        # Soma modular
        character = (character + ord(key[i % len(key)])) % 256
        # Adiciona o caractere resultante à string de resultado
        result += chr(character)
    return result

def xor_decrypt(encrypted_string, key):
    # Inicializa uma string vazia para o resultado da descriptografia
    result = ""
    for i in range(len(encrypted_string)):
        # Inverte a soma modular
        character = (ord(encrypted_string[i]) - ord(key[i % len(key)])) % 256
        # Aplica XOR para obter o caractere original
        character = character ^ ord(key[i % len(key)])
        # Adiciona o caractere resultante à string de resultado
        result += chr(character)
    return result



def texto_para_base64(texto):
    # Converte cada caractere do texto para sua representação binária de 8 bits
    binario = ''.join(f'{ord(char):08b}' for char in texto)
    # Adiciona bits de preenchimento para que o comprimento seja múltiplo de 6
    binario += '0' * ((6 - len(binario) % 6) % 6)
    # Mapeia cada grupo de 6 bits para o caractere correspondente em base64_chars
    base64_string = ''.join(base64_chars[int(binario[i:i+6], 2)] for i in range(0, len(binario), 6))
    # Adiciona caracteres de preenchimento '=' para ajustar o comprimento final para múltiplos de 4
    base64_string += '=' * ((4 - len(base64_string) % 4) % 4)
    return base64_string



def base64_para_texto(base64_string):
    # Remove os caracteres de padding '='
    base64_string = base64_string.rstrip('=')
    
    # Converte cada caractere Base64 para seu valor binário de 6 bits
    binario = ''.join(f'{base64_chars.index(char):06b}' for char in base64_string)
    
    # Quebra o binário em grupos de 8 bits (1 byte)
    texto = ''.join(chr(int(binario[i:i+8], 2)) for i in range(0, len(binario), 8))
    
    return texto



# Define o dicionário candidatos_exemplo com códigos de candidatos e seus respectivos nomes

candidatos_exemplo ={
    '15': "Ricardo Nunes",
    '28': "Pablo Marçal",
    '50': "Guilherme Boulos",
    '45': "José Luiz Datena",
    '40': "Tabata Amaral",
    '30': "Marina Helena",
}


def registrar_votos():
    # Inicializa um dicionário de votos com os candidatos, começando com zero votos
    votos = {nome: 0 for nome in candidatos_exemplo.values()}
    # Inicializa uma variável global para armazenar o total de votos 
    global total
    total = 0
    # Inicia um loop para registrar votos continuamente
    while True:
        # Itera sobre o dicionário de candidatos e exibe o código e o nome de cada candidato
        for c in candidatos_exemplo:
            print(c,candidatos_exemplo[c])
        # Solicita ao usuário que digite o código do candidato ou -1 para sair
        escolha = input("Digite o código do prefeito(a) ou -1 para sair da votação: ")
        # Verifica se o código digitado está no dicionário de candidatos
        if(escolha in candidatos_exemplo):
            # Incrementa o contador de votos para o candidato escolhido
            votos[candidatos_exemplo[escolha]] +=1
            # Incrementa o total de votos
            total += 1
            # Exibe uma mensagem confirmando o voto registrado
            print("Voto para o prefeito: ",candidatos_exemplo[escolha], "computado")
            #Retorna ao menu, pois o voto é unitário
            menu()
            return 
            # Verifica se o código digitado é -1 para encerrar a votação
        elif(escolha == "-1"):
            # Exibe uma mensagem indicando a saída da votação e sai do loop
            print("Saindo da votação")
            break
        else:
            # Exibe uma mensagem indicando que o código digitado não existe
            print("Candidato com o número: ", escolha, "não existe.")
        # Constrói uma string contendo o total de votos para cada candidato
    votos_string = "\n".join(f"{candidato}:{voto}" for candidato, voto in votos.items())
    return votos_string


def hash(string, key):
    # Inicializa uma string para o hash
    hash = ""
    # Aplica a função XOR ao texto e à chave fornecida
    hash = xor(string, key).strip()
    # Codifica o texto criptografado em Base64
    hash = texto_para_base64(hash)
    return hash

def decryp_hash(hash, key):
    # Remove espaços em branco do hash fornecido
    decryp_hash = hash.strip()
    # Decodifica o texto em Base64
    decrypted_hash = base64_para_texto(decryp_hash)
    # Descriptografa o texto usando a função xor_decrypt
    decrypted_hash = xor_decrypt(decrypted_hash, key)
    return decrypted_hash
def salvar_dados(dados, key):
    # Abre o arquivo criptografia_votos no modo de escrita
    with open ("criptografia_votos", "w") as arquivo:
        # Escreve a string de votos no arquivo
        arquivo.write(dados + "\n")
        # Escreve a string de dados no arquivo
        arquivo.write(hash(dados, key) + "\n")
        # Escreve a string de total no arquivo
        arquivo.write(str(total))

def criptografar_dados(key):
    # Chama a função registrar_votos e armazena o resultado
    string = registrar_votos()
    # Aplica a função XOR à string de votos com a chave fornecida
    xor_string = xor(string, key)
    # Converte o resultado da função XOR em Base64
    xor_64 = texto_para_base64(xor_string)
    # Chama a função salvar_dados para salvar os dados criptografados
    salvar_dados(xor_64, key)

def descriptografar_dados(string, key):
    # Remove espaços em branco da string criptografada
    string_normal = string.strip()
    # Decodifica a string de Base64 para texto
    xor_string = base64_para_texto(string_normal)
    # Descriptografa o texto usando a função xor_decrypt
    uncripted_string = xor_decrypt(xor_string, key)
    return uncripted_string


def ver_dados(key):
    # Abre o arquivo criptografia_votos no modo de leitura
    with open("criptografia_votos", "r") as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()
        # Descriptografa o hash usando a função decryp_hash
        decryp = str(decryp_hash(linhas[1], key))
        # Remove o último caractere do hash descriptografado
        decryp_without_last = decryp[:-1]
        # Remove o caractere de nova linha da string de votos
        linhas[0] = linhas[0][:-1]
        # Verifica se o hash descriptografado é igual à string de votos
        if(decryp_without_last == str(linhas[0])):
            # Exibe o relatório de votação, incluindo a lista de candidatos e o total de votos
            print("RELATÓRIO DE VOTAÇÃO")
            print("URNA 012345")
            print("VOTOS")
            # Exibe os votos descriptografados
            for c in candidatos_exemplo:
                print(c ,candidatos_exemplo[c], sep=" - ")

            print("TOTAL DE VOTOS:", linhas[2])
            print(descriptografar_dados(linhas[0], key))
        else:
            # Exibe uma mensagem de erro caso o hash seja inválido
           print("Hash inválido. Insira a chave correta ou realize uma nova votação.")
        


def menu():
    # Solicita ao usuário que insira uma chave para criptografia/descriptografia
    key = input("Escolha uma chave: *lembre da chave para usar no próximo apuramento de votos* ")
    # Inicia um loop para o menu de ações
    while True:
        # Exibe as opções do menu para votar, ver votos ou sair          
        print("Escolha uma das ações:")
        print("1: Votar")
        print("2: Ver Votos")
        print("3: Sair do app.")
        # Recebe a escolha do usuário
        escolha = input("")
        if(escolha == "1"):
            # Chama a função criptografar_dados se a escolha for votar
            criptografar_dados(key)
        elif(escolha == "2"):
            # Chama a função ver_dados se a escolha for ver votos
            ver_dados(key)
        elif(escolha == "3"):
            # Sai do aplicativo e exibe uma mensagem de encerramento
            print("Fechando o app.")
            break
        else:
            # Exibe uma mensagem de erro caso a opção escolhida não for uma das disponíveis
            print("Valor inválido")

# Chama a função menu para iniciar o programa
menu()
