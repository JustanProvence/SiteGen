import flet as ft

from sitegen.config import HOST, PORT
from sitegen.export.pdf_server import pdf_server
from sitegen.ui.app_shell import build_app


def main() -> None:
    pdf_server.start()
    ft.app(
        target=build_app,
        host=HOST,
        port=PORT,
        view=ft.AppView.WEB_BROWSER,
    )


if __name__ == "__main__":
    main()
