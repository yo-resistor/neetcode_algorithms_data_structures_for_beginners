class Listnode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # map key to node
        self.capacity = capacity
        self.occupy = 0
        self.left = Listnode(key=0, val=0)
        self.right = Listnode(key=0, val=0)
        # left indicates the least recently used node
        # right indicates the most recently used node
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # make the pointer value to the most recently used node
            target = self.cache[key]
            # cut the target node from the linked list
            target.prev.next = target.next
            target.next.prev = target.prev
            # add the target node at the end of the linked list
            target.prev = self.right.prev
            target.next = self.right
            self.right.prev.next = target
            self.right.prev = target
            # return the target node's value
            return target.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update the value and make it to the most recently used node
            target = self.cache[key]
            target.val = value
            # cut the target node from the linked list
            target.prev.next = target.next
            target.next.prev = target.prev
            # add the target node at the end of the linked list
            target.prev = self.right.prev
            target.next = self.right
            self.right.prev.next = target
            self.right.prev = target
            # end the function
            return
        else:
            # if the map is not fully occupied, add
            if self.occupy < self.capacity:
                # create a new node
                newNode = Listnode(key=key, val=value)
                # update the cache with the new key-val pointer pair
                self.cache[key] = newNode
                # add the new node at the ned of the linked list
                newNode.prev = self.right.prev
                newNode.next = self.right
                self.right.prev.next = newNode
                self.right.prev = newNode
                # increase the number of occupied elements
                self.occupy += 1
                # end the function
                return
            # if the map is fully occupied, evict LRU key-val pointer pair
            else:
                # create a new node
                newNode = Listnode(key=key, val=value)
                # update the cache with the new key-val pointer pair
                self.cache[key] = newNode
                # add the new node at the ned of the linked list
                newNode.prev = self.right.prev
                newNode.next = self.right
                self.right.prev.next = newNode
                self.right.prev = newNode
                # evict the least recently used node
                LRUnode = self.left.next
                # delete key-val pointer pair from cache
                del self.cache[LRUnode.key]
                # remove the node out of the linked list
                self.left.next = LRUnode.next
                LRUnode.next.prev = self.left
                # end the function
                return 
        

def main():
    obj = LRUCache(capacity=2)
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(key=1))
    obj.put(3,3)
    print(obj.get(2))
    obj.put(4,4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))

if __name__ == "__main__":
    main()