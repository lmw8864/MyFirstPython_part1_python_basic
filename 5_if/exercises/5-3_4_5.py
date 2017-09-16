# 5-3_4_5.py

"""
5-3. 외계인 색 #1
5-4. 외계인 색 #2
5-5. 외계인 색 #3
"""

alien_colors = ['green', 'blue', 'yellow', 'white', 'red']
for alien_color in alien_colors:
    print("You destroy a " + alien_color + " alien.")
    if alien_color == 'green':
        print(" + 5 points!\n")
    elif alien_color == 'yellow':
        print(" + 10 points!\n")
    elif alien_color == 'red':
        print(" + 15 points!\n")
    else:
        print(" - 30 points!\n")
