# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:29:21 2018

@author: Nodar.Okroshiashvili
"""



# Put this number in j 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
# or whatever you want

h = list(map(int, input().strip().split(' ')))
word = input().strip()


def designerPdfViewer(h, word):
    letters_heights = [h[ord(i) - 97] for i in word]
    area = max(letters_heights) * len(letters_heights)
    return area


result = designerPdfViewer(h, word)


