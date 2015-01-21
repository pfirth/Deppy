from __future__ import division
import serial
import time



class Seren_R301():

    def __init__(self,port):
        '''Initialization requires that the port number of the 4-port USB to serial
        adapter be input (A,B,C,D) to start. This will be changed to work with different
        computers.'''

        self.connection = serial.Serial('/dev/tty.usbserial-FTXE353B'+port)

    def Receive_Data(self,command):
        while True:
            self.connection.write(command + '\r\n')
            out = ''
            time.sleep(0.1)
            t = time.time()
            while self.connection.inWaiting() >0:
                incoming  = self.connection.read()
                out+=incoming
                print out
                if time.time()-t >30:
                    return -1
            return out

if __name__=='__main__':
    X = Seren_R301('A')
    print X.Receive_Data('Q')