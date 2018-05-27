import random

NUMBER_OF_STEPS = random.randint(10,30)

message = "There were not enough of iteration. Please check your `while` loop."

step_count = 0

while step_count < NUMBER_OF_STEPS:
    step_count += 1
    print(random.randint(10,30))
    
print('\n')    

print("Iterated {} times.".format(step_count))
assert step_count == NUMBER_OF_STEPS, message

