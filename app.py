base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def xor(string, key):
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
    binario = ''.join(f'{ord(char):08b}' for char in texto)
    binario += '0' * ((6 - len(binario) % 6) % 6)
    base64_string = ''.join(base64_chars[int(binario[i:i+6], 2)] for i in range(0, len(binario), 6))
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


# encrypted_texto = xor(base64_texto, "ESCOLA_COELHO_NETO")

candidatos_exemplo ={
    '15': "Ricardo Nunes",
    '28': "Pablo Marçal",
    '50': "Guilherme Boulos",
    '45': "José Luiz Datena",
    '40': "Tabata Amaral",
    '30': "Marina Helena",
}


def registrar_votos():
    votos = {nome: 0 for nome in candidatos_exemplo.values()}
    global total
    total = 0
    while True:
        for c in candidatos_exemplo:
            print(c,candidatos_exemplo[c])
        escolha = input("Digite o código do prefeito(a) ou -1 para sair da votação: ")
        
        if(escolha in candidatos_exemplo):
            votos[candidatos_exemplo[escolha]] +=1
            total += 1
            print("Voto para o prefeito: ",candidatos_exemplo[escolha], "computado")
        elif(escolha == "-1"):
            print("Saindo da votação")
            break
        else:
            print("Candidato com o número: ", escolha, "não existe.")
    votos_string = "\n".join(f"{candidato}:{voto}" for candidato, voto in votos.items())
    return votos_string


def hash(string, key):
    hash = ""
    hash = xor(string, key).strip()
    hash = texto_para_base64(hash)
    return hash

def decryp_hash(hash, key):
    decryp_hash = hash.strip()
    decrypted_hash = base64_para_texto(decryp_hash)
    decrypted_hash = xor_decrypt(decrypted_hash, key)
    return decrypted_hash
def salvar_dados(dados, key):
    with open ("criptografia_votos", "w") as arquivo:
        arquivo.write(dados + "\n")
        arquivo.write(hash(dados, key) + "\n")
        arquivo.write(str(total))

def criptografar_dados(key):
    string = registrar_votos()
    xor_string = xor(string, key)
    xor_64 = texto_para_base64(xor_string)
    salvar_dados(xor_64, key)

def descriptografar_dados(string, key):
    string_normal = string.strip()
    xor_string = base64_para_texto(string_normal)
    uncripted_string = xor_decrypt(xor_string, key)
    return uncripted_string


def ver_dados(key):
    with open("criptografia_votos", "r") as arquivo:
        linhas = arquivo.readlines()
        decryp = str(decryp_hash(linhas[1], key))
        decryp_without_last = decryp[:-1]
        linhas[0] = linhas[0][:-1]
        if(decryp_without_last == str(linhas[0])):
            print("RELATÓRIO DE VOTAÇÃO")
            print("URNA 012345")
            print("VOTOS")
            for c in candidatos_exemplo:
                print(c ,candidatos_exemplo[c], sep=" - ")

            print("TOTAL DE VOTOS:", linhas[2])
            print(descriptografar_dados(linhas[0], key))
        else:
           print("Hash inválido. Insira a chave correta ou realize uma nova votação.")
        


def menu():
    key = input("Escolha uma chave: *lembre da chave para usar no próximo apuramento de votos* ")
    while True:          
        print("Escolha uma das ações:")
        print("1: Votar")
        print("2: Ver Votos")
        print("3: Sair do app.")
        escolha = input("")
        if(escolha == "1"):
            criptografar_dados(key)
        elif(escolha == "2"):
            ver_dados(key)
        else:
            print("Fechando o app.")
            break

menu()
