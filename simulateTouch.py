from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.input.providers.mouse import MouseMotionEvent 
from kivy.input.factory import MotionEventFactory
from kivy.base import EventLoop 

from kivy.uix.floatlayout import FloatLayout


class testSimulateTouch(App):
    
    def simulateTouch(self, dt):
        win=EventLoop.window
        coord = [win.width/2,  win.height - (win.height/2)]
        print(coord)
        win.dispatch(
            'on_mouse_down',
            coord[0], coord[1],
            'left', {}
        )
        win.dispatch(
            'on_mouse_up',
            coord[0], coord[1],
            'left', {}
        )
    
    def inspect(self, *args):
        print(args)
        
    
    def build(self):
        print(MotionEventFactory.list())
        Clock.schedule_interval(self.simulateTouch, 2.)
        self.fl = FloatLayout()
        self.btn=Button(text="simulate Touch", size_hint=[None, None], pos_hint={"center_x":0.5, "center_y":0.5})
        self.btn.bind(on_touch_down=self.inspect)
        self.fl.add_widget(self.btn)
        return self.fl
    
testSimulateTouch().run()