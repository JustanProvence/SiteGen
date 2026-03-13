"""Custom code block widget with copy-to-clipboard button."""

import flet as ft


def build_code_block(language: str, code: str, page: ft.Page, dark: bool = False) -> ft.Control:
    border_color = ft.Colors.GREY_700 if dark else ft.Colors.GREY_300
    label_color = ft.Colors.GREY_500

    def _copy(_e: ft.ControlEvent) -> None:
        async def _do_copy(text: str = code) -> None:
            await ft.Clipboard().set(text)

        page.run_task(_do_copy)

    copy_icon = ft.IconButton(
        icon=ft.Icons.CONTENT_COPY,
        icon_size=16,
        icon_color=label_color,
        tooltip="Copy",
        style=ft.ButtonStyle(padding=ft.padding.all(4)),
        on_click=_copy,
    )

    header_controls: list[ft.Control] = []
    if language:
        header_controls.append(ft.Text(language, size=11, color=label_color, font_family="monospace"))
    header_controls.append(ft.Container(expand=True))
    header_controls.append(copy_icon)

    # Render the code as ft.Markdown to preserve Flet's built-in syntax highlighting
    fence = f"```{language}\n{code.rstrip()}\n```"
    code_md = ft.Markdown(
        value=fence,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme=ft.MarkdownCodeTheme.GITHUB,
        selectable=True,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(controls=header_controls, spacing=4),
                code_md,
            ],
            spacing=0,
            tight=True,
        ),
        border=ft.border.all(1, border_color),
        border_radius=8,
        padding=ft.padding.only(left=8, right=8, top=8, bottom=0),
        margin=ft.margin.symmetric(vertical=8),
    )
