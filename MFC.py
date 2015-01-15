from __future__ import division
import serial
import time



class MFC():

    def __init__(self,port,module):
        '''Initialization requires that the port number of the 4-port USB to serial
        adapter be input (A,B,C,D) to start. This will be changed to work with different
        computers.

        The module variable refers to the two separate modules on the hub (4 MFCs each)
        a value of 1 refers to the control system for Deppy and a value of 2 refers to
        the control system for Annie'''
        self.connection = serial.Serial('/dev/tty.usbserial-FTXE353B'+port)
        self.m = str(module)

    def __Receive_Data(self,command):
        while True:
            self.connection.write(command + '\n')
            out = ''
            time.sleep(0.1)
            t = time.time()
            while self.connection.inWaiting() >0:
                incoming  = self.connection.read()
                out+=incoming
                if time.time()-t >30:
                    return -1
            return out

    def Get_Flowrate(self,Port):
        '''The command $BR<module>:<MFC Port> is used to get the string containing
        the flowrate of the MFC at <MFC Port>'''
        print '$BR'+self.m+':'+ Port

        ret = self.__Receive_Data('$BR'+self.m+':'+ Port).split(':')[2]
        return ret

    def Set_Flowrate(self,Port,Flowrate):
        '''The command $AW<module>:<MFC Port>:<Flowrate> is used to set the
        flowrate.'''
        set_flow_command = '$AW' + self.m + ':'+ str(Port) + ':' + str(Flowrate)
        self.__Receive_Data(set_flow_command)

    def MFC_Control(self,Port):
        '''This function sends the command to put the MFC into control
        mode, essentially opening the valve'''
        open_command = '$IW' + self.m + ':' +str(Port) + ':' + '1'
        self.__Receive_Data(open_command)

    def MFC_Off(self,Port):
        '''This function takes the MFC out of control mode and turns it off'''
        command = '$IW' + self.m + ':' +str(Port) + ':' + '0'
        self.__Receive_Data(command)

    def MFC_Close(self,Port):
        '''this function closes the MFC valve'''
        command = '$IW' + self.m + ':' +str(Port) + ':' + '3'
        self.__Receive_Data(command)


if __name__ == '__main__':
    X = MFC('A',2)

    #print X. Get_Flowrate('3')
    print X.Set_Flowrate('3','10.34')