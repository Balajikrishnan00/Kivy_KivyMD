from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.name = TextInput(multiline=False)
        self.pizza = TextInput(multiline=False)
        self.color = TextInput(multiline=False)

        self.add_widget(Label(text='Name'))
        self.add_widget(self.name)

        self.add_widget((Label(text='Color')))
        self.add_widget(self.color)

        self.add_widget(Label(text='Pizza'))
        self.add_widget(self.pizza)

        self.btn = Button(text='Submit', font_size=30, size_hint_y=None, height=50)
        self.btn.bind(on_press=self.press)
        self.add_widget(self.btn)

    def press(self,i):
        n = self.name.text
        c = self.color.text
        p = self.pizza.text
        self.add_widget(Label(text=f'{n},{c},{p}', font_size=30))

        self.name.text = ''
        self.color.text = ''
        self.pizza.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
