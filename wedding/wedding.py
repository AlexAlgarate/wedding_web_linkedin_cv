import reflex as rx

from wedding import utils
from wedding.components import (
    farewell_message,
    flowers_between_section,
    lavender_flowers,
    navbar,
)
from wedding.routes import FileRoutes
from wedding.styles import style
from wedding.views.bus.bus_service import bus_service
from wedding.views.celebration.celebration import celebration
from wedding.views.confirmation.confirmation import confirmation
from wedding.views.contact.contact import contact
from wedding.views.countdown.countdown import countdown
from wedding.views.google_photo.google_photo import google_photo
from wedding.views.header.header import header

# from wedding.views.gifts.wedding_gifts import wedding_gifts


@rx.page(
    title=utils.title_main,
    description=utils.description_main,
    image=FileRoutes.IMAGE_HEADER.value,
)
def index() -> rx.Component:
    return rx.vstack(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        lavender_flowers(
            alt=utils.alt_image_lavender,
            image=FileRoutes.IMAGE_LAVENDER_TOP.value,
        ),
        rx.vstack(
            rx.flex(
                header(),
                countdown(),
                flowers_between_section(),
                confirmation(),
                celebration(),
                # wedding_gifts(),
                bus_service(),
                flowers_between_section(),
                contact(),
                flowers_between_section(),
                google_photo(),
                direction="column",
                gap="16px",
                align="center",
                width="100%",
                max_width=style.MAX_WIDTH,
            ),
            width="auto",
        ),
        farewell_message(),
        lavender_flowers(
            alt=utils.alt_image_lavender,
            image=FileRoutes.IMAGE_LAVENDER_BOTTOM.value,
            margin_type=False,
        ),
        align="center",
        width="100%",
        style=style.BASE_STYLE,
        align_items="center",
    )


app = rx.App(
    stylesheets=style.STYLESHEETS,
)
