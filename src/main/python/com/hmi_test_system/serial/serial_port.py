from threading import Thread
import serial
import queue

class SerialPort:

    is_receiving : bool
    thread : Thread
    
    def __init__(self, port):
        self.is_receiving = False
        self.thread = Thread(target = self.thread_loop)
        self.port_queue = queue.Queue()
        self.serial = serial.Serial(port = port, baudrate = 115200, bytesize = 8, parity = serial.PARITY_NONE, stopbits = 1, xonxoff=False)

    # igual ao que tem no get_image
    def get_serial(self):
        pass

    def start_receive(self):
        self.is_receiving = True
        self.thread.start()

    def stop_receive(self):
        self.is_receiving = False
        self.thread.join()

    def thread_loop(self):
        while self.is_receiving:
            self.read_port()

    # acrescentar time.time()
    # a fila tem dois valores (usar tupla) [0]->informação, [1]->tempo
    def read_port(self):
        if self.serial.in_waiting() != 0:
            self.port_queue.put(self.serial.readline().decode())

    # enviar uma string por serial port
    def write_port(self, data):
        pass

    def clear_queue(self):
        self.port_queue.queue.clear()


    