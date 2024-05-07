import reflex as rx

import wedding.urls as url
from wedding import utils as utils
from wedding.components import secondary_button, text_section
from wedding.routes import FileRoutes
from wedding.styles import Color

from .components import create_countdown_vstack


def countdown() -> rx.Component:
    """
    Creates a countdown component for the wedding date.

    Returns:
        rx.Component: The countdown component.
    """
    countdown_elements = [
        create_countdown_vstack(element="days", text_date="Días"),
        create_countdown_vstack(element="hours", text_date="horas"),
        create_countdown_vstack(element="minutes", text_date="mins"),
        create_countdown_vstack(element="seconds", text_date="segs"),
    ]
    return rx.vstack(
        text_section(utils.countdown_text),
        secondary_button(utils.countdown_button, url=url.CALENDAR_HTML),
        rx.flex(
            *countdown_elements,
            rx.script(src=FileRoutes.JS_COUNTDOWN.value),
            justify="center",
            align="center",
            padding="16px 0px",
            gap="1.5em",
            align_self="stretch",
            background=Color.COUNTDOWN_BACKGROUND.value,
            width="100%",
        ),
        align="center",
        gap="16px",
        id="wedding_date",
        width="100%",
    )
