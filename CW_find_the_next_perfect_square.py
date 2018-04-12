#we need sqrt() so we import the build in math module
import math
#we start the function off taking in the square passed to it
def find_next_square(sq):
#for later we set up the number one higher than the passed square
    wsk=sq+1
    # Return the next square if sq is a square, -1 otherwise
#here we look to see if the passed number is a perfect square, if it is we look for the next one
    if math.sqrt(sq)%1==0:
        print("A Perfect Square! the next one is: ")
#here we are looking for the next one by taking the current one incrementing by one and checking for perfection
        #im using a modulus on 1 of greater than 0 to check for perfection
        while math.sqrt(wsk)%1>0:
            wsk=wsk+1
        return(wsk)

    else:
        return -1

#121->144
print(find_next_square(121))