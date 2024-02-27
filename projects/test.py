def choose(paragraphs, select, k):
    valid_paragrph=[]
    for paragraph in paragraphs:
        if select(paragraph):
            valid_paragrph += [paragraph]
    if len(valid_paragrph) <= k:
        return ''
    else:
        return valid_paragrph[k]