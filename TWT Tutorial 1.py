import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):  # inheritance from GridLayout module
    def __init__(self, **kwargs):          # ** = infinite amount of key words, they will come in as a list
        super(MyGrid, self).__init__(**kwargs)     # calling the Grid Layout constructor, we get the properties of GridLayout bc of inheritance
        
        self.cols = 2   # number of columns
        self.add_widget(Label(text='First Name: '))  # add_widget is a part of the GridLayout module
        self.firstname = TextInput(multiline=False)  #
        self.add_widget(self.firstname)

        self.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


        # nothing happens when you click the button and we want to add it in the middle
        # perform a column span to make the button centered
        # create another grid layout inside the first grid layout, and add it to the other grid layout
        
        self.submit = Button(text='Submit', font_size=40)
        self.add_widget(self.submit)
        


class MyApp(App):
    def build(self):
        return MyGrid()

    

if __name__ == "__main__":
    MyApp().run()
