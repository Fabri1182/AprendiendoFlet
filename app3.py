import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la página (color de fondo y alineaciones)
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "App de lista de tareas"

    #titulo = ft.Text(value="Lista de Tareas con Flet", size=30, color=ft.Colors.WHITE,
    #                 weight=ft.FontWeight.BOLD)

    titulo = ft.Stack(
            [
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            "Listador de Tareas",
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                foreground=ft.Paint(
                                    color=ft.Colors.BLUE_700,
                                    stroke_width=6,
                                    style=ft.PaintingStyle.STROKE,
                                ),
                            ),
                        ),
                    ],
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            "Listador de Tareas",
                            ft.TextStyle(
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.GREY_300,
                            ),
                        ),
                    ],
                ),
            ]
        )
    
    tareas = [] # Lista para almacenar las tareas

    def eliminar_tareas_realizadas(e):
        #nonlocal tareas
        # Elimina las tareas que están marcadas (checkbox seleccionado)
        tareas[:] = [t for t in tareas if not t.leading.value]
        # Después de eliminar, ya no hay tareas realizadas
        tareas_realizadas.value = ""
        actualizar_lista()

    def seleccionar_tarea(e):
        realizadas = [t.title.value for t in tareas if t.leading.value]
        tareas_realizadas.value = "Tareas realizadas: " + ", ".join(realizadas)
        page.update()

    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()

    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(
                title=ft.Text(campo_tarea.value),
                leading=ft.Checkbox(on_change=seleccionar_tarea)
            )
        tareas.append(tarea)         # Agrega la tarea a la lista
        campo_tarea.value = ""       # Limpia el campo de texto
        actualizar_lista()           # Actualiza la lista en la interfaz
    
    campo_tarea = ft.TextField(hint_text="Ingrese una nueva tarea",
                               on_submit=agregar_tarea)  # <-- Esto permite agregar con ENTER)
    boton_agregar = ft.FilledButton(text="Agregar Tarea", on_click=agregar_tarea)
    lista_tareas = ft.ListView(expand=True, spacing=5)
        
    tareas_realizadas = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)
    boton_eliminar_tr = ft.FilledButton(text="Eliminar tareas realizadas",
                                     on_click=eliminar_tareas_realizadas)

    page.add(titulo, campo_tarea, boton_agregar, lista_tareas, tareas_realizadas,
              boton_eliminar_tr)

ft.app(target=main, view=ft.WEB_BROWSER, port=8080)