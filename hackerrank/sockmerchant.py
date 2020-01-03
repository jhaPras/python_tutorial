def sockmerchant(i,*ar):
    counter = {i:ar.count(i) for i in ar}
    for k,_ in counter.items():
        if counter[k] == 2:
            pair_list = []
            pair_list.append(k)
        else:
            pass
    return len(pair_list)
