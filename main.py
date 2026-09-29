import json
import os

ARQUIVO = "tarefas.json"

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa ainda.")
    for i, t in enumerate(tarefas, 1):
        marca = "✔" if t["feita"] else " "
        print(f"{i}. [{marca}] {t['titulo']}")

def main():
    tarefas = carregar()
    while True:
        print("\n1-Listar 2-Adicionar 3-Concluir 4-Remover 0-Sair")
        op = input("Escolha: ")
        if op == "1":
            listar(tarefas)
        elif op == "2":
            titulo = input("Nova tarefa: ")
            tarefas.append({"titulo": titulo, "feita": False})
            salvar(tarefas)
        elif op == "3":
            listar(tarefas)
            n = int(input("Número da tarefa: "))
            tarefas[n - 1]["feita"] = True
            salvar(tarefas)
        elif op == "4":
            listar(tarefas)
            n = int(input("Número da tarefa: "))
            tarefas.pop(n - 1)
            salvar(tarefas)
        elif op == "0":
            break

main()
