from __future__ import division
import serial
import time
import re

class Chuck():

    def __init__(self,port):
        '''Initialization reauires that the port number of the 4-port USB to serial
        adapter be input (A,B,C,D) to start. This will be changed to work with different
        computers'''
        self.Busy = False
        self.connection = serial.Serial('/dev/tty.usbserial-FTXE353B'+port)
        self.XPOS = self.Get_XPOS() #X position
        self.ZPOS = self.Get_ZPOS() #Z position
        self.VMX = self.Get_X_Speed() #X speed


    def __Busy(self):
        '''If a command is being performed, the variable
        'Busy' is set to True. If another command is issued, the command is
        queued until the previous command sets 'Busy' to False.'''
        while self.Busy:
            time.sleep(0.1)

    def __Send_Command(self,command):
        while True:
            self.connection.write(command + '\r')
            out = ''
            time.sleep(0.1)
            t = time.time()
            while True:
                #if the time to make an individual move is greater than
                #The break time here is changed to 30 seconds since the home move is very slow
                #If the function times out, it returns a -1
                if time.time()-t >30:
                    self.Busy = False
                    return -1
                out+=self.connection.read()
                #Checks the last 4 characters
                finished = out[len(out)-4:len(out)]
                #if the last 4 characters are DONE, then the move has completed
                #successfully and the loop ends and returns 0
                if finished == 'DONE':
                    self.Busy = False
                    return 0
            self.Busy = False
            break


    def __Receive_Data(self,command):
        '''This is specifically used to query the position of the chuck in the
        x an z directions. Data is returned in the format Command\r\nPosition\r\n.
        This function returns the poition in the form of a string'''
        while True:
            self.connection.write(command + '\r')
            out = ''
            time.sleep(0.1)
            t = time.time()
            while self.connection.inWaiting() >0:
                out+=self.connection.read()
                if time.time()-t >30:
                    self.Busy = False
                    return -1
            x = re.findall(r'\d+\.\d+',out)[0] #finds all the return value with the float
            self.Busy = False
            return x

    def Move(self,position):
        '''This function moves the chuck in the x direction. The input is either
        1,2,3 or E as strings.'''
        self.__Busy()
        self.Busy = True
        x = self.__Send_Command('M_X'+position) #Initial Move
        self.XPOS = self.Get_XPOS() #Update the x Position
        return x #return status

    def Get_XPOS(self):
        '''This function returns the current x position'''
        self.__Busy()
        self.Busy = True
        return self.__Receive_Data('PRINT1 XPOS')

    def Set_X_Speed(self,speed):
        '''This function changes the peak velocity of the chuck'''
        self.__Busy()
        self.Busy = True
        x = self.__Receive_Data('VMX=' + speed)
        self.VMX = self.Get_X_Speed()
        return x

    def Get_X_Speed(self):
        '''Returns the current x-axis speed'''
        self.__Busy()
        self.Busy = True
        return self.__Receive_Data('PRINT1 VMX')

    def Home(self):
        '''This function homes the chuck'''
        self.__Busy()
        self.Busy = True
        x = self.__Send_Command('HMAL')
        self.XPOS = self.Get_XPOS()
        self.ZPOS = self.Get_ZPOS()
        return x

    def Get_ZPOS(self):
        '''This function returns the Z position'''
        self.__Busy()
        self.Busy = True
        return self.__Receive_Data('PRINT1 ZPOS')

    def Move_Z(self,position):
        '''This function moves the z-axis. Can be moved in one of two poitions up and
        down. The inputs are string values U and D'''
        self.__Busy()
        self.Busy = True
        x = self.__Send_Command('M_Z'+position)
        self.ZPOS = self.Get_ZPOS()
        return x

    def Set_ZUP(self,position):
        '''Sets the top Z Position'''
        self.__Busy()
        self.Busy = True
        return self.__Receive_Data('ZU='+position)

    def Set_ZDOWN(self,position):
        '''Sets the bottom Z position'''
        self.__Busy()
        self.Busy = True
        return self.__Receive_Data('ZD='+position)

    def Home_Z(self):
        '''Returns the Z-axis to home'''
        self.__Busy()
        self.Busy = True
        x = self.__Send_Command('HMZ')
        self.ZPOS = self.Get_ZPOS()
        return x

if __name__ == '__main__':
    chk = Chuck('A')













