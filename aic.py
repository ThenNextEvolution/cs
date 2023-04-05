from PIL import Image
from rich_pixels import Pixels
from rich.console import Console
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.geometry import Size
from textual.widgets import Button, Header, Footer, Static
from time import monotonic
from textual.reactive import reactive


class draw(Static):
    left = 0
    img = Image.open("assets/MainCharacters/MaskDude/run.png")
    x, y = img.size
    hel = 320
    console = Console()

    def _on_mount(self) -> None:
        im1 = self.img.crop((self.left, 0, self.x - self.hel, self.y - 0))
        im1 = im1.resize((25, 25))
        xels = reactive(Pixels.from_image(im1))
        xels = Pixels.from_image(im1)
        self.console.print(xels, end="\r")
        self.console.print(end="\x1b[2K")
        self.set_interval(1 / 60, self.update_xels)
        self.update(xels)

    def update_xels(self):
        if self.hel == 0:
            self.hel = 320
        if self.left == 320:
            self.left = 0

        self.hel -= 32
        self.left += 32
        im1 = self.img.crop((self.left, 0, self.x - self.hel, self.y - 0))
        xels = Pixels.from_image(im1)
        self.console.print(xels, end="\r")
        self.console.print(end="\x1b[2K")
        self.update(xels)

class controls(Static):
    url = reactive("assets\MainCharacters\MaskDude\idle.png")


class Display(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "hol/sp.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("c", "cancel", "Cancel")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(draw())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_cancel(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = Display()
    app.run()
