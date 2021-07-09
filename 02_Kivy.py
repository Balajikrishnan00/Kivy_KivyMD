from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MYGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MYGrid, self).__init__(**kwargs)
        self.cols=2

        self.Name=TextInput(multiline=False)
        self.Color=TextInput(multiline=False)
        self.Pizza=TextInput(multiline=False)

        self.add_widget(Label(text='name'))
        self.add_widget(self.Name)

        self.add_widget(Label(text='color'))
        self.add_widget(self.Color)

        self.add_widget(Label(text='pizza'))
        self.add_widget(self.Pizza)

        self.btn=Button(text='Submit')
        #self.btn.bind(on_press=root.press) # MYApp.press
        self.btn.bind(on_press=self.press)
        self.add_widget(self.btn)
    def press(self,i):
        print('Hello Kivy',i)


class MYApp(App):


    def build(self):

        return MYGrid()
if __name__ == '__main__':

    root=MYApp()
    root.run()