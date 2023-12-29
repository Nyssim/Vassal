import flet as ft

def main(page: ft.Page):
    #Configuração de página
    page.title = "Vassal"
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY

    #Elementos
    title_app = ft.Text(value = "Vassal", color = "White") 
    first_name = ft.TextField(label = "Seu Nome", bgcolor = "White", border_radius = 15)
    send_button = ft.ElevatedButton(text = "Confirmar")

    #Header / cabeçalho da página
    page.appbar = ft.AppBar(
        bgcolor = "#2196f3",
        title = title_app,

    )

    #Main / Conteudo da página
    page.add(
        ft.Row(
            controls = [
                first_name
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            controls = [
                send_button
            ],
            alignment=ft.MainAxisAlignment.CENTER 
        ),
    )

    page.update()
ft.app(target = main)