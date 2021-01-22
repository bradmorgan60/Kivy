import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyAnchor(AnchorLayout):
    def __init__(self, **kwargs):
        super(MyAnchor, self).__init__(**kwargs)

        self.add_widget = AnchorLayout(
        anchor_x='right', anchor_y='bottom')
        btn = Button(text='Hello World')
        self.add_widget(btn)


class MyApp(App):
    def build(self):
        return MyAnchor()
    

if __name__ == "__main__":
    MyApp().run()
    






