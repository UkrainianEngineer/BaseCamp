import abc


class Container (object):
    __meta__ = abc.ABCMeta

    level = None
    original_level = None

    @abc.abstractmethod
    def increase(self, amt=1):
        self.level = self.level + amt

    @abc.abstractmethod
    def decrease(self, amt=1):
        self.level = self.level - amt

    @abc.abstractmethod
    def is_empty(self):
        return self.level == 0


class Pot(Container):
    def __init__(self, level):
        self.level = level
        self.original_level = level


class Watertank(Container):
    def __init__(self, level):
        self.level = level
        self.original_level = level


class Coffee:
    def __init__(self):
        self.refill = 20
        self.watertank = Watertank(20)
        self.pot = Pot(0)
        self.filter = False
        self.on = False
        self.spoons = 0

    def brew(self):  # And as requirment
        if self.is_ready():
            print("The coffee is brewing...")

            while self.on:
                self.watertank.decrease(1)
                self.pot.increase(1)

                if self.pot.level == self.watertank.original_level and self.watertank.is_empty():
                    print("The coffee has been brewed. Enjoy!")
                    break
        else:
            print("Sorry, the brewer is not ready to brew.")
            self.ready_check()

    def ready_check(self):
        if self.watertank.level == 0:
            print("The Watertank is not filled.")
        if not self.filter:
            print("A filter has not been loaded.")
        if self.spoons == 0:
            print("There are no spoons of coffee mix.")
        if self.pot.level > 0:
            print("The Pot is not empty.")
        if not self.on:
            print("The brewer is not turned on.")

    def is_ready(self):
        return self.watertank.level > 0 \
            and self.filter \
            and self.spoons > 0\
            and self.pot.level == 0 \
            and self.on

    def add_spoons(self, amt=1):
        self.spoons = self.spoons + amt

    def install_filter(self):
        self.filter = True
        print("A filter has been installed.")

    def turn_on(self):
        self.on = True
        print("The brewer is now on!")

    def turn_off(self):
        self.on = False
        print("The brewer is now off!")


if __name__ == "__main__":
    brewer = Coffee()
    brewer.install_filter()
    brewer.add_spoons(4)
    brewer.turn_on()

    brewer.brew()
