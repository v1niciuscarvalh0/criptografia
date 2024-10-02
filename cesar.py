alfabeto = ["a","b","c","d","e","f","g","h","i",
            "j","k","l","m","n","o","p","q","r",
            "s","t","u","v","w","x","y","z"]      

# define função de criptografia usando algoritmo de cesar
def criptografaCifraCesar(item, chave):
    # define e inicializa variavel para salvar o valor cifrado
    cifrado = ""

    # itera por cada letra da mensagem e ser cifrada
    for i in item:
        # se letra esta no alfabeto
        if(i in alfabeto):
            # define deslocamento e salva caractere cifrado
            deslocamento = (alfabeto.index(i) + chave) % 26
            cifrado += alfabeto[deslocamento]
        else:
            # caso valor estiver fora do alfabeto volta erro
            return "Valor de texto invalido"
    # retorna valor cifrado
    return cifrado
    
# define função de descriptografia usando algoritmo de cesar
def descriptografaCifraCesar(item, chave):
    # para descriptografar ele aplica o mesmo algoritimo com a chave negativa
    descifrado = criptografaCifraCesar(item, -(chave))
    # retorna valor descifrado
    return descifrado
