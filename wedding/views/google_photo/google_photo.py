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


def google_photo() -> rx.Component:
    """
    Create a component for opening the Google Photos album
    dedicated to the wedding.

    Returns:
    - rx.Component: A Reflex component designed to facilitate
    access to the wedding Google Photos album.
    """

    return card(
        icon_section(icon=icon.ICON_CAMERA.value, alt=utils.alt_icon_camera),
        title_section(title=utils.title_photo),
        text_section(text=utils.google_photo_text_one),
        text_section(text=utils.google_photo_text_two),
        main_button(
            button_name=utils.google_photo_button,
            url=urls.GITHUB_URL,
            z_index="999",
        ),
        id="photos_section",
    )
