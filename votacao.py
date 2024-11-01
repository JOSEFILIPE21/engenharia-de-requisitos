opcao1 = 0
opcao2 = 0
opcao3 = 0
 
    
        
while True:
    print("Sistema de votação")
    print("as opções são:\n 1. opção 1\n 2. opção 2\n 3. opção 3")
    escolha = input("escolha a opção 1 - 2 - 3 ou aperte 0 para exibir o resultado: ")
    if escolha == "1":
        opcao1 += 1
        print(f"você votou na opção {escolha}")
    elif escolha == "2":
        opcao2 +=1
        print(f"você votou na opção {escolha}")
    elif escolha == "3":
        opcao3 +=1
        print(f"você votou na opção {escolha}")
    elif escolha == "0":
        print(f"opção 1: {opcao1} voto(s)\nopção 2: {opcao2} voto(s)\nopção 3: {opcao3} voto(s)")
        break
    else:
        print("opçao invalida")