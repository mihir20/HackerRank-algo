    #!/bin/python3

import sys

def designerPdfViewer(h, word):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    height= []
    for i in range(len(word)):
        for j in range(len(alphabets)):
            if word[i] == alphabets[j]:
                height.append(h[j])
    return max(height)*len(word)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
