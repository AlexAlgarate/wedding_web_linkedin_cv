from typing import Dict

import reflex as rx

from wedding.styles import Size


def create_single_email(email: Dict[str, str]) -> rx.Component:
    """
    Creates a reflex component for a single email.

    Args:
        email (Dict[str, str]): Dictionary containing email information.

    Returns:
        rx.Component: Reflex component for a single email.
    """

    return rx.link(
        rx.text(
            email["email"],
            font_size=[
                "1.2em",
                "1.2em",
                "1.2em",
                "1.2em",
                Size.LARGE.value,
            ],
            font_weight="600",
        ),
        href=f"mailto:{email['email']}",
    )
