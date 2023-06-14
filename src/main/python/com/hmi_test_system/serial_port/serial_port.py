import queue
import time
from threading import Thread

import serial


class SerialPort:

    _is_receiving : bool
    _thread : Thread
    
    def __init__(self, port):
        self._is_receiving = False
        self._thread = Thread(target = self._thread_loop)
        self._serial = serial.Serial(port = port, baudrate = 115200, bytesize = 8, parity = serial.PARITY_NONE, stopbits = 1, xonxoff=False)
        self._port_queue_data = queue.Queue()
        self._port_queue_time = queue.Queue()
    
    def get_serial(self):
        if self._port_queue_data.empty():
            return None, None
        else:
            return self._port_queue_data.get(), self._port_queue_time.get()

    def start_receive(self):
        self._is_receiving = True
        self._thread.start()

    def stop_receive(self):
        self._is_receiving = False
        if self._thread.is_alive():
            try:
                self._thread.join()
            except RuntimeError:
                pass
    
    def _thread_loop(self):
        while self._is_receiving:
            self._read_port()

    def _read_port(self):
        try:
            if not self.closed() and self._serial.in_waiting != 0:
                data = self._serial.readline().decode()
                current_time = time.time()
                data = data.strip()
                if len(data) > 0:
                    self._port_queue_data.put(data)
                    self._port_queue_time.put(current_time)
        except:
            self.close()

    def write_port(self, data: str):
        self._serial.write(data.encode('utf-8'))

    def clear_queue(self):
        self._port_queue_data.queue.clear()
        self._port_queue_time.queue.clear()

    def close(self):
        self.stop_receive()
        self.clear_queue()
        if not self.closed():
            self._serial.close()

    def closed(self):
        return ((self._serial is None) or (not self._serial.is_open))
    