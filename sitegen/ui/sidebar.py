import flet as ft

from sitegen.core.nav import NavNode, NavTree

_SIDEBAR_WIDTH = 240


def build_sidebar(
    nav_tree: NavTree,
    active_slug: str,
    on_navigate,
    dark: bool = False,
    active_doc_id: str | None = None,
) -> ft.Container:
    """Build the navigation sidebar for the given nav tree and active page."""
    colors = _dark_colors() if dark else _light_colors()
    items: list[ft.Control] = []

    for node in nav_tree.nodes:
        if node.is_section:
            if active_doc_id and node.document_id != active_doc_id:
                continue
            items.append(_section_header(node, active_slug, on_navigate, colors))
            for child in node.children:
                items.append(_page_item(child.title, child.slug, active_slug, on_navigate, colors, indent=16))
        else:
            items.append(_page_item(node.title, node.slug, active_slug, on_navigate, colors, indent=0))

    return ft.Container(
        content=ft.Column(
            controls=items,
            scroll=ft.ScrollMode.AUTO,
            spacing=0,
        ),
        width=_SIDEBAR_WIDTH,
        bgcolor=colors["sidebar_bg"],
        padding=ft.padding.symmetric(vertical=8),
    )


def _light_colors() -> dict:
    return {
        "sidebar_bg": ft.Colors.GREY_100,
        "section_label": ft.Colors.GREY_600,
        "active_bg": ft.Colors.BLUE_50,
        "active_text": ft.Colors.BLUE_700,
        "default_text": ft.Colors.GREY_900,
    }


def _dark_colors() -> dict:
    return {
        "sidebar_bg": ft.Colors.GREY_800,
        "section_label": ft.Colors.GREY_400,
        "active_bg": ft.Colors.BLUE_900,
        "active_text": ft.Colors.BLUE_200,
        "default_text": ft.Colors.GREY_200,
    }


def _section_header(node: NavNode, active_slug: str, on_navigate, colors: dict) -> ft.Control:
    is_active = active_slug == node.slug or active_slug == f"{node.slug}/index"
    return ft.Container(
        content=ft.Text(
            node.title.upper(),
            size=11,
            weight=ft.FontWeight.BOLD,
            color=colors["active_text"] if is_active else colors["section_label"],
        ),
        padding=ft.padding.only(left=16, right=8, top=16, bottom=4),
        on_click=lambda e, s=node.slug: on_navigate(s),
        ink=True,
    )


def _page_item(
    title: str,
    slug: str,
    active_slug: str,
    on_navigate,
    colors: dict,
    indent: int,
) -> ft.Control:
    is_active = active_slug == slug
    return ft.Container(
        content=ft.Text(
            title,
            size=14,
            color=colors["active_text"] if is_active else colors["default_text"],
            weight=ft.FontWeight.W_500 if is_active else ft.FontWeight.NORMAL,
        ),
        padding=ft.padding.only(left=16 + indent, right=8, top=6, bottom=6),
        bgcolor=colors["active_bg"] if is_active else None,
        border_radius=4,
        on_click=lambda e, s=slug: on_navigate(s),
        ink=True,
    )
