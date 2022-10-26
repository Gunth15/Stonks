from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class SubmitTicker(Screen):
    pass
    
class GraphDisplays(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('stockkivy.kv')
ticker = ''
class MainApp(App):
    def build(self):
        return kv
    def clicked(self,text_):
        print(text_)
        ticker = text_


if __name__ == '__main__':
    MainApp().run()
