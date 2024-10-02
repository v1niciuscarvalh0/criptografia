alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# define função de criptografia usando algoritmo de vigenere

def criptografa(msg_original, chave):
    # define variavel para salvar o texto cifrado e o index do caractere da chave 
    txt_cifrado = ""
    index_chave = 0
    
    # itera o numero de vezes do comprimento da mensagem definindo os index de deslocamento necessario e letra do alfabeto correspondente
    for i in range(len(msg_original)):
        deslocamento = alfabeto.index(chave[index_chave])
        letra_alfabeto = alfabeto.index(msg_original[i])
        # aplica a criptografia no caractere
        letra_cifrada = alfabeto[(letra_alfabeto + deslocamento) % 26]
        # adiciona o caractere criptografado
        txt_cifrado += letra_cifrada
        # passa para o proximo index da chave e modulariza o valor
        index_chave = (index_chave + 1) % len(chave)
        
    # retorna texto cifrado
    return txt_cifrado

# define função de descriptografia usando algoritmo de vigenere

def descriptografa(msg_original, chave):
    txt_descifrado = ""
    index_chave = 0
    # o metodo de criptografia é o mesmo, entretando usamos o deslocamento negativo
    
    for i in range(len(msg_original)):
        deslocamento = alfabeto.index(chave[index_chave])
        letra_alfabeto = alfabeto.index(msg_original[i])
        letra_decifrada = alfabeto[(letra_alfabeto - deslocamento) % 26]
        txt_descifrado += letra_decifrada
        index_chave = (index_chave +1 ) % len(chave)
        
    # retorna texto descifrado
    return txt_descifrado



