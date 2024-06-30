import reflex as rx

from wedding import utils
from wedding.components import card, icon_section, text_section, title_section
from wedding.routes import IconRoutes as icon

from .components import create_single_email, whatsapp_button


def contact() -> rx.Component:
    """
    Create a contact information section component.

    Returns:
    - rx.Component: A Reflex component representing the contact information section.
    """

    return card(
        icon_section(icon=icon.ICON_PHONE.value, alt=utils.alt_icon_contact),
        title_section(title=utils.contact_title),
        text_section(utils.contact_text_whatsapp),
        whatsapp_button(utils.contact_groom),
        text_section(utils.contact_text_email),
        create_single_email(utils.contact_groom),
        id="contact_section",
    )
