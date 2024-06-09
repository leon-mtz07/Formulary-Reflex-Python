import reflex as rx


class State(rx.State):
    ...


def index() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.flex(
                    rx.image(
                        src="../assets/favicon.ico",
                        width="2.5em",
                        border_radius="10px",
                    ),
                    rx.heading(
                        "Sign in to your account",
                        size="5",
                    ),
                    rx.hstack(
                        rx.text(
                            "New Here?"
                        ),
                        rx.link("Sing Up", href="#")
                    ),
                    justify="start",
                    direction="column",
                    spacing="4",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email Address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@reflex.dev",
                        type="email",
                        size="3",
                        width="100%",
                        required=True
                    ),
                    spacing="2",
                    justify="start",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                        required=True
                    ),
                    spacing="2",
                    justify="start",
                    width="100%",
                ),
                rx.button(
                    "Sign In",
                    width="100%",
                    border_radius="10px",
                    padding="20px",
                    margin_top="15px"
                ),
                rx.hstack(
                    rx.divider(margin="0"),
                    rx.text(
                        "Or continue with",
                        white_space="nowrap",
                        weight="medium"
                    ),
                    rx.divider(margin="0"),
                    align="center",
                    width="100%",
                    margin_top="10px",
                ),
                rx.center(
                    rx.icon_button(
                        rx.icon(tag="github"),
                        variant="soft",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="facebook"),
                        variant="soft",
                        size="3",
                    ),
                    rx.icon_button(
                        rx.icon(tag="twitter"),
                        variant="soft",
                        size="3",
                    ),
                    spacing="4",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%"
            ),
            size="4",
            max_width="28em",
            width="100%",
            margin_top="50px",
        ),
    )


app = rx.App()
app.add_page(index)
