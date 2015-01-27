from Interface import Interface
from Valve import Valve
from Pressure import Pressure
from MFC import MFC
from Chuck import Chuck
from threading import Thread
import time

'''
* Need to add in a start-up routine where the states of all the different components are
checked

* Also need a shut down procedure
'''


def Create_Thread(function,*args):
	New_Thread = Thread(target = function, args = (args))
	New_Thread.start()


#Getting relevant labelxs/buttons out for Logic Use
class Int(Interface):
    '''Inherits structure from the interface class, adds logic
    and functionality.'''
    def prnt(self,instance):
        print 'sup\n\n\n\n\n\n'

    def Bind(self):
        '''This function goes through each button in the
        interface and binds functions to their actions'''
        Motion = self.Motion_Control_Object

        self.Process_Container_Object.Vacuum_Button_Object.Button.bind(on_press = self.Valve_Open)
        self.Process_Container_Object.Move_Button_Object.Button.bind(on_press = lambda widget: Create_Thread(self.Move,
                                                            self.Process_Container_Object.Move_Button_Object.Button))
        self.Parameter_Object.MFC1_Read_Label_Object.L.text = 'Hello'

        Motion.Home_Button_Object.Button.bind(on_press = lambda widget: Create_Thread(Chuck.Home,))
        Motion.Ellipsometer_Button_Object.Button.bind(on_press = lambda  widget: Create_Thread(Chuck.Move,'2'))
        Motion.Nozzle_Button_Object.Button.bind(on_press = lambda  widget: Create_Thread(Chuck.Move,'3'))

    def Valve_Open(self,instance):
        '''This function is bound to the Vacuum Toggle Button,
        If the state of the button is down, the valve opens, if
        it is up, the valve will close'''
        if instance.state == 'down':
            Valve.Open()
        else:
            '''When the button is placed back into it's normal position,
            it also turns off the gasses and returns the Gass_Button to it's
            normal state'''
            self.Process_Container_Object.Gas_Button_Object.Button.state = 'normal'
            time.sleep(0.5)#Small break allows gasses to be pumped out
            Valve.Close()

    def Start_Set_Pressure(self):
        Create_Thread(self.Set_Pressure,self.Parameter_Object.Pressure_Set_Object.Button)

    def Set_Pressure(self,instance):
        '''Sends a string to the gate valve telling it to control the pressure'''
        temp = 'Off'
        Set_Temp = instance.text
        while self.close_toggle.state == 'normal':
            if self.Process_Container_Object.Gas_Button_Object.Button.state == 'down' and temp == 'Off':
                Valve.Set_Pressure(float(instance.text))
                Set_Temp = instance.text
                temp = 'On'
            if self.Process_Container_Object.Gas_Button_Object.Button.state == 'normal' and temp == 'On':
                Valve.Open()
                temp = 'Off'

            if instance.text != Set_Temp:
                temp = 'Off'

            time.sleep(0.2)

    def Start_Pressure_Read(self):
        '''This function creates a thread that will monitor
        the readings from the MKS pressure sensor'''
        Create_Thread(self.Read_Pressure,)

    def Move(self,instance):
        print instance.state
        for i in range(3):
            if i%2 == 0:
                Chuck.Move('2')
            else:
                Chuck.Move('3')
            if instance.state == 'normal':
                break
        instance.state = 'normal'


    def Read_Pressure(self):
        '''This function continually reads the pressure from the MKS
        sensor and updates the text on the pressure labels. When the app
        closes (close_toggle.state == 'down') the loop ends'''
        while self.close_toggle.state == 'normal':
            self.Parameter_Object.Pressure_Read_Object.L.text = Pressure.Get_Chamber_Pressure()
            self.Parameter_Object.Pressure_Quartz_Object.L.text = Pressure.Get_Plasma_Pressure()
            time.sleep(0.3)

    def Gas_Start_Stop(self,instance):
        '''This function turns changes the MFC state from control (flowing)
        to closed (not flowing) when the Gas Control Button is pressed)'''
        if instance.state == 'normal':
            MFC.MFC_Close(1)
            MFC.MFC_Close(2)
            MFC.MFC_Close(3)

        else:
            MFC.MFC_Control(1)
            MFC.MFC_Control(2)
            MFC.MFC_Control(3)

    def Start_MFC_Control(self):
        Create_Thread(self.MFC_Control,)

    def MFC_Control(self): #This really needs to be better, something with ques, but I don't really know how
        '''This function deals with all things MFC. It is looking at the Gas button
        to determine the state of the MFC, turning it on and off as necessary. Constantly
        sending commands to get the MFC flowrate and updating the Read labels'''

        #The purpose of the temp variables to to keep uneccesary commands from being sent
        Temp_State = 'On'
        MFC1_Temp = self.Parameter_Object.MFC1_Button_Object.Button.text
        MFC2_Temp = self.Parameter_Object.MFC1_Button_Object.Button.text
        MFC3_Temp = self.Parameter_Object.MFC1_Button_Object.Button.text

        while self.close_toggle.state == 'normal':
            if self.Process_Container_Object.Gas_Button_Object.Button.state == 'normal' and Temp_State == 'On':
                MFC.MFC_Close(1)
                MFC.MFC_Close(2)
                MFC.MFC_Close(3)
                #Valve.Open() #Opens the valve to pump out the chamber when the gas is shut off
                Temp_State = 'Off'

            if self.Process_Container_Object.Gas_Button_Object.Button.state == 'down' and Temp_State == 'Off':

                MFC.MFC_Control(1)
                MFC.MFC_Control(2)
                MFC.MFC_Control(3)
                Temp_State = 'On'

            if self.Parameter_Object.MFC1_Button_Object.Button.text != MFC1_Temp:
                #MFC.Set_Flowrate(1,self.Parameter_Object.MFC1_Button_Object.Button.text)
                MFC1_Temp = self.Parameter_Object.MFC1_Button_Object.Button.text

            if self.Parameter_Object.MFC2_Button_Object.Button.text != MFC2_Temp:

                MFC.Set_Flowrate(2,self.Parameter_Object.MFC2_Button_Object.Button.text)
                MFC2_Temp = self.Parameter_Object.MFC2_Button_Object.Button.text

            if self.Parameter_Object.MFC3_Button_Object.Button.text != MFC3_Temp:
                MFC.Set_Flowrate(3,self.Parameter_Object.MFC3_Button_Object.Button.text)
                MFC3_Temp = self.Parameter_Object.MFC3_Button_Object.Button.text

            try: #Sometimes when another command is entered, the outputs get all jumbled up and an
                 #Indedx Errror is thrown. This just passes through it until the next iteration
                self.Parameter_Object.MFC1_Read_Label_Object.L.text = MFC.Get_Flowrate('1')
                self.Parameter_Object.MFC2_Read_Label_Object.L.text = MFC.Get_Flowrate('2')
                self.Parameter_Object.MFC3_Read_Label_Object.L.text = MFC.Get_Flowrate('3')
            except IndexError:
                pass

            time.sleep(0.1)


#Opening Connections to Equipment
Valve = Valve('A')
Pressure = Pressure('B')
MFC = MFC('C',1)
Chuck = Chuck('D')

def main():

    Interface = Int()
    Interface.Bind()
    Interface.Start_Pressure_Read()
    Interface.Start_MFC_Control()
    Interface.Start_Set_Pressure()

    Interface.run()


if __name__ == '__main__':
    main()
