import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
pick_a_person=(random.choice(friends))
print(pick_a_person)
random_index=random.randint(0,4)
print(friends[random_index])