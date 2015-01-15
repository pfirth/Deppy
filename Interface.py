import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.layout import Layout
from kivy.uix.checkbox import CheckBox
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.slider import Slider


from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '600')

class Green_Set_Button(Button):
    '''This Button class just sets the background to the desired images'''
    #background_normal = 'Images/Green_Label.png'
    #background_down = 'Images/Green_Label.png'

class Red_Read_Button(Button):
    '''This Button class just sets the background to the desired images'''
    #background_normal = 'Images/Red_Label.png'
    #background_down = 'Images/Red_Label.png'

class MFC_Read_Label(Label):
    text = '0'
    color = [0,0,0,1]

class Interface(App):
    F = FloatLayout()
    Background_Picture = Image(source = 'Images/Background.jpg',
                               keep_ratio=False,allow_stretch=True)
    Background_Box = BoxLayout()

    #The MFC Layout
    MFC_Box = BoxLayout(size_hint_x = 0.5, size_hint_y = 0.25, pos_hint = {'y':0.75,'x':0})
    MFC_Grid = GridLayout(cols = 3, rows = 3)

    #Labels for the MFCs
    He_Label = Label(text = 'Helium', color = [0,0,0,1])
    Silane_Label = Label(text = 'Silane', color = [0,0,0,1])
    Hydrogen_Label = Label(text = 'Hydrogen', color = [0,0,0,1])
    MFC_Grid.add_widget(He_Label)
    MFC_Grid.add_widget(Silane_Label)
    MFC_Grid.add_widget(Hydrogen_Label)

    #Green_Set_Button
    He_Set_Button = Green_Set_Button()
    Silane_Set_Button = Green_Set_Button()
    Hydrogen_Set_Button = Green_Set_Button()
    MFC_Grid.add_widget(He_Set_Button)
    MFC_Grid.add_widget(Silane_Set_Button)
    MFC_Grid.add_widget(Hydrogen_Set_Button)

    #Read Labels
    He_Read_Label = MFC_Read_Label()
    Silane_Read_Label = MFC_Read_Label()
    Hydrogen_Read_Label = MFC_Read_Label()
    MFC_Grid.add_widget(He_Read_Label)
    MFC_Grid.add_widget(Silane_Read_Label)
    MFC_Grid.add_widget(Hydrogen_Read_Label)


    MFC_Box.add_widget(MFC_Grid)

    Background_Box.add_widget(MFC_Box)

    def build(self):
        self.F.add_widget(self.Background_Picture)
        self.F.add_widget(self.Background_Box)

        return self.F


if __name__ =='__main__':
    Interface().run()





