# registrar tarefas a fazer, listar as tarefas, ordernar por status (urgente, sem pressa, etc), remover as tarefas feitas


def adicionar_tarefas(dicionario: dict, tarefa: str, status: str, /):

    if tarefa in dicionario:
        print(' a tarefa ja esta listada !')
    else:
        dicionario[tarefa] = status
    return dicionario

def listar_tarefa(lista: dict, /):
    texto = ''
    for key, valor in lista.items():
         texto += f'{key}: ({valor})\n'
    print(texto)

def filtrar_urgentes(dicionario: dict, /):
    tarefas_urgentes = [key for key in dicionario if dicionario[key] == 'urgente']
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

teste = {'lavar o carro': 'não urgente', 'sair para comprar arroz': 'pouco urgente', 'trocar a geladeira de lugar': 'urgente', 'fazer a janta': 'urgente'}

res = adicionar_tarefas(teste, 'fazer lição de casa', 'urgente')

listar_tarefa(res)

print('-' * 30)
filtrar_urgentes(res)

