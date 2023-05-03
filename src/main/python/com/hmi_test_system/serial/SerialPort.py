from threading import Thread
import queue

class SerialPort:

    is_receiving : bool
    thread : Thread 
    
    def __init__(self):
        self.is_receiving = False
        self.thread = Thread(target = self.thread_loop)
        self.port_queue = queue.Queue()

    def start_receive(self):
        self.is_receiving = True
        self.thread.start()

    def stop_receive(self):
        self.is_receiving = False
        self.thread.join()

    def thread_loop(self):
        while self.is_receiving:

    def read_port(self):
        pass

    def clear_queue(self):
        self.port_queue.queue.clear()


    