

def reverse(text):
    gg=[]
    print(text)

    for y in range(len(text)):

        gg.insert(0,text[y])
    hh=''.join(gg)
    print(hh)

#str1 = ''.join(list1)

reverse("hello")