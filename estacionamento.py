import os

def clear():
    os.system("cls")

vagas = {}
max_vagas = 100
def vagas_estacionamento():
    for i in range(1,(max_vagas + 1)):
        vagas[i] = None
vagas_estacionamento()

def estacionar_veiculo():
    placa = input("Informe a placa do veiculo: ")
    for vaga in vagas:
        if vagas[vaga] == placa:
            return print(f"O veiculo com a placa {placa} já está estacionado")
        elif vagas[vaga] == None:
            vagas[vaga] = placa
            return print(f"O veiculo com a placa {placa} foi estacionado na vaga {vaga}")
        
        
def exibir_vagas():
    for i in vagas:
        if vagas[i] == None:
            print(f"vaga {i} está livre")

def remover_veiculo():
    placa = input("informe a placa do veiculo: ")
    for vaga in vagas:
        if vagas[vaga] == placa:
            vagas[vaga] = None
            return print(f"O veiculo com a placa {placa} foi removido do estacionamento")
    print(f"Nenhum veiculo com a placa {placa} encontrado.")

            

while True:
        
        print("Sistema de Gerenciamento de Estacionamento")
        print("1. Exibir Vagas")
        print("2. Estacionar Veículo")
        print("3. Remover Veículo")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        

        if escolha == '1':            
            exibir_vagas()
        elif escolha == '2':
            clear()
            estacionar_veiculo()
        elif escolha == '3':
            clear()
            remover_veiculo()
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")
