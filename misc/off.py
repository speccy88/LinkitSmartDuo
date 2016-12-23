from pyfirmata import Arduino

board = Arduino('/dev/ttyS0')
#board.digital[13].write(1)
board.digital[13].write(0)
