# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.initial_value = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    #def decrease(self):
    #    pass

    # Write the rest of the methods here!


#-----------------------------------------------------------------------------------------
# PART 1:  Decreasing the value of the counter
# Please complete the method decrease defined in the template, so that it decreases the value stored in the counter by one. 
# See the example above for expected behaviour.

    # def decrease(self):
    #     self.value -= 1




#-----------------------------------------------------------------------------------------
# PART 2:  The counter must not have a negative value
# Please add functionality to your decrease method, so that the value of the counter will never reach negative values. 
# If the value of the counter is 0, it will not be further decreased.

    def decrease(self):
        if self.value > 0:
            self.value -= 1


#-----------------------------------------------------------------------------------------
# PART 3:  Setting the value to zero
# Please add a method set_to_zero which sets the value of the counter to 0.

    def set_to_zero(self):
        self.value = 0


    def reset_original_value(self):
        self.value = self.initial_value

    
if __name__ == "__main__":
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()