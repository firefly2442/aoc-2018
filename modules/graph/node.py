class Node:
    def __init__(self, name):
        self.name = name
        self.triggered = False
        self.parents = []
        self.child_nodes = []

    def add_child(self, child):
        if child in self.child_nodes:
            return

        child.add_parent(self)
        self.child_nodes.append(child)
        self.child_nodes.sort(key=lambda n: n.name)

    def add_parent(self, parent):
        if parent in self.parents:
            return

        self.parents.append(parent)

    def can_trigger(self):
        for parent in self.parents:
            if not parent.triggered:
                return False
        return True

    def is_root(self):
        if len(self.parents) == 0:
            return True
        return False
