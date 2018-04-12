def remove_duplicates(lst):
    wlst=lst
    nlst=[]
    for x in range(len(wlst)):

        wvar=(wlst[x])
        if wvar not in nlst:
            nlst.append(wvar)
    return nlst














remove_duplicates([1, 1, 2, 2])

