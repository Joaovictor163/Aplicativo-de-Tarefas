
# registrar tarefas a fazer, listar as tarefas, ordernar por status (urgente, sem pressa, etc), remover as tarefas feitas


def adicionar_tarefas(dicionario: dict, tarefa: str, status: str, /): # certo
    if tarefa in dicionario:
        print(' a tarefa ja esta listada !')
    else:
        dicionario[tarefa] = status
    return dicionario

def listar_tarefa(lista: dict, /): # certo
    texto = ''
    for key, valor in lista.items():
         texto += f'{key}: ({valor})\n'
    print(texto)

def filtrar_urgentes(dicionario: dict, /): # certo
    tarefas_urgentes = [key for key in dicionario if dicionario[key] == 'urgente']
    for tasks in tarefas_urgentes:
        print(tasks)


def marcar_concluida(dicionario: dict, lista_concluidas: list, /):
    concluir = input('Digite o nome da tarefa que deseja marcar como concluida: ')
    task_name = dicionario.pop(concluir, {})
    if task_name:
        lista_concluidas.append(concluir)
    return lista_concluidas

lista_das_concluidas = list()

teste = {'lavar o carro': 'não urgente', 'sair para comprar arroz': 'pouco urgente', 'trocar a geladeira de lugar': 'urgente', 'fazer a janta': 'urgente'}

res = adicionar_tarefas(teste, 'fazer lição de casa', 'urgente')

listar_tarefa(res)

print('-' * 30)
filtrar_urgentes(res)

final = marcar_concluida(res, lista_das_concluidas)

print(final)