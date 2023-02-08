from flet import Page
from flet import app
from flet import Text as txt
from flet import Row
from flet import TextField as txtinput
from flet import ElevatedButton as button
from flet import Image
from flet import UserControl

class Kelas(UserControl):
    def __init__(self,i, page) -> None:
        super().__init__()
        self.i = i
        self.page = page

    def kelaspage(self,):
        return self.page.reload()

    def build(self):
        return button(self.i,on_click=self.kelaspage)


def main(page: Page):
    page.add(Kelas("Serangga",page))
    btn = ft.ElevatedButton("Mamalia")
    btn = ft.ElevatedButton("Reptill")
    btn = ft.ElevatedButton("Unggas")
    page.add(Kelas("Serangga",page))
    page.add(Kelas("Serangga",page))
    page.add(Kelas("Serangga",page))

app(target=main)