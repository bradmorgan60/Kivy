import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):  # inheritance from GridLayout module
    def __init__(self, **kwargs):          # ** = infinite amount of key words, they will come in as a list
        super(MyGrid, self).__init__(**kwargs)     # calling the Grid Layout constructor, we get the properties of GridLayout bc of inheritance
        self.cols = 1

        self.inside = GridLayout()   # this new Grid Layout contains everything below
        self.inside.cols = 2

        self.inside.add_widget(Label(text='First Name: '))  # add_widget is a part of the GridLayout module
        self.firstname = TextInput(multiline=False)  #
        self.inside.add_widget(self.firstname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)


        # nothing happens when you click the button and we want to add it in the middle
        # perform a column span to make the button centered
        # create another grid layout inside the first grid layout, and add it to the other grid layout
        
        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    
    def pressed(self, instance):
        first = self.firstname.text 
        last = self.lastname.text 
        email = self.email.text

        print("First Name: ", first, "Last name: ", last, "Email: ", email)
        # now, let's be able to clear the information out of the box when we hit 'submit'
        self.firstname.text = ""
        self.lastname.text = ""
        self.email.text = ""
           
        


class MyApp(App):
    def build(self):
        return MyGrid()

    

if __name__ == "__main__":
    MyApp().run()
