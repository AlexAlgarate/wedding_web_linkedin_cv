import reflex as rx

from wedding import utils
from wedding.styles import Size


def text_celebration() -> rx.Component:
    return rx.flex(
        rx.text(utils.wedding_place, font_weight="bold", as_="span"),
        rx.text(utils.wedding_address_street),
        rx.text(utils.wedding_address_province),
        direction="column",
        align="center",
        font_size=[
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
            Size.MAIN_TEXTS.value,
        ],
    )
