import micropython
import time

pinC0 = pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.OUT_PP)
time.sleep(2)
pinC0.high()
time.sleep(5)
pinC0.low()

