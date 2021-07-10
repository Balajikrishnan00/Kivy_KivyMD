from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
Builder.load_file('kivyapp.kv')
class BoxLay(Widget):
    pass
class mywidget(Widget):
    name=ObjectProperty()
    pizza=ObjectProperty()
    color=ObjectProperty()
    def press(self):
        name=self.name.text
        pizza=self.pizza.text
        color=self.color.text
        print(name,pizza,color)

class Elder(App):
    def build(self):
        return mywidget()

Elder().run()
