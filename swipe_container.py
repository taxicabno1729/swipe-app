from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from swipe_card import SwipeCard
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp

class SwipeContainer(BoxLayout):
    items = ListProperty([])
    current_index = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            Rectangle(pos=self.pos, size=self.size)
        self.show_current_card()
    
    def show_current_card(self):
        self.clear_widgets()
        if self.current_index < len(self.items):
            card = SwipeCard()
            card.content = self.items[self.current_index]
            self.add_widget(card)
    
    def handle_swipe(self, direction):
        self.current_index += 1
        self.show_current_card() 