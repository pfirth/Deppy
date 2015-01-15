from __future__ import division
import serial
import time

class Valve():

    def __init__(self,port):
        '''Initialization requires that the port number of the 4-port USB to serial
        adapter be input (A,B,C,D) to start. This will be changed to work with different
        computers.

        Interacting with a Vat Valve via the service port.
        '''
        self.connection = serial.Serial(port='/dev/tty.usbserial-FTXE353B'+ port,baudrate=38400,
                                        bytesize=serial.SEVENBITS,stopbits = serial.STOPBITS_ONE,
                                        parity=serial.PARITY_EVEN)

    def __Receive_Data(self,command):
        while True:
            self.connection.write('c:0100' + '\r\n') #Gives the user full command priveleges
            time.sleep(0.1) #Buffer time to accept the command
            self.connection.write(command + '\r\n')
            out = ''
            time.sleep(0.1)
            t = time.time()
            while self.connection.inWaiting() >0:
                incoming  = self.connection.read()
                out+=incoming
                if time.time()-t >30:
                    return -1
            return out

    def __Pressure_Conversion(self,P):
        '''converts a pressure in Torr to the appropriate ASII
        command'''''
        command = str(int(P*500000))
        for x in range(7-len(command)):
            command = '0'+command
        return 'S:0'+ command

    def Set_Pressure(self,Pressure):
        '''Sends the pressure setpoint to the valve'''
        command = self.__Pressure_Conversion(Pressure)
        self.__Receive_Data(command)

    def Open(self):
        '''This function sets the valve to it's fully open position'''
        self.__Receive_Data('O:')

    def Close(self):
        '''This function closes the valve'''
        self.__Receive_Data('C:')

    def Soft_Open(self):
        '''This function slowly opens the gate valve as to not cause
        any damage to critical parts of of the system'''
        x = -400
        step = 425 #Valve step size
        self.__Receive_Data('R:000050') #setting the initial position
        time.sleep(5)

        while x <= 12000:
            y = '0'
            x +=int(step)
            command = 'R:'+ (6 - len(str(x)))*y + str(x)
            self.__Receive_Data(command) #Stepping the valve open
            time.sleep(0.4) #break between command sets
        self.Open() #once the valve has been opened to position 12000, the valve fully opens


if __name__ == '__main__':
    X = Valve('A')

