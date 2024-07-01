from typing import Dict

import reflex as rx

from wedding.components import secondary_button


def create_single_email(contact: Dict[str, str]) -> rx.Component:
    """
    Creates a reflex component to display email button.

    Args:
        contact (Dict[str, str]): Dictionary containing contact information.

    Returns:
        rx.Component: Reflex component displaying email button.
    """
    return secondary_button(
        button_name=contact["email"],
        url=f"mailto:{contact['email']}",
        icon="mail-open",
    )
