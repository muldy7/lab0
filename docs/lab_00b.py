import micropython
import time
import cqueue



interrupt = pyb.Timer (1,freq = 1000)
pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)  #initializes the pin as an outport pin
pinB0 = pyb.Pin (pyb.Pin.board.PB0, pyb.Pin.IN) #need to intialize the output pin i think in the same way
QUEUE_SIZE = 2000
int_queue = cqueue.IntQueue(QUEUE_SIZE)
output_array=[]  # array where the outputted values will go before printing
step = 0.001   
time = list(range(QUEUE_SIZE)) #list of times to print alongside output_array
# float(i) * step for i in range(int(0.001 / step), int(2.001 / step))

def main():
    micropython.alloc_emergency_exception_buf(100) # alocates buffer for emergency exception handling, used when memory is a constraint
    
      
    
    
    
          # timer 1 running at 1000 Hz
    interrupt.counter()                         # gets the timer value
    # timer.freq(100)
        
                                   # this is the size of the que to collect 2 seconds of data at 1 ms interupts

    step_response()
    

def timer_int(tim_num):
    """!
    Doxygen style docstring for interrupt callback function
    """
  
    #COLLECT ADC
    int_queue.put(pinB0.value())  #read and put into queue. inside the put() is the value that will be read from the pin. this has not been set up in the code yet
    int_queue.full()
    if int_queue.full() == True:
            interrupt.callback(None)          #If queue is full, disable Callback 
    else:
        pass
   
    pass 
      


def step_response():# run this function when requeste dby user or through GUI
    """!
    Doxygen style docstring for this function 
    """
    # Function code here
    
    interrupt.callback (timer_int)  #configure and enable the calllback. example : timmy.callback(timer_cb)
    pinC0.high()                   #set the trigger pin to high pin.high   (pinC0.value(1)
    while not int_queue.full():                             #wait for a full queue ( while not my_que.full()
            pass						#     pass
            pinC0.low ()                 #	Set pin back to low
                                    
    while int_queue.any():          #iterate through the queue to and add to the array output_array
        output=int_queue.get()
        output_array.append(output)
    print('done')
    print(output_array)
    

if __name__ == "__main__":
    main()