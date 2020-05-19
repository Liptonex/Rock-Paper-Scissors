import random
class RPS:
    types = ["rock", "paper", "scissors"]

    # def __new__(cls, args):
    #     instance = object.__new__(cls)
    #     if args in cls.types:
    #         return instance
    def __init__(self, option):
        self.type = option
        for i in range(len(types)):
            if types[i] == self.type:
                x = i
        list = types[x + 1:]
        list.extend(types[:x])
        l = len(list)
        global win
        win = list[round(l / 2):]
        global lose
        lose = list[:round(l / 2)]
        pass
    def win(self):
        self.win = win
        return win
    def lose(self):
        self.lose = lose
        return lose
def rand():
    return random.choice(types)

def score(name, rating):
    x = 0
    for i in range(len(rating)):
        if name == rating[i][0]:
            x = rating[i][1]
        else:
            pass
    if x == 0:
        rating.append([name, x])
    return x


name = input("Enter your name:")

file = open('rating.txt', mode='r')
rating = []
for line in file:
    y = line.rstrip('\n')
    x = str.split(y, ' ')
    rating.append(x)
file.close()
for i in range(len(rating)):
    x = int(rating[i][1])
    rating[i][1] = x

points = score(name, rating)
print(f'Hello {name}!')

opt = input("Please enter options you'd like to use during the game. If you won't write anything a standard rock, "
            "paper, scissors will begin")

if opt == '':
    types = RPS.types
else:
    types = opt.split(',')

print(f'Here are your types {types}')

for i in range(len(types)):
    y = RPS(types[i])
    print(f"If you choose {[y.type]} you win against {y.win()} and you lose against {y.lose()}")

print("Anytime type:")
print("!ranking - to see how many points you have")
print("!exit - to stop the game")

print("Okay, lets's start!")

while True:
    x = input()
    if x == '!exit':
        print('Bye!')
        break
    elif x == '!rating':
        print(points)
    elif x in types:
        user = RPS(x)
        y = rand()
        computer = RPS(y)
        if user.type == computer.type:
            points += 50
            print(f'There is a draw ({computer.type})')
        elif user.type in computer.win():
            print(f'Sorry, but the computer choose {computer.type}')
        elif user.type in computer.lose():
            points += 100
            print(f'Well done. Computer chosse {computer.type} and failed')
    else:
        print('Invalid input')

