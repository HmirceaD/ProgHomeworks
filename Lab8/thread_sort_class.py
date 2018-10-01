#prob1
import threading
from queue import Queue


class ThreadSort(threading.Thread):

    def __init__(self, *lists):
        threading.Thread.__init__(self)
        self.list_queue = Queue()

        for list_item in lists:
            self.list_queue.put(list_item)

    def run(self):
        lock = threading.Lock()

        while not self.list_queue.empty():
            with lock:
                sorted_list = self.list_queue.get()
                sorted_list.sort()
                print(sorted_list)

