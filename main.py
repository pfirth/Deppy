from Interface import Interface
from Valve import Valve
from Pressure import Pressure
from threading import Thread

def Create_Thread(function,*args):
	New_Thread = Thread(target = function, args = (args))
	New_Thread.start()


#Opening Connections to Equipment
Valve = Valve('A')
Pressure = Pressure('B')


#Getting relevant labelxs/buttons out for Logic Use
class Int(Interface):
    def prnt(self):
        print 'sup'


Interface = Int()
Process_Container = Interface.Process_Container_Object
Vacuum_Button = Process_Container.Vacuum_Button_Object.Button
Gas_Button = Process_Container.Gas_Button_Object.Button

Close = Interface.close_toggle


#Binding the Process Buttons


#Reading the Pressure
def Read_Pressure():
    print Pressure.Get_Chamber_Pressure()
    print Pressure.Get_Plasma_Pressure()

#Opening and Closing the Vacuum Valve
def Valve_Open(instance):
    '''This function is bound to the Vacuum Toggle Button,
    If the state of the button is down, the valve opens, if
    it is up, the valve will close'''
    if instance.state == 'down':
        Valve.Open()
    else:
        Valve.Close()
Vacuum_Button.bind(on_press = Valve_Open) #Opens the Vacuum when pressed







Interface.run()

