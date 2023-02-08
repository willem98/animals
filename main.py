from flet import Page
from flet import app
from flet import Text as txt
from flet import Row
from flet import TextField as txtinput
from flet import ElevatedButton as button
from flet import Image
import flet as ft

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