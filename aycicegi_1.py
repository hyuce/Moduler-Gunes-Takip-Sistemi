import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#A1=4, A2=17, B1=27, B2=22
stepPinler1 = [4, 17, 27, 22]
#A1=6, A2=13, B1=19, B2=26
stepPinler2 = [6, 13, 19, 26]
#Enable pin
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 1)

sure = 10
adim = 100

for pin in stepPinler1:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
for pin in stepPinler2:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)    

ileri = [[0,0,0,1],
        [0,1,0,0],
        [0,0,1,0],
        [1,0,0,0]]

geri = [[1,0,0,0],
        [0,0,1,0],
        [0,1,0,0],
        [0,0,0,1]]

def ileri_don(sure, adim):
    for i in range(0,adim):
        for j in range(0,4):
            if (a==1):
                setStep1(ileri[j][0], ileri[j][1], ileri[j][2], ileri[j][3])
                time.sleep(sure)
            if (a==2):
                setStep2(ileri[j][0], ileri[j][1], ileri[j][2], ileri[j][3])
                time.sleep(sure)
                
def geri_don(sure,adim):
    for i in range(0,adim):
        for j in range(0,4):
            if (a==1):
                setStep1(geri[j][0], geri[j][1], geri[j][2], geri[j][3])
                time.sleep(sure)
            if (a==2):
                setStep2(geri[j][0], geri[j][1], geri[j][2], geri[j][3])
                time.sleep(sure)

def setStep1(p1, p2, p3, p4):
    GPIO.output(4, p1)
    GPIO.output(17, p2)
    GPIO.output(27, p3)
    GPIO.output(22, p4)

def setStep2(p5, p6, p7, p8):
    GPIO.output(6, p5)
    GPIO.output(13, p6)
    GPIO.output(19, p7)
    GPIO.output(26, p8)

    
def RCtime(RCpin):
    reading=0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(1)

    GPIO.setup(RCpin, GPIO.IN)
    while(GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading

def kar(ldr_pin):
    if(RCtime(ldr_pin) < 30):
        return 1
    if(RCtime(ldr_pin) >= 30 and RCtime(ldr_pin) < 60):
        return 2
    if(RCtime(ldr_pin) >= 60 and RCtime(ldr_pin) < 90):
        return 3
    if(RCtime(ldr_pin) >= 90 and RCtime(ldr_pin) < 120):
        return 4
    if(RCtime(ldr_pin) >= 120 and RCtime(ldr_pin) < 150):
        return 5
    if(RCtime(ldr_pin) >= 150):
        return 6

    

while True:
    k1 = kar(2)
    k2 = kar(3)
    k3 = kar(20)
    k4 = kar(21)
    
    if(k1 < k2):
        a=1
        ileri_don(int(sure)/1000.0, int(adim))
        
    if(k1 > k2):
        a=1
        geri_don(int(sure)/1000.0, int(adim))
       
    if(k3 < k4):
        a=2
        ileri_don(int(sure)/1000.0, int(adim))
       
    if(k3 > k4):
        a=2
        geri_don(int(sure)/1000.0, int(adim))
          









            
