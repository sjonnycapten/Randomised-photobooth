import serial


ser = serial.Serial('COM5',9600,timeout =0.001)
def readbutton():
    ser_bytes = ser.read(100)
    decoded_bytes = (ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
    if (decoded_bytes) == "2":
        return 1
    else:
        return 0



