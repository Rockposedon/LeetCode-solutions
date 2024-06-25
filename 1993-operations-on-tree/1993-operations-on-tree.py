class LockingTree:
    
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = {}  # stores {node: user} for locked nodes
        self.children = {i: [] for i in range(len(parent))}
        for child, par in enumerate(parent):
            if par != -1:
                self.children[par].append(child)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            del self.locked[num]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False

        # Check for locked ancestors
        ancestor = num
        while ancestor != -1:
            if ancestor in self.locked:
                return False
            ancestor = self.parent[ancestor]

        # Check for at least one locked descendant and unlock them
        has_locked_descendant = False
        stack = [num]
        while stack:
            node = stack.pop()
            if node in self.locked:
                has_locked_descendant = True
                del self.locked[node]
            stack.extend(self.children[node])

        if not has_locked_descendant:
            return False

        # Lock the node
        self.locked[num] = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)