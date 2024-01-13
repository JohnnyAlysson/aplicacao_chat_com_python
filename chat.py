
#criação de uma aplicação em 3 passo importar flet, cirar função com a pagina como argumento e e chamar a função pelo ft.app(função)
import flet as ft 
from datetime import datetime

def main(pagina):
    titulo = ft.Text("Chat Online") #sempre criar um elemento e depois adicioná-lo
    nome_usuario = ft.TextField(label="Escreva seu nome")
    chat= ft.Column()
    campo_mensagem = ft.TextField(label="Escreva a mensagem")

    def enviar_mensage_no_tunel(informações):
        chat.controls.append(ft.Text(informações))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensage_no_tunel)
   

    def enviar_mensagem(evento):
        horas= datetime.now().hour              # função não estava na aplicação original
        minutos= datetime.now().minute
        segundo = datetime.now().second
        momento= f"{horas}:{minutos}:{segundo}"

        texto_campo_mensagem= f"{momento} - {nome_usuario.value} : {campo_mensagem.value}"

        pagina.pubsub.send_all(texto_campo_mensagem)

        campo_mensagem.value=""
        pagina.update()
        
    botao_enviar=  ft.ElevatedButton("Enviar",on_click=enviar_mensagem)

    def entra_chat(evento):
        popup.open= False
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        linha_de_mensagem= ft.Row([campo_mensagem,botao_enviar])
        pagina.add(linha_de_mensagem)
        texto= f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)

        pagina.update()



    popup = ft.AlertDialog(open=False, modal=True, title= ft.Text("Bem-vindo ao Chat"), content= nome_usuario, actions= [ft.ElevatedButton("Entrar",on_click=entra_chat)])



    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open= True

        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

   
ft.app(main)
