import serial

ser = serial.Serial("/dev/ttyACM0",9600)
ser.flushInput()
     
class MSSensor :
        PIN1=1
        PIN3=3
        PIN5=5
        
        def __init__(self):
                print("[MSSensor] init\n")

        def __init__(self, val):
                self.rawValue = [[0]*2 for i in range(3)]
                print((self.rawValue))
                self.limitDistance=0
                self.setLimitDistance(val)

        def setLimitDistance(self, value):
                self.limitDistance = value

        # get Distance from arduino ser
        def getDistance(self):
                self.readings = []
                ser.flushInput()
                input_pin1 = ser.readline()
                input_pin3 = ser.readline()
                input_pin5 = ser.readline()
                self.rawValue[0] = input_pin1.split()
                self.rawValue[1] = input_pin3.split()
                self.rawValue[2] = input_pin5.split()
                
                if len(self.rawValue[0]) <= 1:
                        print("[MSSensor] err : cannot get values from sensor 1");
                        print(self.rawValue[0])
                        self.rawValue[0] = [0,0]
                        self.rawValue[0][0] = 1
                        self.rawValue[0][1] = 33
                elif len(self.rawValue[1]) <= 1:
                        print("[MSSensor] err : cannot get values from sensor 3");
                        self.rawValue[1] = [0,0]
                        self.rawValue[1][0] = 3
                        self.rawValue[1][1] = 33
                elif len(self.rawValue[2]) <= 1:
                        print("[MSSensor] err : cannot get values from sensor 5");
                        self.rawValue[2] = [0,0]
                        self.rawValue[2][0] = 5
                        self.rawValue[2][1] = 33
               # print("[MSSensor] Sensor PIN 1 "+self.rawValue[0][0]+" : "+self.rawValue[0][1]+"cm \n")
               # print("[MSSensor] Sensor PIN 3 "+self.rawValue[1][0]+" : "+self.rawValue[1][1]+"cm \n")
               # print("[MSSensor] Sensor PIN 5 "+self.rawValue[2][0]+" : "+self.rawValue[2][1]+"cm \n")
                ser.flushInput()
                
                self.readings.append(int(self.rawValue[0][1]))
                self.readings.append(int(self.rawValue[1][1]))
                self.readings.append(int(self.rawValue[2][1]))

                return self.readings

        # checking Agent is closed to something.,.,.,., 
        def checkDistance(self):
                value=0
                pin=0
                
                try:
                        pin=int(self.rawValue[0][0])
                        pin=int(self.rawValue[1][0])
                        pin=int(self.rawValue[2][0])                        
                        value=int(self.rawValue[0][1])
                        value=int(self.rawValue[1][1])
                        value=int(self.rawValue[2][1])                        
                
                except IndexError as err:
                        print("[MSSensor] index err -1 err\n")
                        return -1

                # [0,0,0] : no danger
                # [1,1,1] : danger in all of side
                flag = [0 for i in range(6)]

                for checkPin in self.rawValue:
                        print("@@@@@@@@")
                        print(checkPin)
                        print(flag)
                        if int(checkPin[1]) < self.limitDistance:
                                flag[int(checkPin[0])]=1
                        else:
                                flag[int(checkPin[0])]=0
                return flag

        
'''
                        
                        if pin==MSSensor.PIN1:
                                print("[MSSensor] pinNum1 Danger!\n")
                                return MSSensor.PIN1
                        elif pin==MSSensor.PIN3:
                                print("[MSSensor] pinNum3 Danger!\n")
                                return MSSensor.PIN3
                        elif pin==MSSensor.PIN5:
                                print("[MSSensor] pinNum5 Danger!\n")
                                return MSSensor.PIN5
                        else:
                                print("[MSSensor] err\n")
                                return -1
                else:
                        return 0
'''
