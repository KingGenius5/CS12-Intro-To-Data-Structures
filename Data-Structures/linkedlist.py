#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?
        O(N) since it'll go through all of the nodes everytime once indicating linear time.
        """
        # TODO: Loop through all nodes and count one for each
        node = self.head#always starting at head
        count = 0
        while node is not None:#keep looping until there are no more references
            count += 1
            #this will go to the next node
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        Should be O(1) since we're only keeping track of the tail taking up constant time.
        """
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)

        if self.tail is not None:
            #point current tail to new node
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        Just like append, this should be constant time which means O(1) since we're
        only keeping track of the head node.
        """
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        #does head exist?
        if self.head is not None:
            #setting new node to point to current head as well as changing head pointer
            new_node.next = self.head
            self.head = new_node
        
        else:
            self.head = new_node
            self.tail = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
         O(1) if item is first in the list.
        TODO: Worst case running time: O(???) Why and under what conditions?
        I'm assuming O(N) if you have to transverse the entire linkedlist? Possibly
        looking for something at the end of the linkedlist or it doesn't exist at all.
        """
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head

        while node is not None:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next

        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        I'm thinking it's the same as find, where it's O(1) if the first item is deleted
        TODO: Worst case running time: O(???) Why and under what conditions?
         O(N) if the last item is deleted or isn't in the list so the whole linkedlist needs to be traversed.
        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        current_node = self.head
        prev_node = None

        #while there are still more nodes in linkedlist
        while current_node is not None:

            
            #node with item has been found
            if item == current_node.data:

                #Cases
                #item we want to remove is at head
                if prev_node is None:
                    self.head = current_node.next

                    #but head is also tail
                    if current_node.next is None:
                        self.tail = prev_node

                #item we want to remove is at tail
                elif current_node.next is None:
                    prev_node.next = None
                    self.tail = prev_node

                #make previous node point to next node
                else:
                    prev_node.next = current_node.next

                return
            
            else:
                prev_node = current_node
                current_node = current_node.next

        raise ValueError(f'Item not found: {item}')

    def update_list(self, data):
        '''Updates list by checking if data passed exist,
        if data exist in the list, delete then append
        if not just append'''
        for item in self.items():
            if item[0] == data[0]:
                print(f"Updating {item} to {data}")
                self.delete(item)
            else:
                continue
            self.append(data)



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()