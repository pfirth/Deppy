from __future__ import division
import serial
import time

class Pressure():
    '''Note, this piece of equipment requires a Null Cable'''
    def __init__(self,port):
        '''Initialization reauires that the port number of the 4-port USB to serial
        adapter be input (A,B,C,D) to start. This will be changed to work with different
        computers'''
        self.connection = serial.Serial('/dev/tty.usbserial-FTXE353B'+port)

    def __Receive_Data(self,command):
        '''This sends a command to the baratron and returns a value if good, or -1 if
        a time out situation'''
        while True:
            self.connection.write(command + '\r')
            out = ''
            time.sleep(0.1)
            t = time.time()
            while self.connection.inWaiting() >0:
                out+=self.connection.read()
                if time.time()-t >30:
                    return -1
            return out

    def Get_Plasma_Pressure(self):
        return self.__Receive_Data('?AV1').strip()

    def Get_Chamber_Pressure(self):
        return self.__Receive_Data('?AV2').strip()


if __name__ == '__main__':
    Bar = Pressure('A')
    x = Bar.Get_Chamber_Pressure()
    print x

