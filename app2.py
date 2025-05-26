import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la página (color de fondo y alineaciones)
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "App mejorada con filas y columnas"

    # 2. Creación de los textos que se mostrarán en la interfaz
    text1 = ft.Text(value="Filas y Columnas", size=24, color=ft.Colors.WHITE)
    page.add(text1)

    # se crea los textos que van en cada fila
    text2 = ft.Text(value="Fila 1, Columna 1", size=21, color=ft.Colors.WHITE)
    text3 = ft.Text(value="Fila 1, Columna 2", size=21, color=ft.Colors.WHITE)
    text4 = ft.Text(value="Fila 2, Columna 1", size=21, color=ft.Colors.WHITE)

    #Creacion de filas y columnas
    fila1_text1 = ft.Row(
        controls=[ft.Container(width=20), text2, text3, text4],
        alignment=ft.MainAxisAlignment.START,
        spacing=50
    )
    page.add(fila1_text1)

    but1 = ft.FilledButton(text="Boton 1")
    but2 = ft.FilledButton(text="Boton 2")
    but3 = ft.FilledButton(text="Boton 3")
    
    fila1_buts = ft.Row(
        controls=[ft.Container(width=20), but1, but2, but3],
        alignment=ft.MainAxisAlignment.START,
        spacing=100
    )
    page.add(fila1_buts)

    col1_text1 = ft.Text(value="Columna 1, Fila 1", size=21, color=ft.Colors.WHITE)
    col1_text2 = ft.Text(value="Columna 1, Fila 2", size=21, color=ft.Colors.WHITE)
    col1_text3 = ft.Text(value="Columna 1, Fila 3", size=21, color=ft.Colors.WHITE)

    # Creación de la columna con los textos
    col1_texts = ft.Column(
        controls=[col1_text1, col1_text2, col1_text3],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )

    col2_texts = ft.Column(
        controls=[
            ft.Text(value="Columna 2, Fila 1", size=21, color=ft.Colors.WHITE),
            ft.Text(value="Columna 2, Fila 2", size=21, color=ft.Colors.WHITE),
            ft.Text(value="Columna 2, Fila 3", size=21, color=ft.Colors.WHITE)
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )

    fila_columnas = ft.Row(
        controls=[ft.Container(width=20), col1_texts, col2_texts],
        alignment=ft.MainAxisAlignment.START,
        spacing=50
    )
    page.add(fila_columnas)
    # 3. Añadir los textos de la columna a la página
    #page.add(col1_texts)

 
# 6. Inicia la aplicación Flet y abre la interfaz en el navegador web
ft.app(target=main, view=ft.WEB_BROWSER)