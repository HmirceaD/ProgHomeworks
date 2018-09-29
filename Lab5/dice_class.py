from random import randint


class Dice:

    num_to_words = ['one', 'two', 'three', 'four', 'five', 'six']

    def __init__(self):
        self.dice_faces = []
        self.assign_faces()

    def assign_faces(self):
        for face in self.num_to_words:
            with open("{}.txt".format(face), "r") as f:
                self.dice_faces.append(f.read())

    def roll_dice(self):
        print("Let's roll the dice\n\n\n")
        print(self.dice_faces[randint(0,5)])


if __name__ == "__main__":
    dice_obj = Dice()
    dice_obj.roll_dice()
    dice_obj.roll_dice()
    dice_obj.roll_dice()
