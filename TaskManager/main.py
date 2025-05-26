# Lista para armazenar as tarefas
tarefas = []

def mostrar_tarefas():
    if not tarefas:
        print("Sua lista de tarefas está vazia!")
    else:
        print("Suas tarefas:")
        for idx, tarefa in enumerate(tarefas, 1):
            print(f"{idx}. {tarefa}")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append(tarefa)
    print(f'"{tarefa}" foi adicionada à sua lista.')

def remover_tarefa():
    mostrar_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa que deseja remover: "))
            removida = tarefas.pop(indice - 1)
            print(f'"{removida}" foi removida da sua lista.')
        except (IndexError, ValueError):
            print("Número inválido. Tente novamente.")

def menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Mostrar tarefas")
        print("2. Adicionar tarefa")
        print("3. Remover tarefa")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            mostrar_tarefas()
        elif escolha == '2':
            adicionar_tarefa()
        elif escolha == '3':
            remover_tarefa()
        elif escolha == '4':
            print("Até mais! Boa sorte com suas tarefas.")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o menu
menu()