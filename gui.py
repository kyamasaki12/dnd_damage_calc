import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# ddc = D&d Damage Calculator


class ddcInput(GridLayout):
    def __init__(self, **kwargs):
        super(ddcInput, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='userName'))
        self.username=TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

     

class ddcApp(App):
    def build(self):
        return ddcInput()


if __name__ == '__main__':
    ddcApp().run()