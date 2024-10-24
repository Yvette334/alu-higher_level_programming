#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)

    if (leng == 0):
        ntuple = (leng, None)
    else:
        ntuple = (leng, sentence[0])

    return (ntuple)
