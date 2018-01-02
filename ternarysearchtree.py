class TreeNode:
    def __init__(self, char):
        self.split_char = char
        self.lt_node = 0
        self.gt_node = 0
        self.eq_node = 0
        self.leaf = False
        
class TernarySearchTree:
    def __init__(self):
        self._tst = []
    
    def search(self, s):
        if not self._tst or not s:
            return(False)
        n = 0
        while n is not None:
            char = s[0]
            splitchar, lt_node, gt_node, eq_node, leaf = self._tst[n:n+5]
            if char < splitchar:
                n = lt_node
            elif char > splitchar:
                n = gt_node
            else:
                s = s[1:]
                if not s:
                    return(True if leaf else False )
                n = eq_node
        return(False)            

    def has_prefix(self, s):
        if not self._tst or not s:
            return(False)
        n = 0
        while n is not None:
            char = s[0]
            splitchar, lt_node, gt_node, eq_node, leaf = self._tst[n:n+5]
            if char < splitchar:
                n = lt_node
            elif char > splitchar:
                n = gt_node
            else:
                s = s[1:]
                if leaf:
                    return(True)
                n = eq_node
        return(False)            

    def insert(self, s):
        assert(s)

        if not self._tst:
            self._tst.extend((s[0], None, None, None, False))
            
        n = 0
        while s:
            char = s[0]
            splitchar, lt_node, gt_node, eq_node, leaf = self._tst[n:n+5]
            if char < splitchar:
                if lt_node is None:
                    self._tst.extend((char, None, None, None, False))
                    self._tst[n+1] = len(self._tst) - 5
                    n = len(self._tst) - 5
                else:                    
                    n = lt_node                
            elif char > splitchar:
                if gt_node is None:
                    self._tst.extend((char, None, None, None, False))
                    self._tst[n+2] = len(self._tst) - 5
                    n = len(self._tst) - 5
                else:
                    n = gt_node                                    
            else:
                s = s[1:]
                if not s:
                    self._tst[n+4] = True
                    return()
                if eq_node is None:
                    self._tst.extend((s[0], None, None, None, False))
                    self._tst[n+3] = len(self._tst) - 5
                    n = len(self._tst) - 5
                else:
                    n = eq_node                                    
if __name__ == '__builtin__':
    import cProfile
    pr = cProfile.Profile()
    
    from itertools import permutations
    from random import shuffle

    tst = TernarySearchTree()
    pr.enable()
    words = permutations("aabcdefgh")
    print("Creating dictionary ...")
    c = 0
    for w in words:
        tst.insert("".join(w))
        c += 1
    print("Total " + str(c) + " words")

    for w in words:
        w = list(w)
        shuffle(w)
        assert(tst.search("".join(w)))

    print("Test 1 ...")
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(not tst.search("".join(w)+'b'))

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

    words = permutations("aabcdefgb")
    print("Test 5 ...")    
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(not tst.search("".join(w)))

    words = permutations("aabcdefgh")
    print("Test 6 ...")    
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(tst.has_prefix("".join(w)))

    print("Test 7 ...")    
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(tst.has_prefix("".join(w)+"b"))

    print("Test 8 ...")    
    for w in words:
        w = list(w)    
        shuffle(w)    
        assert(tst.has_prefix("".join(w)+"bf"))


    pr.disable()
    pr.print_stats(sort="time")
