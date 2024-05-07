import os
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv()

menu_data: Dict[str, str] = {
    "Confirmación": "/#confirmation_section",
    "Dirección": "/#celebration_section",
    "Autobús": "/#bus_service_section",
    "Contacto": "/#contact_section",
    "Fotos": "/#photos_section",
}


# Web descriptions
title_main = "Invitación de boda de Vicky y Álex 30/08/2024"
description_main = """
    ¡Quedas invitada a nuestra boda! ¡Acompáñanos en este día mágico e inolvidable!
"""


# Header texts
title_header = "¡Nos casamos!"
wedding_date: List[str] = [
    "30",
    "agosto",
    "2024",
]
wedding_hour = "19:00"


# Image descriptions
alt_image_celebration = "Foto de la entrada de La Agripina."
alt_image_partners = "Foto principal de los novios."
label_image_celebration = "Pincha en la imagen para visitar el sitio web de La Agripina"
alt_image_leafs = "Foto de unas hojas amarillas."
alt_image_lavender = "Foto de unas ramas de lavanda con sus hojas"

# Icons desriptions
alt_icon_confirmation = "Icono de un sobre morado"
alt_icon_celebration = "Icono de un pórtico con velo morado"
alt_icon_bus = "Icono de un bus morado"
alt_icon_ubication = "Icono de ubicación morado"
alt_icon_contact = "Icono de un teléfono y un mensaje de texto morado"
alt_icon_whatsapp = "Icono de Whatsapp morado"
alt_icon_camera = "Icono de una cámara de fotos morada"


# SECTION TEXTS
# Countdown texts
countdown_title: str = "¡Cuenta atrás!"
countdown_text = "¡Ven a acompañarnos en el día más feliz de nuestras vidas!"
countdown_button = "Guardar fecha"

# Confirmation
confirmation_title = "Confirmación"
confirmation_button = "Confirmar asistencia"
confirmation_text = """Seguro que tienes muchas ganas de compartir este día con nosotros.\n
    ¿Confirmas tu asistencia?"""


# Celebration
celebration_title = "¿Dónde nos casamos"
celebration_button = "Abrir en Google Maps"
celebration_text = "Hemos elegido un sitio muy especial para celebrar este gran día."
wedding_place = "La Agripina"
wedding_address_street = "Callejón los Romanos, 1"
wedding_address_province = "Punta Umbría, Huelva"


# Bus
but_title = "Servicio de autobús"
bus_text = """
    Para facilitar la asistencia habrá un servicio de autobuses tanto a la ida como a la vuelta.
"""
bus_origin_title = "Ida a la ceremonia"
bur_origin_address = "Av. Martín Alonso Pinzón, 34"
hotel_name = "Senator Huelva Hotel"
hotel_address = "C/ Pablo Rada"
# origin_address = "El Punto, Av. Martín Alonso Pinzón, 34"  # Si sale de El Punto
origin_bus_schedule = "pte hora"
# origin_bus_schedule = "17:00"

bus_destination_title = "Regreso a casa"
# bus_destination_title = "Vuelta a descansar"

destination_address = "Cjón. los Romanos, 1 (Punta Umbría, Huelva)"


# Photo Album
title_photo = "Álbum de Fotos"
google_photo_text_one = "¿Quieres recordar este día para siempre?"
google_photo_text_two = """
    Comparte tus fotos de la boda subiéndolas al albúm compartido de Google Fotos.
"""
google_photo_button = "Abrir álbum"


# Gift
gift_title = "Lista de regalos"
gift_text = """
    Vuestra presencia es nuestro mayor regalo,
    pero si nos queréis hacer una aportacion para ayudarnos a celebrar,
    este es nuestro número de cuenta
"""
account_number_text = os.getenv("ACCOUNT_NUMBER")


# Contact
contact_title = "Contacta con nosotros"
contact_bride = dict(
    name="Vicky",
    email=os.getenv("VICKY_EMAIL"),
    phone_number=os.getenv("VICKY_PHONE"),
)
contact_groom = dict(
    name="Álex",
    email=os.getenv("ALEX_EMAIL"),
    phone_number=os.getenv("ALEX_PHONE"),
)
contact_text_whatsapp = """
Ponte en contacto con nosotros a través de Whatsapp haciendo click directamente en el botón
"""
contact_text_email = "Si te es más cómodo, puedes mandarnos un correo a:"


# Bottom
bottom_text = "Te esperamos"
