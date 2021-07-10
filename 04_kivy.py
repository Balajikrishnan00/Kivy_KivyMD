from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class mywidget(Widget):
    name=ObjectProperty()
    pizza=ObjectProperty()
    color=ObjectProperty()
    def press(self,):
        name=self.name.text

        print('Hello',name)


class kivyapp(App):
    def build(self):
        return mywidget()

app=kivyapp()
app.run()