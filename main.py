from flet import Page
from flet import app
from flet import Text as txt
from flet import Row
from flet import TextField as txtinput
from flet import ElevatedButton as button
from flet import Image
import flet as ft

class Kelas(ft.UserControl):
    def __init__(self,i, page) -> None:
        super().__init__()
        self.i = i
        self.page = page

    def kelaspage(self,):
        return self.page.reload()

    def build(self):
        return button(self.txt,on_click=self.kelaspage)

def main(page: ft.Page):
    btn = ft.ElevatedButton("Mamalia")
    page.add(btn)

def main(page: ft.Page):
    btn = ft.ElevatedButton("Reptill")
    page.add(btn)

def main(page: ft.Page):
    btn = ft.ElevatedButton("Unggas")
    page.add(btn)

def main(page: ft.Page):
    btn = ft.ElevatedButton("Serangga")
    page.add(btn)

ft.app(target=main)