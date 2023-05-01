from threading import Thread
import queue

class SerialPort:

    thread : Thread
    is_receiving : bool
    
    def __init__(self):
        self.is_receiving = False
        self.thread = Thread(target = self.thread_loop)
        self.port_queue = queue.Queue()

    def start_receive(self):
        pass

    def stop_receive(self):
        pass

    def thread_loop(self):
        pass

    def read_port(self):
        pass

    def clear_queue(self):
        pass


    