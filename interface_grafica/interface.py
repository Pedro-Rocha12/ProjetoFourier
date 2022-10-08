import PySimpleGUI as sg
from telaEdicao import TelaEdicao
from transformada import transformada
from coisasUteis import LARGURA_JANELA, ALTURA_JANELA


#Oi, para o projeto funcionar por enquanto temos as dependências de:
#Python 3.10 ou superior,
#PysimpleGUI (pip install PySimpleGUI)
#Pillow (pip install Pillow)
#numpy (pip install numpy)
#cv2 (pip install opencv-python)

#TODO - Função para unir todos os grupos



def escolha(imagem):
    #imgTransf = Transformada(imagem) 2
    #resultadoFreq = editar(imgTransf) #quando acabar retorna imagem editada 3
    #resultado = TransformadaInversa(resultadoFreq) 2
    #mostrar(resultado) #abre nova janela mostrando resultado 1
    return
def open_first_window():
    #Definindo o layout

    layout = [
        [sg.Text("", size=(80,1),justification="center")],
        [sg.Button(image_filename= image_mulie, image_size=(200, 200), key = 'muliepressed',pad=(4,4)),
        sg.Button(image_filename= image_zebra, image_size=(200, 200), key = 'zebrapressed',pad=(4,4))],
        [sg.Button(image_filename= image_mario, image_size=(200, 200), key = 'mariopressed',pad=(4,4)),
        sg.Button(image_filename= image_pengu, image_size=(200, 200), key = 'pengupressed',pad=(4,4))],
        [sg.Text("Ou importe uma imagem:")]
    ]

    #Criando a Window

    window = sg.Window('Fast Fourier Transform',layout,size=(LARGURA_JANELA,ALTURA_JANELA))

    while True:
        event,values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "muliepressed":
            window.close()
            transf = transformada(image_mulie)
            telaPaint = TelaEdicao(transf)
            telaPaint.run()
            break
        elif event == "zebrapressed":
            window.close()
            transf = transformada(image_zebra)
            telaPaint = TelaEdicao(transf)
            telaPaint.run()
            break
        elif event == "mariopressed":
            window.close()
            transf = transformada(image_mario)
            telaPaint = TelaEdicao(transf)
            telaPaint.run()
            break
        elif event == "pengupressed":
            window.close()
            transf = transformada(image_pengu)
            telaPaint = TelaEdicao(transf)
            telaPaint.run()
            break
    window.close()


def open_second_window(image):
    layout = [
        [sg.Text("Fast Fourier Transform Editor", size=(80, 1), justification="center")],
        [sg.Button(image_filename=image, image_size=(300, 300))],
        [sg.Button("Voltar", key="anterior")]
    ]

    window = sg.Window("FFT", layout, size=(LARGURA_JANELA, ALTURA_JANELA))

    # Interagindo o a segunda janela
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "anterior":
            window.close()
            open_first_window()

    window.close()


#Salvando imagens em variáveis
image_mulie = "../data/mulie.png"
image_zebra = "../data/zebra.png"
image_mario = "../data/mario.png"
image_pengu = "../data/pengu.png"

#Elementos da janela introdutoria
layout = [
    [sg.Text("Bem vindo ao protótipo do projeto fourier", size=(100,1),justification="center")],
    [sg.Button("Próxima Página", key = "next")]
]
window = sg.Window('Fast Fourier Transform',layout,size=(LARGURA_JANELA,ALTURA_JANELA), modal=True)

#Interagindo com a janela introdutoria

while True:
    event,values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "next":
        window.close()
        open_first_window()


window.close()

