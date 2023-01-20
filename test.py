dices = [6, 2, 3, 4, 5]

small_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

for straight in small_straights:
    if all(item in dices for item in straight):
        print("Small straight")
        break

else:
    print("No small straight")
