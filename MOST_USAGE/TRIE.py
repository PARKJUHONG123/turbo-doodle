class Node(object):
    def __init__(self, key, count=0):
        self.key = key
        self.child = {}
        self.value = 0

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for i in range(len(word)):
            ch = word[i]
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur.value += 1
            cur = cur.child[ch]
        cur.child["*"] = True

    def search(self, word):
        cur = self.head
        for i in range(len(word)):
            if word[i] not in cur.child:
                ############################
                if word[i] == "?":
                    if i == 0:
                        return cur.value
                    else:
                        return cur.value
                else:
                #############################
                    return 0 # don't exist
            else:
                cur = cur.child[word[i]]
        if "*" in cur.child:
            return 1 #exist

def main():
    trie = Trie()
    trie.insert('hooong')
    print(trie.search('hooong'))

if __name__ == "__main__":
    main()