
import kivy
import matplotlib 
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.uix.label import Label
from kivy.uix.label import Widget
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder



Builder.load_file('Split.kv')

class MyLayout(Widget):
    pass
class SplitScreenApp(App):
    def build(self):
        return MyLayout()















  
if __name__ == "__main__":
    SplitScreenApp().run()
