from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.base import EventLoop 
from functools import partial

from kivy.uix.floatlayout import FloatLayout


class testSimulateTouch(App):
    
    def simulateTouch(self, x, y, dt):
        
        coord = [x,  self.win.height - y]
        print(coord)
        self.win.dispatch(
            'on_mouse_down',
            coord[0], coord[1],
            'left', {}
        )
        self.win.dispatch(
            'on_mouse_up',
            coord[0], coord[1],
            'left', {}
        )
            
    def build(self):
        self.fl = FloatLayout()
        self.btn=Button(text="simulate Touch", size_hint=[None, None], pos_hint={"center_x":0.5, "center_y":0.5})
        self.fl.add_widget(self.btn)
        return self.fl
    
    def on_start(self, *args):
        self.win=EventLoop.window
        Clock.schedule_interval(partial(self.simulateTouch, self.win.width /2, self.win.height/2), 2.)
    
testSimulateTouch().run()