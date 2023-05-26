from threading import Thread
from serial import Serial, PARITY_NONE
import queue
import time
from .constant_test import *

class SerialPort:

    is_receiving : bool
    thread : Thread
    
    def __init__(self, port):
        self.is_receiving = False
        self.thread = Thread(target = self.thread_loop)
        self.serial = Serial(port = port, baudrate = 115200, bytesize = 8, parity = PARITY_NONE, stopbits = 1, xonxoff=False)
        self.port_queue_data = queue.Queue()
        self.port_queue_time = queue.Queue()
    
    def get_serial(self):
        if self.port_queue_data.empty():
            return None, None
        else:
            return self.port_queue_data.get(), self.port_queue_time.get()

    def start_receive(self):
        self.is_receiving = True
        self.thread.start()

    def stop_receive(self):
        self.is_receiving = False
        self.thread.join()

    def thread_loop(self):
        while self.is_receiving:
            self.read_port()

    def read_port(self):
        if self.serial.in_waiting != 0:
            data = self.serial.readline().decode()
            current_time = time.time()
            data = data.strip()
            if len(data) > 0:
                self.port_queue_data.put(data)
                self.port_queue_time.put(current_time)

    def write_port(self, data: str):
        self.serial.write(data.encode('utf-8'))

    def clear_queue(self):
        self.port_queue_data.queue.clear()
        self.port_queue_time.queue.clear()


    