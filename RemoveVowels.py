
def anti_vowel(text):
    vow=["a","e","i","o","u","A","E","I","O","U"]
    gg=[]
    nn=[]
    for x in range(len(text)):

        yy=text[x]
        if yy in vow:
            nn.insert(x,yy)
        else:
            gg.insert(x,text[x])
        ff=''.join(gg)
    print(ff)
    return(ff)



anti_vowel("WhAt Youths")