from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivy.metrics import dp

class SwipeCard(BoxLayout):
    swipe_threshold = dp(100)
    start_x = NumericProperty(0)
    content = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.start_x = touch.x
            return True
        return super().on_touch_down(touch)
    
    def on_touch_move(self, touch):
        if self.start_x:
            delta_x = touch.x - self.start_x
            self.x = self.parent.x + delta_x
            self.update_card_opacity(delta_x)
            return True
        return super().on_touch_move(touch)
    
    def on_touch_up(self, touch):
        if self.start_x:
            delta_x = touch.x - self.start_x
            if abs(delta_x) > self.swipe_threshold:
                direction = 'right' if delta_x > 0 else 'left'
                self.complete_swipe(direction)
            else:
                self.return_to_center()
            self.start_x = 0
            return True
        return super().on_touch_up(touch)
    
    def update_card_opacity(self, delta_x):
        # Change opacity based on swipe distance
        self.opacity = max(0.5, 1 - abs(delta_x) / (2 * self.swipe_threshold))
    
    def complete_swipe(self, direction):
        target_x = self.parent.width if direction == 'right' else -self.width
        anim = Animation(x=target_x, duration=0.2)
        anim.bind(on_complete=lambda *args: self.parent.handle_swipe(direction))
        anim.start(self)
    
    def return_to_center(self):
        anim = Animation(x=self.parent.x, duration=0.2)
        anim.start(self)