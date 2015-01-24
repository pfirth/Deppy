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
from Viewer_Pop_up import Viewer
from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '600')


class Green_Set_Button(Widget):
    '''This Button class just sets the background to the desired images'''
    def __init__(self,Set_Label):
        self.B = BoxLayout()
        self.Set_Label = Set_Label

        self.Button = Button(allow_stretch = False,
                             keep_ratio = True)

        self.Pop = Viewer('PopupPlaceHold_9876',self.Button,self.Set_Label).build()
        self.Button.bind(on_press = lambda  widget: self.Pop.open())

    def build(self):
        self.B.add_widget(self.Button)
        return self.B

class Red_Read_Button(Button):
    '''This Button class just sets the background to the desired images'''
    #background_normal = 'Images/Red_Label.png'
    #background_down = 'Images/Red_Label.png'

class MFC_Read_Label(Widget):
    '''place holder'''
    def __init__(self):
        self.B = BoxLayout()
        self.L = Label(text = 'PlaceHolder', color = [0,0,0,1])

    def build(self):
        self.B.add_widget(self.L)
        return self.B

class Title(Widget):
    '''place holder'''
    def __init__(self):
        self.B = BoxLayout()
        self.L = Label(text = 'Title_Box', color = [1,0,0,1])

    def build(self):
        self.B.add_widget(self.L)
        return self.B

class MFC_Container(object):
    '''Class contains a box, containing agrid with the
    MFC labels and set point buttons'''
    def __init__(self):
        self.Container = BoxLayout(pos_hint = {'top':1},
                                   size_hint_x = 0.33, size_hint_y =  0.33)

        self.Grid = GridLayout(rows = 3, cols = 4, spacing = 5)

        self.MFC1_Label_Object = MFC_Read_Label()
        self.MFC2_Label_Object = MFC_Read_Label()
        self.MFC3_Label_Object = MFC_Read_Label()
        self.MFC1_Label = self.MFC1_Label_Object.build()
        self.MFC2_Label = self.MFC2_Label_Object.build()
        self.MFC3_Label = self.MFC3_Label_Object.build()

        self.MFC1_Read_Label_Object = MFC_Read_Label()
        self.MFC2_Read_Label_Object = MFC_Read_Label()
        self.MFC3_Read_Label_Object = MFC_Read_Label()
        self.MFC1_Read_Label = self.MFC1_Read_Label_Object.build()
        self.MFC2_Read_Label = self.MFC2_Read_Label_Object.build()
        self.MFC3_Read_Label = self.MFC3_Read_Label_Object.build()

        self.MFC1_Set_Label_Object = MFC_Read_Label()
        self.MFC2_Set_Label_Object = MFC_Read_Label()
        self.MFC3_Set_Label_Object = MFC_Read_Label()
        self.MFC1_Set_Label = self.MFC1_Set_Label_Object.build()
        self.MFC2_Set_Label = self.MFC2_Set_Label_Object.build()
        self.MFC3_Set_Label = self.MFC3_Set_Label_Object.build()

        self.MFC1_Button_Object  = Green_Set_Button(self.MFC1_Set_Label_Object.L)
        self.MFC2_Button_Object  = Green_Set_Button(self.MFC2_Set_Label_Object.L)
        self.MFC3_Button_Object  = Green_Set_Button(self.MFC3_Set_Label_Object.L)
        self.MFC1_Button = self.MFC1_Button_Object.build()
        self.MFC2_Button = self.MFC2_Button_Object.build()
        self.MFC3_Button = self.MFC3_Button_Object.build()

    def set_label_text(self,label,text):
        '''A method to access the text for the MFC labels'''
        if label == 'MFC1':
            self.MFC1_Read_Label_Object.L.text = text
        elif label == 'MFC2':
            self.MFC2_Read_Label_Object.L.text = text
        elif label == 'MFC3':
            self.MFC3_Read_Label_Object.L.text = text

    def build(self):
        '''Adds the different widgets (Buttons and Labels)
        to the grid and add the grid to the box'''

        self.Grid.add_widget(self.MFC1_Label)
        self.Grid.add_widget(self.MFC1_Read_Label)
        self.Grid.add_widget(self.MFC1_Set_Label)
        self.Grid.add_widget(self.MFC1_Button)

        self.Grid.add_widget(self.MFC2_Label)
        self.Grid.add_widget(self.MFC2_Read_Label)
        self.Grid.add_widget(self.MFC2_Set_Label)
        self.Grid.add_widget(self.MFC2_Button)

        self.Grid.add_widget(self.MFC3_Label)
        self.Grid.add_widget(self.MFC3_Read_Label)
        self.Grid.add_widget(self.MFC3_Set_Label)
        self.Grid.add_widget(self.MFC3_Button)

        self.Container.add_widget(self.Grid)
        return self.Container


class Generator_Container(object):
    '''a class containing a box for all of the generator
    set & reads'''

    def __init__(self):
        self.Container = BoxLayout(pos_hint = {'top':0.66},
                           size_hint_x = 0.33, size_hint_y =  0.33)

        self.Grid = GridLayout(rows = 2, cols = 3, spacing = 5)

        #Title (Label)
        self.Set_Title_Object = Title()
        self.Set_Title = self.Set_Title_Object.build()
        self.Read_Title_Object = Title()
        self.Read_Title = self.Read_Title_Object.build()
        self.Reflected_Title_Object = Title()
        self.Reflected_Title = self.Reflected_Title_Object.build()
        #Title (Label)

        #Values(Label)
        self.Read_Label_Object = MFC_Read_Label()
        self.Read_Label = self.Read_Label_Object.build()
        self.Reflected_Label_Object = MFC_Read_Label()
        self.Reflected_Label = self.Reflected_Label_Object.build()
        self.Set_Button_Object = Green_Set_Button(self.Read_Label)
        self.Set_Button = self.Set_Button_Object.build()

    def build(self):
        self.Grid.add_widget(self.Read_Title)
        self.Grid.add_widget(self.Reflected_Title)
        self.Grid.add_widget(self.Set_Title)
        self.Grid.add_widget(self.Read_Label)
        self.Grid.add_widget(self.Reflected_Label)
        self.Grid.add_widget(self.Set_Button)

        self.Container.add_widget(self.Grid)
        return self.Container


class Interface(App):
    F = FloatLayout()
    Background_Picture = Image(source = 'Images/Background.jpg',
                         keep_ratio=False,allow_stretch=True)
    Background_Box = BoxLayout()

    MFC_Grid_Object = MFC_Container()
    MFC_Grid = MFC_Grid_Object.build()

    Generator_Container_Object = Generator_Container()
    Generator_Container = Generator_Container_Object.build()


    def build(self):
        self.F.add_widget(self.Background_Picture)
        self.F.add_widget(self.Background_Box)
        self.F.add_widget(self.MFC_Grid)
        self.F.add_widget(self.Generator_Container)

        return self.F


if __name__ =='__main__':
    Interface().run()





