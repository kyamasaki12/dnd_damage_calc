import kivy
from kivy.app import App
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.cache import Cache
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image

import app
import plot
import helper

# ddc = D&d Damage Calculator
# calculations(numDice, numAttacks, toCrit, proficiency, ability,
#              toDamage, magicWeapon, advantage_string, gwf)


class DamageForm(Screen):
    # declare object properties
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

    printNonSharpshooter =  ObjectProperty()
    printSharpshooter = ObjectProperty()

    # runtests runs the backend calculations for the app.

    def run_test(self):
        # define and initialize variables from kivy object
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
        # run the calculations for sharpshooter and non-sharpshooter
        non_sharpshooter = app.calculations(dieArray, numAttacks, toCrit,
                                proficiency, abilityModifier, toDamage,
                                magicWeapon, self.advantageString.text,
                                self.gwf.text, 'no')
        sharpshooter = app.calculations(dieArray, numAttacks, toCrit,
                                proficiency, abilityModifier, toDamage,
                                magicWeapon, self.advantageString.text,
                                self.gwf.text, 'yes')
        # create plots saved to folder
        plot.hist(non_sharpshooter, sharpshooter)
        # convert arrays for printing
        non_sharpshooter = helper.convertArray(non_sharpshooter)
        sharpshooter = helper.convertArray(sharpshooter)
        # print to gui the arrays
        self.printNonSharpshooter.text = non_sharpshooter
        self.printSharpshooter.text = sharpshooter
    pass

# code for display graphs screen

class DisplayGraphs(Screen):
    # direct source to images, hardcoded into app
    img_src1 = "images/toHit.png"
    img_src2 = "images/damage.png"
    # retrieve object property
    toHitHist = ObjectProperty()
    damageHist = ObjectProperty()

    # create clock to refresh 5 times per second.
    # 5 times per second should be more than enough to refresh before
    # a user is able to see the graph

    def __init__(self,**kwargs):
        super(DisplayGraphs,self).__init__(**kwargs)
        Clock.schedule_interval(self.update_graphs, .2)
    
    # code to update the graphs

    def update_graphs(self, dt):
        self.toHitHist.reload()
        self.damageHist.reload()
        
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("app.kv")

class ddcApp(App):
    def build(self):
        return kv
    pass


if __name__ == '__main__':
    ddcApp().run()
