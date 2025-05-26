import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la página (color de fondo y alineaciones)
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "App de lista de tareas"

    titulo = ft.Text(value="Lista de Tareas con Flet", size=30, color=ft.Colors.WHITE,
                     weight=ft.FontWeight.BOLD)
    
    def seleccionar_tarea(e):
        pass

    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(
                title=ft.Text(campo_tarea.value),
                leading=ft.Checkbox(on_change=seleccionar_tarea)
            )
    
    campo_tarea = ft.TextField(hint_text="Ingrese una nueva tarea")
    boton_agregar = ft.FilledButton(text="Agregar Tarea", on_click=agregar_tarea)

    tareas = []

    tareas_seleccionadas = ft.Text(value="", size=20, 
                                   weight=ft.FontWeight.BOLD)
    
    page.add(titulo, campo_tarea, boton_agregar, tareas_seleccionadas)

ft.app(target=main, view=ft.WEB_BROWSER)