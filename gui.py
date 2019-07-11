import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import app

# ddc = D&d Damage Calculator
# calculations(numDice, numAttacks, toCrit, proficiency, ability,
#              toDamage, magicWeapon, advantage_string, gwf)


class DamageForm(BoxLayout):
    d4 = ObjectProperty()
    d6 = ObjectProperty()
    d8 = ObjectProperty()
    d10 = ObjectProperty()
    d12 = ObjectProperty()
    numAttacks = ObjectProperty()
    toCrit = ObjectProperty()
    proficiency = ObjectProperty()
    abilityModifier = ObjectProperty()
    toDamage = ObjectProperty()
    magicWeapon = ObjectProperty()
    advantageString = ObjectProperty()
    gwf = ObjectProperty()

    def run_test(self):
        # print("number of attacks is :'{}'".format(self.numAttacks.text))
        numDice = [self.d4, self.d6, self.d8, self.d10, self.d12]
        d4 = int(float(self.d4.text))
        d6 = int(float(self.d6.text))
        d8 = int(float(self.d8.text))
        d10 = int(float(self.d10.text))
        d12 = int(float(self.d12.text))
        numAttacks = int(float(self.numAttacks.text))
        toCrit = int(float(self.toCrit.text))
        proficiency = int(float(self.proficiency.text))
        abilityModifier = int(float(self.abilityModifier.text))
        toDamage = int(float(self.toDamage.text))
        magicWeapon = int(float(self.magicWeapon.text))
        dieArray = [d4, d6, d8, d10, d12]
        print("non-sharpsooter:")
        print(app.calculations(dieArray, numAttacks, toCrit,
                               proficiency, abilityModifier, toDamage,
                               magicWeapon, self.advantageString.text,
                               self.gwf.text, 'no'))
        print("with sharpshooter:")
        print(app.calculations(dieArray, numAttacks, toCrit,
                               proficiency, abilityModifier, toDamage,
                               magicWeapon, self.advantageString.text,
                               self.gwf.text, 'yes'))
        # print(app.calculations([0, 0, 1, 0, 0], 1, 20, 3, 3,
        #            2, 0, 'advantage', 'no'))
        # print(numAttacks.type)
    pass


class ddcApp(App):
    pass


if __name__ == '__main__':
    ddcApp().run()
