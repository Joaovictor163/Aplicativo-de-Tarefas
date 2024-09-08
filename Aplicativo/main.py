# registrar tarefas a fazer, listar as tarefas, ordernar por status (urgente, sem pressa, etc), remover as tarefas feitas


def criar_tarefas(tarefa: str, status: str, /):
    #lista_tarefas = list() #FIXE Mudar a lista para ser criada no escopo da função principal que vai rodar o código 
    lista_tarefas = dict()
    lista_tarefas[tarefa] = status
    return lista_tarefas

def listar_tarefa(lista: list, /):
    for indice, items in enumerate(lista):
        texto += f'{indice}: {items[0]} ({items[1]})\n'
    print(texto)
    return texto

def filtrar_urgentes(lista: list, /):
    tarefas_urgentes = [item[0] for item in lista if item[1] == 'urgente']
    for tasks in tarefas_urgentes:
        print(tasks)


def marcar_concluida(txt: str, /):
    print('Essas são suas tarefas pendentes atualmente: ')
    txt = txt.split('\n')
    for tasks in txt:
        print(tasks)
    op = input('Insira o número da tarefa para marca-lá como conclúida')
    if op.isnumeric and op in tasks:
        pass


def alterar_tarefa():
    pass



'''lista_nova = [('lavar louça', 'urgente'), ('limpar casa', 'pouco urgente'), ('pagar o mercado', 'urgente'), ('passear com a safira', 'sem pressa'), ('limpar o quarto', 'urgente')]


listar_tarefa(lista_nova)
'''

