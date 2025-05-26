import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la página (color de fondo y alineaciones)
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 2. Creación de los textos que se mostrarán en la interfaz
    text1 = ft.Text("Hello, Flet!")
    text2 = ft.Text("Este es un ejemplo para aprender Flet!")

    # 3. Definición de la función que se ejecuta al hacer clic en el botón
    def change_text2(e):
        # Cambia el texto de text2 y actualiza la página
        text2.value = "vamos avanzando en el aprenizaje de Flet!"
        page.update()

    # 4. Creación del botón y asignación de la función al evento on_click
    button1 = ft.FilledButton(text="Cambiar texto 2", on_click=change_text2)

    # 5. Agrega los controles (textos y botón) a la página
    page.add(text1, text2, button1)

# 6. Inicia la aplicación Flet y abre la interfaz en el navegador web
ft.app(target=main, view=ft.WEB_BROWSER)
# print("hola")
