class TernarySearchTree:
    def __init__(self):
        self._tst = []
    
    def search(self, s):
        if not self._tst or not s:
            return(False)
        s = s + chr(0)
        n = 0
        while s:
            node = self._tst[n]
            ch = node[0]
            if s[0] < ch:
                n = node[1]
            elif s[0] > ch:
                n = node[2]
            else:
                n = node[3]
                s = s[1:]
            if n is None and s:
                return (False)
        return (True)

    def insert(self, s):
        assert(s)
        s = s + chr(0)
        if not self._tst:
            self._tst.append([s[0], None, None, None])
        n = 0
        while s:
            node = self._tst[n]
            ch = node[0]
   
            if s[0] < ch:
                if node[1] is None:
                    self._tst.append([s[0], None, None, None])
                    node[1] = len(self._tst) - 1
                n = node[1]
            elif s[0] > ch:
                if node[2] is None:
                    self._tst.append([s[0], None, None, None])
                    node[2] = len(self._tst) - 1
                n = node[2]
            else:
                if node[3] is None and ord(ch):
                    self._tst.append([s[1], None, None, None])
                    node[3] = len(self._tst) - 1
                n = node[3]
                s = s[1:]

if __name__ == 'builtins':
    from itertools import permutations
    from random import shuffle

    tst = TernarySearchTree()
    words = permutations("aabcdefgh")
    print("Creating dictionary ...")
    c = 0
    for w in words:
        tst.insert("".join(w))
        c += 1
    print("Total " + str(c) + " words")

    words = permutations("aabcdefgh")
    print("Test for words ...")
    for w in words:
        w = list(w)
        shuffle(w)
        assert(tst.search("".join(w)))

    words = permutations("aabcdefgh")
    print("Test 1 ...")
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(not tst.search("".join(w)+'b'))

    words = permutations("aabcdefgh")
    print("Test 2 ...")    
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(not tst.search("".join(w)[1:]))

    words = permutations("aabcdefgd")
    print("Test 3 ...")    
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(not tst.search("".join(w)))

    words = permutations("aabcdefgz")
    print("Test 4 ...")    
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(not tst.search("".join(w)))
        
        
