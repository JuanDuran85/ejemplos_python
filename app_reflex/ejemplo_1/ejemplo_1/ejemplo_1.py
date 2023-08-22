"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from ejemplo_1 import style

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style), # type: ignore
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style), # type: ignore
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            placeholder="Ask a question",
            style=style.input_style, # type: ignore
        ),
        rx.button("Ask", style=style.button_style), # type: ignore
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
    )


app = rx.App()
app.add_page(index)
app.compile()


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
