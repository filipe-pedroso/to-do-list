import PySimpleGUI as sg

def createNewTask():
    sg.theme('DarkPurple2')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Limpar')]
    ]

    return sg.Window('To do list',layout=layout,finalize=True)


janela = createNewTask()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Limpar':
        janela.close()
        janela = createNewTask()    