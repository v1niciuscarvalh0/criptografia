# importa arquivos com as funções de criptografia e descriptografia de cesar e vigenere
import cesar 
import vigenere

#Cria interface com usuario
print("\nO que deseja fazer?")
print("1 - Criptografar")
print("2 - Descriptografar")


opt = int(input('Digite a opção desejada: '))


if(opt == 1):
    print("1 - Cesar")
    print("2 - Vigenare")
    alg = int(input("Escolha o algoritmo para criptografia: "))
    
    match alg:
        case 1:
            # aceita a mensagem e trata ela
            msg = input("Digite a mensagem a ser cifrada: ").lower().strip().replace(" ", "")
            chave = int(input("Chave da mensagem: "))
            
            # chama a função que faz a criptografia e mostra em tela o valor criptografado
            print("Mensagem criptografada:\n " +  cesar.criptografaCifraCesar(msg, chave))
        case 2: 
            # aceita a mensagem e trata ela
            msg = input("Digite a mensagem a ser cifrada: ").lower().strip().replace(" ", "")
            chave = input("Chave da mensagem: ").lower().strip().replace(" ", "")
            
            # chama a função que faz a criptografia e mostra em tela o valor criptografado
            print("Mensagem criptografada:\n " + vigenere.criptografa(msg, chave))
        case _:
            
            # se digitar opção não disponivel volta erro
            print("Opção inválida")
elif(opt == 2):
    print(" 1 - Cesar")
    print(" 2 - Vigenare")
    alg = int(input("Escolha o algoritmo para descriptografia: "))
    
    match alg:
        case 1:
            # aceita a mensagem criptografada e trata ela
            msg = input("Digite a mensagem a ser descifrada: ").lower().strip().replace(" ", "")
            chave = int(input("Chave da mensagem: "))
            
            # chama a função que faz a descriptografia e mostra em tela o valor descriptografado
            print("Mensagem descriptografada:\n" + cesar.descriptografaCifraCesar(msg, chave))
        case 2:
            # aceita a mensagem criptografada e trata ela
            msg = input("Digite a mensagem a ser descifrada: ").lower().strip().replace(" ", "")
            chave = input("Chave da mensagem: ").lower().strip().replace(" ", "")
            
            # chama a função que faz a descriptografia e mostra em tela o valor descriptografado
            print("Mensagem descriptografada:\n " + vigenere.descriptografa(msg, chave))
        case _:
            
            # se digitar opção não disponivel volta erro
            print("Opção inválida")
else:
    # se digitar opção não disponivel volta erro
    print("Opção inválida")
    
    






