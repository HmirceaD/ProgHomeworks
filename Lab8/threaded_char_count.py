import threading


class ThreadedCharCount(threading.Thread):

    def __init__(self, c):
        threading.Thread.__init__(self)

        with open("text.txt", "r") as f:
            self.text = f.read()

        self.c = c

    def run(self):
        lock = threading.Lock()

        with lock:
            counter = 0
            words = self.text.split(" ")

            for word in words:
                for char in word:
                    if char == self.c:
                        counter += 1

            print("The character {0} appeared in the text {1} times".format(self.c, counter))
