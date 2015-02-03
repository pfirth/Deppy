import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
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




Config.set('graphics', 'width', '1350')
Config.set('graphics', 'height', '700')

class Motion_button(Button):
    def __init__(self):
        self.Button = ToggleButton(background_down = 'Images/Position_Down.png',
                                   background_normal = 'Images/Position_Normal.png')
        self.Button.border = [0,0,0,0]
    def Build(self):
        return self.Button

class Motion_Control_Menu(Widget):
    def __init__(self):
        self.B = BoxLayout(pos_hint = {'x':0.665,'y':0.74},
                         size_hint_x = 0.33, size_hint_y =  0.25)

        self.F = RelativeLayout(rows = 1, cols  =1)
        self.G = GridLayout(rows = 1, cols = 5)

        self.Deppy = Image(source = 'Images/Deppy.png', keep_ratio=False,allow_stretch=True)

        self.Home_Button_Object =Motion_button()
        self.Home_Button = self.Home_Button_Object.Build()

        self.Ellipsometer_Button_Object =Motion_button()
        self.Ellipsometer_Button = self.Ellipsometer_Button_Object.Build()

        self.Pre_Nozzle_Button_Object =Motion_button()
        self.Pre_Nozzle_Button = self.Pre_Nozzle_Button_Object.Build()

        self.Nozzle_Button_Object =Motion_button()
        self.Nozzle_Button = self.Nozzle_Button_Object.Build()

        self.Glove_Button_Object =Motion_button()
        self.Glove_Button = self.Glove_Button_Object.Build()


    def build(self):
        self.G.add_widget(self.Home_Button)
        self.G.add_widget(self.Ellipsometer_Button)
        self.G.add_widget(self.Pre_Nozzle_Button)
        self.G.add_widget(self.Nozzle_Button)
        self.G.add_widget(self.Glove_Button)

        self.F.add_widget(self.Deppy)
        self.F.add_widget(self.G)

        self.B.add_widget(self.F)
        return self.B

class Green_Set_Button(Widget):
    '''This Button class just sets the background to the desired images'''
    def __init__(self,Set_Label):
        self.B = BoxLayout()
        self.Set_Label = Set_Label

        self.Button = Button(allow_stretch = False,
                             keep_ratio = True,text ='0', background_normal = 'Images/Blue_Label.png',
                             border = [0,0,0,0])

        self.Pop = Viewer('PopupPlaceHold_9876',self.Button,self.Button).build()
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

        self.L = Button(text = '0', color = [0,0,0,1], background_down = 'Images/Green_Label.png',
                        background_normal = 'Images/Green_Label.png', border = [0,0,0,0])


    def Set_Text(self,Txt):
        self.L.text = Txt

    def build(self):
        self.B.add_widget(self.L)
        return self.B

class Title(Widget):
    '''place holder'''
    def __init__(self):
        self.B = BoxLayout()
        self.L = Button(text = 'Title_Box', color = [0,0,0,1], background_down = 'Images/Title.png',
                        background_normal = 'Images/Title.png', border = [0,0,0,0])

    def Set_Text(self,txt):
        self.L.text = txt

    def build(self):
        self.B.add_widget(self.L)
        return self.B

class Process_Button(Widget):
    def __init__(self):
        self.B = BoxLayout()
        self.Button = ToggleButton(text = 'Process_Toggle_Button', color = [0,0,0,1],
                                   background_normal = 'Images/Start_Button.png',
                                   background_down = 'Images/Start_Button_Down.png')
        self.Button.border = [0,0,0,0]

    def Set_Text(self,txt):
        self.Button.text = txt

    def build(self):
        self.B.add_widget(self.Button)
        return self.B



class Process_Container():
    def __init__(self):
        self.Container = BoxLayout(pos_hint = {'x':0.335,'y':0.01},
                         size_hint_x = 0.66, size_hint_y =  0.33)
        self.Grid = GridLayout(rows = 1, cols = 4, spacing = 5)

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
        self.Container = BoxLayout(pos_hint = {'top':1,'x':0.005},
                                   size_hint_x = 0.32, size_hint_y =  1)

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

        self.Pressure_Set_Object = Green_Set_Button(self.Pressure_Space)
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
        self.Grid.add_widget(self.MFC1_Button)
        self.Grid.add_widget(self.MFC1_Read_Label)
        self.Grid.add_widget(self.MFC1_Set_Label)

        self.Grid.add_widget(self.MFC2_Label)
        self.Grid.add_widget(self.MFC2_Button)
        self.Grid.add_widget(self.MFC2_Read_Label)
        self.Grid.add_widget(self.MFC2_Set_Label)

        self.Grid.add_widget(self.MFC3_Label)
        self.Grid.add_widget(self.MFC3_Button)
        self.Grid.add_widget(self.MFC3_Read_Label)
        self.Grid.add_widget(self.MFC3_Set_Label)


        #RF Additions
        self.Grid.add_widget(self.RF_Title)
        self.Grid.add_widget(self.RF_Set_Title)
        self.Grid.add_widget(self.RF_Read_Title)
        self.Grid.add_widget(self.RF_Reflected_Title)
        self.Grid.add_widget(self.RF_Space)
        self.Grid.add_widget(self.RF_Set_Button)
        self.Grid.add_widget(self.RF_Read_Label)
        self.Grid.add_widget(self.RF_Reflected_Label)

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

class Chuck_Properties(object):
    def __init__(self):
        self.B = BoxLayout(pos_hint = {'x':0.665,'y':0.41},
                 size_hint_x = 0.33, size_hint_y =  0.25)
        self.G = GridLayout(rows = 2, cols = 4,spacing = 5)


        self.Loop_Label_Object = Title()
        self.Loop_Label = self.Loop_Label_Object.build()
        self.Speed_Label_Object = Title()
        self.Speed_Label = self.Speed_Label_Object.build()
        self.Zpos_Label_Object = Title()
        self.Zpos_Label = self.Zpos_Label_Object.build()
        self.Nozzle_Label_Object = Title()
        self.Nozzle_Label = self.Nozzle_Label_Object.build()

        self.Loop_Button_Object = Green_Set_Button(Label())
        self.Loop_Button = self.Loop_Button_Object.build()
        self.Speed_Button_Object =Green_Set_Button(Label())
        self.Speed_Button = self.Speed_Button_Object.build()
        self.Zpos_Button_Object = Green_Set_Button(Label())
        self.Zpos_Button = self.Zpos_Button_Object.build()
        self.Nozzle_Button_Object = Green_Set_Button(Label())
        self.Nozzle_Button = self.Nozzle_Button_Object.build()

        self.Loop_Label_Object.Set_Text('# of Loops')
        self.Speed_Label_Object.Set_Text('Speed\n(mm/s)')
        self.Zpos_Label_Object.Set_Text('Z Position')
        self.Nozzle_Label_Object.Set_Text('Nozzle\nWidth')

    def build(self):
        self.G.add_widget(self.Loop_Label)
        self.G.add_widget(self.Speed_Label)
        self.G.add_widget(self.Zpos_Label)
        self.G.add_widget(self.Nozzle_Label)
        self.G.add_widget(self.Loop_Button)
        self.G.add_widget(self.Speed_Button)
        self.G.add_widget(self.Zpos_Button)
        self.G.add_widget(self.Nozzle_Button)

        self.B.add_widget(self.G)
        return self.B





class Interface(App):
    F = FloatLayout()
    Background_Picture = Image(source = 'Images/Background.jpg',
                         keep_ratio=False,allow_stretch=True)
    Background_Box = BoxLayout()

    Parameter_Object= Parameter_Container()
    Parameter_Grid = Parameter_Object.build()

    Process_Container_Object = Process_Container()
    Process_Container = Process_Container_Object.build()

    Motion_Control_Object = Motion_Control_Menu()
    Motion_Control = Motion_Control_Object.build()

    Chuck_Properties_Object = Chuck_Properties()
    Chuck_Properties = Chuck_Properties_Object.build()

    close_toggle = ToggleButton()

    def build(self):
        self.F.add_widget(self.Background_Picture)
        self.F.add_widget(self.Background_Box)
        self.F.add_widget(self.Parameter_Grid)
        self.F.add_widget(self.Process_Container)
        self.F.add_widget(self.Motion_Control)
        self.F.add_widget(self.Chuck_Properties)

        return self.F

    def on_stop(self):
        self.close_toggle.state = 'down'


if __name__ =='__main__':
    Interface().run()





