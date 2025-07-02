from machine import Pin
import time

ids = [1, 3, 5, 7]

pins = {
    id_: Pin(id_, mode=Pin.IN, pull=Pin.PULL_UP)
    for id_ in ids
}


def check_state(state):
    cur_value = None
    next_value = None
    
    for i in range(len(state)-1):
        cur_value = state[i]
        next_value = state[i+1]
        
        if cur_value < next_value:
            return 'boom'
        
    return 'safe'

while True:
    time.sleep(1)
    state = [pins[id_].value() for id_ in ids]
    print(check_state(state))
    

