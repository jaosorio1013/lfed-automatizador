import flet as ft
from paginador_planimetria import generar_planimetria


def main(page: ft.Page):
    page.title = "Automatizaciones"
    page.window.width = 1000
    page.window.height = 700
    page.padding = 0

    def change_view(e):
        selected = e.control.selected_index
        if selected == 0:
            content_area.content = duplicate_files_view
        elif selected == 1:
            content_area.content = ft.Text("Proximanent", size=24)
        content_area.update()

    lvl_unused_pages = ft.Text(value="Páginas a saltar", color=ft.Colors.WHITE)
    input_unused_pages = ft.TextField(value="1", width=350, color=ft.Colors.GREY_700, bgcolor=ft.Colors.WHITE)
    lvl_ciudad = ft.Text(value="Ciudad", color=ft.Colors.WHITE)
    input_ciudad = ft.TextField(value="El retiro", width=350, color=ft.Colors.GREY_700, bgcolor=ft.Colors.WHITE)
    lvl_cliente = ft.Text(value="Cliente", color=ft.Colors.WHITE)
    input_cliente = ft.TextField(value="Camilo y Valentina", width=350, color=ft.Colors.GREY_700, bgcolor=ft.Colors.WHITE)
    lvl_diseno = ft.Text(value="Nombre del diseño", color=ft.Colors.WHITE)
    input_diseno = ft.TextField(value="Apartamento Wood", width=350, color=ft.Colors.GREY_700, bgcolor=ft.Colors.WHITE)

    def add_pagination(original_file):
        generar_planimetria(
            original_file=original_file,
            unused_pages=int(input_unused_pages.value),
            ciudad=input_ciudad.value,
            cliente=input_cliente.value,
            diseno=input_diseno.value
        )

    # VARIABLES DE ESTADO
    selected_file_text = ft.Text(
        "No se han seleccionado archivos",
        size=14,
        color=ft.Colors.BLUE_500
    )

    select_plane_button = ft.ElevatedButton(
        "Seleccionar plano y paginar",
        icon=ft.Icons.FOLDER_OPEN,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE_900,
        on_click=lambda _: file_picker.pick_files()
    )

    add_pagination_title = ft.Container(
        content=ft.Text(
            "Organizar Paginación Planimetria",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_500
        ),
        margin=ft.margin.only(bottom=20)
    )

    add_pagination_container = ft.Container(
        content=selected_file_text,
        margin=ft.margin.only(top=10, bottom=10)
    )

    def handle_file_picker(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                selected_file_text.value = f"Plano seleccionado: {f.name}"
                selected_file_text.update()
                add_pagination(f)
                selected_file_text.value = "Paginación finalizada"

    # Configurar el selector de carpetas
    file_picker = ft.FilePicker(on_result=handle_file_picker)
    page.overlay.append(file_picker)

    # VISTA de archivos
    duplicate_files_view = ft.Container(
        content=ft.Column([
            add_pagination_title,
            lvl_unused_pages,
            input_unused_pages,
            lvl_ciudad,
            input_ciudad,
            lvl_cliente,
            input_cliente,
            lvl_diseno,
            input_diseno,
            select_plane_button,
            add_pagination_container,
        ]),
        padding=30,
        expand=True
    )

    content_area = ft.Container(
        content=duplicate_files_view,
        expand=True,
    )

    # MENU
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.PLAY_ARROW,
                selected_icon=ft.Icons.PLAY_ARROW,
                label="Paginar"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                selected_icon=ft.Icons.ADD_CIRCLE,
                label="Proximamente"
            )
        ],
        on_change=change_view,
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                content_area,
            ],
            expand=True,
        )
    )


if __name__ == '__main__':
    ft.app(target=main)