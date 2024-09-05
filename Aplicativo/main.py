# registrar tarefas a fazer, listar as tarefas, ordernar por status (urgente, sem pressa, etc), remover as tarefas feitas


def criar_tarefas(tarefa: str, status: str, /):
    lista_tarefas = list()
    lista_tarefas.append((tarefa, status))
    return lista_tarefas

def listar_tarefa(lista: list, /):
    for items in lista:
        texto += f'{items[0]} ({items[1]})\n'
    print(texto)

def filtrar_urgentes(lista: list, /):
    tarefas_urgentes = [item[0] for item in lista if item[1] == 'urgente']
    for tasks in tarefas_urgentes:
        print(tasks)





'''lista_nova = [('lavar louça', 'urgente'), ('limpar casa', 'pouco urgente'), ('pagar o mercado', 'urgente'), ('passear com a safira', 'sem pressa'), ('limpar o quarto', 'urgente')]


filtrar_urgentes(lista_nova)

'''
