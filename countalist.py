
def count(sequence,item):
    h=sequence
    x=0
    for z in range(len(h)):

        if item == h[z]:
            print(h[z])
            print("It's in there!")
            x+=1

    else:
        print("Taint")
    print(x)
    print(h)
    print("Item: ",item)



#count([1, 2, 1, 1], 3)

count([1, 2, 1, 1], 1)
