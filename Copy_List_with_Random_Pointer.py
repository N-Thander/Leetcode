class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        node_mapping = {}
        current = head
        while current:
            copied_node = Node(current.val)
            node_mapping[current] = copied_node
            current = current.next

        current = head
        while current:
            copied_node = node_mapping[current]
            copied_node.next = node_mapping.get(current.next)
            copied_node.random = node_mapping.get(current.random)
            current = current.next

        return node_mapping[head]
