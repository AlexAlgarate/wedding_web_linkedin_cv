import reflex as rx

from wedding import urls, utils
from wedding.components import (
    icon_section,
    secondary_button,
    text_section,
    title_section,
)
from wedding.routes import FileRoutes
from wedding.routes import IconRoutes as icon

from .components import image_celebration, text_celebration


def celebration() -> rx.Component:
    return rx.flex(
        icon_section(icon=icon.ICON_CELEBRATION.value, alt=utils.alt_icon_celebration),
        title_section(title=utils.celebration_title),
        text_section(utils.celebration_text),
        image_celebration(image=FileRoutes.IMAGE_AGRIPINA.value),
        text_celebration(),
        secondary_button(
            button_name=utils.celebration_button,
            url=urls.AGRIPINA_MAPS_URL,
        ),
        direction="column",
        align_items="center",
        align_self="stretch",
        gap="8px",
        scroll_margin_top="75px",
        id="celebration_section",
    )
