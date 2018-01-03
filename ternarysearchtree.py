class TreeNode:
    def __init__(self, char):
        self.split_char = char
        self.lt_node = 0
        self.gt_node = 0
        self.eq_node = 0
        self.leaf = False
        
class TernarySearchTree:
    def __init__(self):
        self._root = 0
    
    def search(self, s):
        if not s:
            return False
        n = self._root
        while n:
            if s[0] < n.split_char:
                n = n.lt_node
            elif s[0] > n.split_char:
                n = n.gt_node
            else:
                s = s[1:]
                if not s:
                    return True if n.leaf else False
                n = n.eq_node
        return False
    
    def has_prefix(self, s):
        if not s:
            return False
        n = self._root
        while n:
            if s[0] < n.split_char:
                n = n.lt_node
            elif s[0] > n.split_char:
                n = n.gt_node
            else:
                s = s[1:]
                if n.leaf:
                    return True
                n = n.eq_node
        return False
        
    def insert(self, s):
        assert(s)

        if not self._root:
            self._root = TreeNode(s[0])
            
        n = self._root
        while s:
            #char = s[0]

            if s[0] < n.split_char:
                if not n.lt_node:
                    n.lt_node = TreeNode(s[0])
                n = n.lt_node                
            elif s[0] > n.split_char:
                if not n.gt_node:
                    n.gt_node = TreeNode(s[0])
                n = n.gt_node                                    
            else:
                s = s[1:]
                if not s:
                    n.leaf = True
                    return
                if not n.eq_node:
                    #n.eq_node = TreeNode(char)
                    n.eq_node = TreeNode(s[0])
                n = n.eq_node
                
if __name__ == '__builtin__':
    from itertools import permutations
    from random import shuffle
    import cProfile
    pr = cProfile.Profile()
    
    tst = TernarySearchTree()
    pr.enable()
    PATTERN = "aabcdefgh"
    
    words = permutations(PATTERN)
    print("Creating dictionary ...")
    c = 0
    for w in words:
        tst.insert("".join(w))
        c += 1
    print("Total " + str(c) + " words")

    words = permutations(PATTERN)
    print("Test words ...")
    for w in words:
        assert(tst.search("".join(w)))

    words = permutations(PATTERN)
    print("Test 1 ...")
    for w in words:
        assert(not tst.search("".join(w)+'b'))

    words = permutations(PATTERN)    
    print("Test 2 ...")    
    for w in words:
        assert(not tst.search("".join(w)[1:]))

    words = permutations("aabcdefgd")
    print("Test 3 ...")    
    for w in words:
        assert(not tst.search("".join(w)))

    words = permutations("aabcdefgz")
    print("Test 4 ...")    
    for w in words:
        assert(not tst.search("".join(w)))

    words = permutations("aabcdefgb")
    print("Test 5 ...")    
    for w in words:
        assert(not tst.search("".join(w)))

    words = permutations(PATTERN)
    print("Test 6 ...")    
    for w in words:
        assert(tst.has_prefix("".join(w)))
    
    words = permutations(PATTERN)
    print("Test 7 ...")    
    for w in words:
        assert(tst.has_prefix("".join(w)+"b"))

    words = permutations(PATTERN)    
    print("Test 8 ...")    
    for w in words:
        assert(tst.has_prefix("".join(w)+"bf"))

    pr.disable()
    pr.print_stats(sort="time")
