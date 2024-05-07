import reflex as rx

config = rx.Config(
    app_name="wedding",
    tailwind={
        "theme": {
            "extend": {
                "colors": {
                    "purple_default": "#7d4587",
                    "purple_background": "#f3e3fa",
                    "lime-lemon": "#0ef09d",
                }
            }
        }
    },
)
