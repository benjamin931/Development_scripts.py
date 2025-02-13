# Import the necessary modules
from machine import Pin
from utime import sleep

# Define the LED pins (GPIO 0 through GPIO 6
led_pins = [Pin(i, Pin.OUT) for i in range(0, 7)]
led_num = #This is the line that I am going to fix. I need to create a variable that is = "i" so that i can call on it in the functions.

button_pin = Pin(19, Pin.IN, Pin.PULL_UP) #Create object "button_pin" and assign it to GP 19
button1_pin = Pin(20, Pin.IN, Pin.PULL_UP)  #Create object "button1_pin" and assign it to GP 19

def seq_left(): #Create a function called "seq_left()"
    for i in range(6, -1, -1): #Start a counter that runs from GP 6 to GP 0
        for led in led_pins:
            led.value(0)      #Turn off all the LEDs
        led_pins[i].value(1) #Turn on the specific LED [i]
        if button1_pin.value() == 0: #If button1 is low:
            seq_right() #Call on the function "seq_right()"
        sleep(0.5) #Small delay before going back through the loop
    
def seq_right(): #Create a function called"seq_right()"
    for i in range(0, 7, 1): #Start a counter that runs from GP 0 to GP 6
        for led in led_pins: 
            led.value(0)       #Turn off all the LEDs
        led_pins[i].value(1) #Turn on the specific LED [i]
        if button_pin.value() == 0: #If button is low:
            seq_left() #Call on the function "seq_left"
        sleep(0.5) #Small delay before going back through the loop





# Main loop
try:
    while True:
        if button_pin.value() == 0:
            seq_right()
        if button1_pin.value() == 0:
            seq_left()                        
            
except KeyboardInterrupt:
    # Turn off all LEDs when interrupted
    for led in led_pins:
        led.value(0)
    print("Program stopped. All LEDs are now off.")