from textual.app import App, ComposeResult
from textual.containers import Container
from textual.geometry import Size
from textual.widgets import Button, Header, Footer, Static
from time import monotonic
from textual.reactive import reactive
from rich_pixels import Pixels
from rich.console import Console
import pygame



class TimeDisplay(Static):
    """A widget to display elapsed time."""


class Image(Static):
    def _on_mount(self) -> None:
        console = Console()
        pixels = Pixels.from_image_path("bar.png",(50,50))
        console.print(pixels)
        self.update(pixels)
        #Pixels.from_image_path()

    # def get_content_width(self, container: Size, viewport: Size) -> int:
    #     return 50
    #
    # def get_content_height(self, container: Size, viewport: Size, width: int) -> int:
    #     return 50


class Stopwatch(Static):
    """A stopwatch widget."""

    start_time = reactive(monotonic)
    time = reactive(0.0)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "start":
            self.add_class("started")
        elif event.button.id == "stop":
            self.remove_class("started")

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        # yield Button("Start", id="start", variant="success")
        # yield Button("Stop", id="stop", variant="error")
        # yield Button("Reset", id="reset")
        # yield TimeDisplay("00:00:00.00")
        yield Image()


class StopwatchApp(App):
    """A Textual app to manage stopwatches."""
    CSS_PATH = "sp.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("c", "cancel", "Cancel")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Image())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_cancel(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
