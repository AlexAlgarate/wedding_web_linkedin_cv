import reflex as rx

from wedding import urls, utils
from wedding.components import (
    card,
    icon_section,
    main_button,
    text_section,
    title_section,
)
from wedding.routes import IconRoutes as icon


def confirmation() -> rx.Component:
    return card(
        icon_section(
            icon=icon.ICON_CONFIRMATION.value, alt=utils.alt_icon_confirmation
        ),
        title_section(title=utils.confirmation_title),
        text_section(text=utils.confirmation_text),
        main_button(
            button_name=utils.confirmation_button,
            url=urls.CONFIRMATION_URL,
        ),
        id="confirmation_section",
    )
