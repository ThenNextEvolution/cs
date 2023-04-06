from PIL import Image
from rich_pixels import Pixels
from rich.console import Console
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.geometry import Size
from textual.widgets import Button, Header, Footer, Static,Input
from time import monotonic
from textual.reactive import reactive



class InputApp(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="SPRITE IMAGE",id="spr")
        yield Input(placeholder="NUMBER OF SPRITES IN  ROW", id="num")

    def on_input_submitted(self,message : Input.Submitted):
        if message.input.id=="spr":
            draw.img=Image.open(""+message.value)
        
    
        if message.input.id=="num":
            draw.right=message.value * draw.y



class draw(Static):
    
    left = 0
    img = Image.open("assets\MainCharacters\MaskDude\idle.png")
    x, y = img.size
    siz=32
    top =0
    right = y-siz
    x2, y2 = img.size
    

    def _on_mount(self) -> None:
        
        im1 = self.img.crop((self.left, self.top, self.x - self.right, self.y - 0))
        #im1 = im1.resize((self.x2//4,self.y2//4))
        xels = reactive(Pixels.from_image(im1))
        xels = Pixels.from_image(im1)
        #self.console.print(xels, end="\r")
       # self.console.print(end="\x1b[2K")
        self.set_interval(5 / 60, self.update_xels)
        self.update(xels)

    def update_xels(self):
        if self.right == 0:
            self.right = self.x - self.siz
        if self.left == self.x-self.siz:
            self.left = 0

        self.right -= self.siz
        self.left += self.siz
        im1 = self.img.crop((self.left, self.top, self.x - self.right, self.y - 0))
        #im1 = im1.resize((self.x2//4,self.y2//4))
        
        xels = Pixels.from_image(im1)
        
       # self.console.print(xels, end="\r")
       # self.console.print(end="\x1b[2K")
        self.update(xels)

class controls(Static):
    url = reactive("assets\MainCharacters\MaskDude\idle.png")
    spritesnum = reactive(32)
    level = reactive(0)
    imglen = reactive(352)
    fps = reactive(6)
    

class Display(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = "hol/sp.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), ("c", "cancel", "Cancel")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield draw()
        yield InputApp()
        

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_cancel(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = Display()
    app.run()
