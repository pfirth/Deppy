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

    def Set_Text(self,txt):
        self.L.text = txt

    def build(self):
        self.B.add_widget(self.L)
        return self.B

class Process_Button(Widget):
    def __init__(self):
        self.B = BoxLayout()
        self.Button = ToggleButton(text = 'Process_Button', color = [1,0,0,1])

    def build(self):
        self.B.add_widget(self.Button)
        return self.B


class Process_Container():
    def __init__(self):
        self.Container = BoxLayout(pos_hint = {'x':0.335},
                         size_hint_x = 0.66, size_hint_y =  0.33)
        self.Grid = GridLayout(rows = 1, cols = 4)

        self.Vacuum_Button_Object = Process_Button()
        self.Vacuum_Button = self.Vacuum_Button_Object.build()
        self.Gas_Button_Object = Process_Button()
        self.Gas_Button = self.Gas_Button_Object.build()
        self.RF_Button_Object = Process_Button()
        self.RF_Button = self.RF_Button_Object.build()
        self.Move_Button_Object = Process_Button()
        self.Move_Button = self.Move_Button_Object.build()


    def build(self):
        self.Grid.add_widget(self.Vacuum_Button)
        self.Grid.add_widget(self.Gas_Button)
        self.Grid.add_widget(self.RF_Button)
        self.Grid.add_widget(self.Move_Button)

        self.Container.add_widget(self.Grid)
        return self.Container

class Parameter_Container(object):
    '''Class contains a box, containing agrid with the
    MFC labels and set point buttons'''
    def __init__(self):
        self.Container = BoxLayout(pos_hint = {'top':1},
                                   size_hint_x = 0.33, size_hint_y =  1)

        self.Grid = GridLayout(rows = 9, cols = 4, spacing = 5)

        #_______________________MFC_Labels/Buttons____________________________
        self.MFC_Gas_Title_Object = Title()
        self.MFC_Gas_Title = self.MFC_Gas_Title_Object.build()
        self.MFC_Set_Title_Object = Title()
        self.MFC_Set_Title = self.MFC_Set_Title_Object.build()
        self.MFC_Read_Title_Object = Title()
        self.MFC_Read_Title = self.MFC_Read_Title_Object.build()
        self.MFC_Space = Label()

        self.MFC1_Label_Object = Title()
        self.MFC2_Label_Object = Title()
        self.MFC3_Label_Object = Title()
        self.MFC1_Label = self.MFC1_Label_Object.build()
        self.MFC2_Label = self.MFC2_Label_Object.build()
        self.MFC3_Label = self.MFC3_Label_Object.build()

        self.MFC1_Label_Object.Set_Text('Silane')
        self.MFC2_Label_Object.Set_Text('Helium')
        self.MFC3_Label_Object.Set_Text('Hydrogen')

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

        #_______________________RF_Labels/Buttons____________________________

        #Title (Label)
        self.RF_Title_Object = Title()
        self.RF_Title = self.RF_Title_Object.build()
        self.RF_Set_Title_Object = Title()
        self.RF_Set_Title = self.RF_Set_Title_Object.build()
        self.RF_Read_Title_Object = Title()
        self.RF_Read_Title = self.RF_Read_Title_Object.build()
        self.RF_Reflected_Title_Object = Title()
        self.RF_Reflected_Title = self.RF_Reflected_Title_Object.build()
        #Title (Label)

        #Values(Label)
        self.RF_Space = Label() #This is just a place holder, will have no functionality
        self.RF_Read_Label_Object = MFC_Read_Label()
        self.RF_Read_Label = self.RF_Read_Label_Object.build()
        self.RF_Reflected_Label_Object = MFC_Read_Label()
        self.RF_Reflected_Label = self.RF_Reflected_Label_Object.build()
        self.RF_Set_Button_Object = Green_Set_Button(self.RF_Read_Label)
        self.RF_Set_Button = self.RF_Set_Button_Object.build()

        #_______________________Pressure_Labels/Buttons____________________________

        #Title (Label)
        self.Pressure_Title_Object = Title()
        self.Pressure_Title = self.Pressure_Title_Object.build()

        self.Pressure_Set_Title_Object = Title()
        self.Pressure_Set_Title = self.Pressure_Set_Title_Object.build()

        self.Pressure_Read_Title_Object = Title()
        self.Pressure_Read_Title = self.Pressure_Read_Title_Object.build()

        self.Pressure_Quartz_Title_Object = Title()
        self.Pressure_Quartz_Title = self.Pressure_Quartz_Title_Object.build()

        #Values(Label)
        self.Pressure_Space = Label() #This is just a place holder, will have no functionality

        self.Pressure_Set_Object = MFC_Read_Label()
        self.Pressure_Set = self.Pressure_Set_Object.build()

        self.Pressure_Read_Object = MFC_Read_Label()
        self.Pressure_Read = self.Pressure_Read_Object.build()

        self.Pressure_Quartz_Object = MFC_Read_Label()
        self.Pressure_Quartz = self.Pressure_Quartz_Object.build()



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

        #MFC Additions
        self.Grid.add_widget(self.MFC_Gas_Title)
        self.Grid.add_widget(self.MFC_Set_Title)
        self.Grid.add_widget(self.MFC_Read_Title)
        self.Grid.add_widget(self.MFC_Space)

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

        #RF Additions
        self.Grid.add_widget(self.RF_Title)
        self.Grid.add_widget(self.RF_Set_Title)
        self.Grid.add_widget(self.RF_Read_Title)
        self.Grid.add_widget(self.RF_Reflected_Title)
        self.Grid.add_widget(self.RF_Space)
        self.Grid.add_widget(self.RF_Read_Label)
        self.Grid.add_widget(self.RF_Reflected_Label)
        self.Grid.add_widget(self.RF_Set_Button)

        #Pressure Additions
        self.Grid.add_widget(self.Pressure_Title)
        self.Grid.add_widget(self.Pressure_Set_Title)
        self.Grid.add_widget(self.Pressure_Read_Title)
        self.Grid.add_widget(self.Pressure_Quartz_Title)
        self.Grid.add_widget(self.Pressure_Space)
        self.Grid.add_widget(self.Pressure_Set)
        self.Grid.add_widget(self.Pressure_Read)
        self.Grid.add_widget(self.Pressure_Quartz)

        self.Container.add_widget(self.Grid)
        return self.Container


class Generator_Container(object): #Thinking about getting rid of this
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

    Parameter_Object= Parameter_Container()
    Parameter_Grid = Parameter_Object.build()

    Process_Container_Object = Process_Container()
    Process_Container = Process_Container_Object.build()


    close_toggle = ToggleButton()

    def build(self):
        self.F.add_widget(self.Background_Picture)
        self.F.add_widget(self.Background_Box)
        self.F.add_widget(self.Parameter_Grid)
        self.F.add_widget(self.Process_Container)

        return self.F

    def on_stop(self):
        self.close_toggle.state = 'down'


if __name__ =='__main__':
    Interface().run()





