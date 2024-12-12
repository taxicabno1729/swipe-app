from kivy.app import App
from kivy.lang import Builder
from swipe_container import SwipeContainer

Builder.load_string('''
<SwipeCard>:
    size_hint: 0.9, 0.8
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
    
    Label:
        text: str(root.content) if root.content else ''
        color: 0, 0, 0, 1
        size: root.size
        pos: root.pos
        text_size: self.size
        halign: 'center'
        valign: 'middle'
''')

class SwipeApp(App):
    def build(self):
        container = SwipeContainer()
        # Example content
        container.items = [
            "Swipe me left or right!",
            "Next item",
            "Another one",
            "Last item"
        ]
        return container

if __name__ == '__main__':
    SwipeApp().run() 