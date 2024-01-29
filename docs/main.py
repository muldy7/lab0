# from matplotlib import pyplot
import time

x = 1
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)

while x == 1:
    pinC0.value(1)
    time.sleep(5)
    pinC0.value(0)
    time.sleep(5)

    

    
