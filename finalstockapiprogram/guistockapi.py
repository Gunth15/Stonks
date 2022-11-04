from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from teststockapi import Make_Graphs
from kivy.clock import Clock
from kivy.config import Config



Config.set('graphics', 'height', 400)
DONE = False

class SubmitTicker(Screen):
    pass

class LoadingScreen(Screen):

    def on_enter(self):
                
        Clock.schedule_once(self.ChangeScreen,15)
        
    def ChangeScreen(self, NO):

            global DONE


            if DONE == True:
            
                self.manager.current = 'DisplayTerminal'
                DONE = False

            elif DONE == 'ERROR':

                self.manager.current = 'StockTickerEntry'

    
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
        self.man = WindowManager()
        return kv
    def clicked(self,text_):
        print(text_)
        self.text= text_
        Clock.schedule_once(self.nu_graph,1)
        print('done')
        ticker = text_

    def nu_graph(self,nu):
        global DONE
        try:
            print('stable')
            Make_Graphs(str(self.text))
            DONE = True
        except:
            
            print("Timed Out")
            DONE = 'ERROR'
            

            
if __name__ == '__main__':
    MainApp().run()
