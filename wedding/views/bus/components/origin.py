import reflex as rx

from wedding import utils
from wedding.components import icon_section
from wedding.routes import IconRoutes as icon
from wedding.styles import FontWeight, Size, style


def origin() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            icon_section(
                icon=icon.ICON_UBICATION.value,
                width=Size.BIG.value,
                alt=utils.alt_icon_ubication,
            ),
        ),
        rx.text(utils.bus_origin_title, style=style.BUS_TITLE_SECTION),
        rx.spacer(),
        _bus_text_origin(),
        width="100%",
        align="center",
    )


def _bus_text_origin() -> rx.Component:
    return rx.flex(
        rx.box(
            "Salida ",
            rx.text(
                utils.origin_bus_schedule, font_weight=FontWeight.BOLD.value, as_="span"
            ),
            " desde ",
        ),
        rx.box(
            rx.text(
                utils.hotel_name,
                font_weight=FontWeight.BOLD.value,
                as_="span",
            ),
        ),
        rx.box(
            rx.text(
                utils.hotel_address,
                font_weight=FontWeight.BOLD.value,
                as_="span",
            ),
        ),
        direction="column",
        align="center",
        justify="center",
        font_size=Size.MAIN_TEXTS.value,
    )
