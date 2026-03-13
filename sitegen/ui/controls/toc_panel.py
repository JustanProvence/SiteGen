"""In-page table of contents panel.

Reads nested toc_tokens produced by the python-markdown `toc` extension and
renders a right-hand panel with headings indented by level.

Anchor scroll-navigation is deferred to Phase 7 polish (requires an HTML renderer).
"""

import flet as ft

_PANEL_WIDTH = 200
_INDENT_PER_LEVEL = 10


def build_toc_panel(toc_tokens: list[dict], dark: bool = False) -> ft.Container | None:
    """Build the in-page TOC panel from toc_tokens.

    Returns None if there are no sub-headings worth showing (h2+).
    """
    header_color = ft.Colors.GREY_400 if dark else ft.Colors.GREY_700
    item_color = ft.Colors.GREY_300 if dark else ft.Colors.GREY_800
    divider_color = ft.Colors.GREY_600 if dark else ft.Colors.GREY_300

    items: list[ft.Control] = []
    _collect(toc_tokens, items, min_level=2, item_color=item_color)

    if not items:
        return None

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "On this page",
                    size=11,
                    weight=ft.FontWeight.BOLD,
                    color=header_color,
                ),
                ft.Divider(height=1, color=divider_color),
                *items,
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        ),
        width=_PANEL_WIDTH,
        padding=ft.padding.only(left=16, right=8, top=16, bottom=16),
    )


def _collect(
    tokens: list[dict],
    items: list[ft.Control],
    min_level: int,
    item_color,
) -> None:
    for token in tokens:
        level = token.get("level", 1)
        if level >= min_level:
            indent = (level - min_level) * _INDENT_PER_LEVEL
            items.append(
                ft.Container(
                    content=ft.Text(
                        token.get("name", ""),
                        size=13,
                        color=item_color,
                        no_wrap=True,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                    padding=ft.padding.only(left=indent, top=4, bottom=4),
                )
            )
        _collect(token.get("children", []), items, min_level, item_color)
