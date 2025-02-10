import canio
import time
import digitalio
import board

#Initialize CAN bus
if hasattr(board, 'CAN_STANDBY'):
    standby = digitalio.DigitalInOut(board.CAN_STANDBY)
    standby.switch_to_output(False)

if hasattr(board, 'BOOST_ENABLE'):
    boost_enable = digitalio.DigitalInOut(board.BOOST_ENABLE)
    boost_enable.switch_to_output(True)

can = canio.CAN(board.CAN_TX, board.CAN_RX, baudrate=1000000)

#Function to send a CAN message to control motor speed
def control_motor():
    #Command byte: 0xA2
    #Speed set to a specific value (adjust as needed):
    data = b'\xA2\x00\x00\x00\xA0\x86\x01\x00'  # Modify these bytes to change speed
    message = canio.Message(id=0x141, data=data)
    can.send(message)

# Function to stop the motor
def stop_motor():
    #Command to stop the motor (all speed bytes set to 0)
    data = b'\xA2\x00\x00\x00\x00\x00\x00\x00'
    message = canio.Message(id=0x141, data=data)
    can.send(message)

#Run motor at hardcoded speed for 15 seconds
control_motor()
time.sleep(15) #runs for 15 seconds
stop_motor()

#Deinitialize CAN bus
can.deinit()