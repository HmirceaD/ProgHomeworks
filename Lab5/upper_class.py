class UpperClass:

    def __init__(self):
        self.message = ""

    def read_string(self):
        self.message = input("Give a message to uppercase:\n")

    def output_string(self):
        print(self.message.upper())


def test_upper_class():

    upper_class = UpperClass()
    upper_class.read_string()
    upper_class.output_string()


if __name__ == "__main__":
    test_upper_class()
