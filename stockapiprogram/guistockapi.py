from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from teststockapi import Make_Graphs


class SubmitTicker(Screen):
    pass
    
class GraphDisplays(Screen):
    def on_pre_enter(self):
        
        self.free= self.ids.free
        self.debt= self.ids.debt
        Clock.schedule_once(self.update_image, 0.2)

    def update_image(self,nu):

        self.free.reload()
        self.debt.reload()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('stockkivy.kv')
ticker = ''
class MainApp(App):
    
    def build(self):
        return kv
    
    def clicked(self,text_):
        print(text_)
        self.text= text_
        Clock.schedule_once(self.nu_graph,0.2)
        print('done')
        ticker = text_

    def nu_graph(self,nu):
        print('stable')
        Make_Graphs(str(self.text))

        
if __name__ == '__main__':
    MainApp().run()
