print("ungraded percent: ")
needP = float(input()) / 100
given = 1 - needP

print("curr grade: ")
current = float(input()) / 100

max = ((given * current) + needP) * 100
min = (given * current) * 100

print("max: ", max, "\nmin: ", min)

print("percent goal: ")
guess = float(input())
# goal - current = percent needed
need = (guess / 100) - (min / 100)
if need <= needP:
    need = need / needP
    print("need a ", need * 100, " to achieve goal of ", guess, "%")
else:
    print("max grade possible is: ", max)
