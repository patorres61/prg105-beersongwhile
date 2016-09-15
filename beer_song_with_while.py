# 99 Bottles of Beer on the Wall using a While statement

# define the index
num_beers = 99

while num_beers > 0:
    if num_beers == 1:                  # checking index - if it is one, change bottles to bottle
        print(num_beers),
        print(" bottle of beer on the wall,"),
        print(num_beers),
        print(" bottle of beer.")
        print("Take one down and pass it around,"),
        print(" no more bottles of beer on the wall.\n")
        num_beers -= 1
    else:
        print(num_beers),
        print(" bottles of beer on the wall,"),
        print(num_beers),
        print(" bottles of beer.")
        print("Take one down and pass it around,"),
        num_beers -= 1
        if num_beers == 1:              # checking index - if it is one, change bottles to bottle
            print(num_beers),
            print(" bottle of beer on the wall.\n")
        else:
            print(num_beers),
            print(" bottles of beer on the wall.\n")

# the while statement is now completed, time for the program wrap-up
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall!\n")

print("Now our song is done, let's drink!")
