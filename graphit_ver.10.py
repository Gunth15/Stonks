#import pyplot
from matplotlib import pyplot as plt
#bridge for kivy and matplotlib
from kivy.garden.matplotlib import FigureCanvasKivyAgg
#kivy imports
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout


#starting values for array -to be removed -and replaced with api stuff-
X =[1,2,3,4,5]
Y =[1,2,3,4,5]

plt.plot(X,Y)
#labels for matplot graph - should make namable so we can reuse-
plt.ylabel("Valur")
plt.xlabel("Months")


#this is main class which renders whole applicatio
class Graphcon(FloatLayout):
    
    def __init__(self,**kwargs):

        super().__init__(**kwargs)
        #calls BoxLayout id for the graph aka id graph
        self.graph = self.ids.graph

        #PLot matplot graph as kivy app
        self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        
        #Upadates graph every 0.8 seconds
        Clock.schedule_interval(self.updateGraph,0.8)

        self.numy = 3
        self.numx = 6
        
    #update function    
    def updateGraph(self,val):
        #appends new nums to list
        X.append(self.numx)
        Y.append(self.numy)

        #plot them on matplot graph -force color to be same through out-
        plt.plot(X,Y, color = "blue")

        #clears pervious matplot
        self.graph.clear_widgets()
        
        # adds updated graph
        self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        self.numx = self.numx + 1
        self.numy = self.numy + 1
#app
class graphitApp(App):

    def build(self):
        
        return Graphcon()

  
#needs to be callabe, so we save the app as a variable *important for kivy.clock to work*        
run = graphitApp().run()

