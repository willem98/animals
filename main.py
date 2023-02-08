from flet import Page
from flet import app
from flet import Text as txt
from flet import Row
from flet import TextField as txtinput
from flet import ElevatedButton as button
from flet import Image
from flet import UserControl

class Kelas(UserControl):
    def __init__(self,i, page, ) -> None:
        super().__init__()
        self.i = i
        self.page = page

    def kelaspage(self, e):
        self.page.clean()
        self.page.add(txt(self.i))
        return self.page.reload()

    def build(self):
        print(self.i,self.page)
        return button(self.i,on_click=self.kelaspage)


def main(page: Page):
    page.add(Kelas("Serangga",page))
    page.add(Kelas("Mamalia",page))
    page.add(Kelas("Reptil",page))
    page.add(Kelas("Unggas",page))

app(target=main)