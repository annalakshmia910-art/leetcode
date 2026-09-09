class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        # key -> Node
        self.nodes = {}

        # frequency -> doubly linked list
        self.freq_list = {}

    def add_front(self, node):
        freq = node.freq

        if freq not in self.freq_list:
            self.freq_list[freq] = [None, None]

        head, tail = self.freq_list[freq]

        node.next = head
        node.prev = None

        if head:
            head.prev = node
        else:
            self.freq_list[freq][1] = node

        self.freq_list[freq][0] = node

    def remove(self, node):
        freq = node.freq
        head, tail = self.freq_list[freq]

        if node.prev:
            node.prev.next = node.next
        else:
            self.freq_list[freq][0] = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.freq_list[freq][1] = node.prev

    def increase_freq(self, node):
        old_freq = node.freq

        self.remove(node)

        if self.freq_list[old_freq][0] is None:
            if old_freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1

        self.add_front(node)

    def get(self, key):
        if key not in self.nodes:
            return -1

        node = self.nodes[key]

        self.increase_freq(node)

        return node.value

    def put(self, key, value):

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.nodes:
            node = self.nodes[key]

            node.value = value
            self.increase_freq(node)

            return

        # Cache is full
        if self.size == self.capacity:

            # Remove LRU node from minimum frequency
            head, tail = self.freq_list[self.min_freq]

            remove_node = tail

            self.remove(remove_node)

            del self.nodes[remove_node.key]

            self.size -= 1

        # Create new node
        node = Node(key, value)

        self.nodes[key] = node

        self.min_freq = 1

        self.add_front(node)

        self.size += 1