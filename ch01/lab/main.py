import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 7
cost_per_class = cost_per_week / classes_per_week
print("The cost of class is", cost_per_class)
print(classes_per_week, int(classes_per_week))
print(cost_per_week, int(cost_per_week))
print(cost_per_class, int(cost_per_class))


the_list = [1, 2, 3, 4, 5]
random_number = random.choice(the_list)
print(random_number)