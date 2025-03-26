
from bible import Bible
from ReadCSV import ReadCSV
from ReadJson import ReadJson

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ButtonGrid(GridLayout):
    def __init__(self, bibleX, **kwargs):
        super(ButtonGrid, self).__init__(**kwargs)
        self.cols = 3 # Number of columns in the grid
        self.rows = int(len(bibleX.getBooks())/self.cols) # Number of rows in the grid
        self.buttons = []
        for i in range(self.cols * self.rows):
            button = Button(text=bibleX.getBooks()[i].getName())
            self.buttons.append(button)
            self.add_widget(button)


class MyApp(App):
    def build(self):
        b = Bible("kjv", "en")
        y = ReadJson(".\en_kjv.json")
        y.read(b)
        self.title = "Bible App"
        return ButtonGrid(b)

if __name__ == '__main__':
    MyApp().run()

