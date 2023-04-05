from textual.app import App, ComposeResult
from textual.containers import Container
from textual.geometry import Size
from textual.widgets import Button, Header, Footer, Static
from time import monotonic
from textual.reactive import reactive
from rich_pixels import Pixels
from rich.console import Console

from os import listdir
from os.path import isfile, join
import PIL.Image


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
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")
        yield Image()


class TimeDisplay(Static):
    """A widget to display elapsed time."""


class Image(Static):
    global left,hel,im1,xer,yer
    
   # im1 = img.crop((0,0,xer-320,yer-0))
   # pixels =reactive(Pixels.from_image(im1))
   # test = reactive(im1)
    
    hol = None
    
   
    
    

    def _on_mount(self) -> None:
        global left,hel,im1,xer,yer
        img = PIL.Image.open(r"C:\Users\eyita\cs\assets\MainCharacters\MaskDude\idle.png")
        hel=320
        xer,yer=img.size
        left=0
        im1 = img.crop((left,0,xer-hel,yer-0))
       
        
        def ups():
            global left,hel,im1,xer,yer
            im1 = img.crop((left,0,xer-hel,yer-0))
            if hel ==0:
                hel =320
            if left ==320:
                left = 0
            hel -=32
            left +=32
            self.update(pixels)
            #Image.refresh(pixels)
            Image.auto_refresh
            #6im1.show()
            
        pixels =(Pixels.from_image(im1))
        
        print("boi")
        #console().print(pixels)
        #self.update(pixels) 
        self.set_interval(60 / 60, ups)
        
        
        
    #     global xer,yer
    #     self.img = PIL.Image.open(r"C:\Users\eyita\cs\assets\MainCharacters\MaskDude\idle.png")
    #     xer,yer=self.img.size
    #     im1 = self.img.crop((0,0,xer-320,yer-0))
    #     im1.resize((25,25))
        
        
    #     pixels =reactive( Pixels.from_image(im1))
        
        
    #     self.update(pixels)
        
    #     self.set_interval(1 / 60, Image.update_img(self))

    #     return pixels
    
    def update_img(self)-> None:
        global xer,left,hel,im1
        
        
        
        if hel ==0:
            hel =320
        if left ==320:
            left = 0
        hel -=32
        left +=32
        console = Console()
        
        console.print(pixels)
        self.update(self.pixels)
        
        
        #im1 = self.img.crop((left,0,xer-hel,yer-0))
        #im1.show()
        #im1.resize((25,25))
        #pixels =Pixels.from_image(im1)
        
    def watch_img(self):
        self.update(im1)
        #im1.show()
        Console().print(self.pixels)
        print("watch")



        


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
    for i in range(100):
        app.refresh()
