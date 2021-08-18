from machine import Pin
import time
Relay_1 =Pin(12,Pin.OUT)
Relay_2 =Pin(13,Pin.OUT)
Relay_3 =Pin(14,Pin.OUT)
Relay_4 =Pin(15,Pin.OUT)
button_1 = Pin(16,Pin.IN,Pin.PULL_DOWN)# connect pushbutton in between GPIO and VCC
button_2 = Pin(17,Pin.IN,Pin.PULL_DOWN)# connect pushbutton in between GPIO and VCC
button_3 = Pin(18,Pin.IN,Pin.PULL_DOWN)# connect pushbutton in between GPIO and VCC
button_4 = Pin(19,Pin.IN,Pin.PULL_DOWN)# connect pushbutton in between GPIO and VCC

def Relay1toggle(irq):
    global Relay
    Relay_1.toggle()
    print("button1 value is",button_1.value())
    
def Relay2toggle(irq):
    global Relay
    Relay_2.toggle()
    print("button2 value is",button_2.value())
    
def Relay3toggle(irq):
    global Relay
    Relay_3.toggle()
    print("button3 value is",button_3.value())
    
def Relay4toggle(irq):
    global Relay
    Relay_4.toggle()
    print("button4 value is",button_4.value())
    
button_1.irq(trigger = Pin.IRQ_RISING,handler =Relay1toggle)
button_2.irq(trigger = Pin.IRQ_RISING,handler =Relay2toggle)
button_3.irq(trigger = Pin.IRQ_RISING,handler =Relay3toggle)
button_4.irq(trigger = Pin.IRQ_RISING,handler =Relay4toggle)