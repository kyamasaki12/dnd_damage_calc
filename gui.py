import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import app

# ddc = D&d Damage Calculator
# calculations(numDice, numAttacks, toCrit, proficiency, ability,
#              toDamage, magicWeapon, advantage_string, gwf)


class ddcInput(GridLayout):
    def __init__(self, **kwargs):
        super(ddcInput, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='numDice'))
        self.numDice = TextInput(multiline=False)
        self.add_widget(self.numDice)

        self.add_widget(Label(text='numAttacks'))
        self.numAttacks = TextInput(multiline=False)
        self.add_widget(self.numAttacks)

        self.add_widget(Label(text='toCrit'))
        self.toCrit = TextInput(multiline=False)
        self.add_widget(self.toCrit)

        self.add_widget(Label(text='proficiency'))
        self.proficiency = TextInput(multiline=False)
        self.add_widget(self.proficiency)

        self.add_widget(Label(text='ability'))
        self.ability = TextInput(multiline=False)
        self.add_widget(self.ability)

        self.add_widget(Label(text='toDamage'))
        self.toDamage = TextInput(multiline=False)
        self.add_widget(self.toDamage)

        self.add_widget(Label(text='magicWeapon'))
        self.magicWeapon = TextInput(multiline=False)
        self.add_widget(self.magicWeapon)

        self.add_widget(Label(text='advantageString'))
        self.advantageString = TextInput(multiline=False)
        self.add_widget(self.advantageString)

        self.add_widget(Label(text='gwf'))
        self.gwf = TextInput(multiline=False)
        self.add_widget(self.gwf)

        

class ddcApp(App):
    def build(self):
        return ddcInput()


if __name__ == '__main__':
    ddcApp().run()
    print("this is the end")