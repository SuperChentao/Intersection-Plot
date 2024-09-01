class Road:
    def __init__(self, start, end, id = -1):
        self.start = start
        self.end = end
        self.id = id
        self.intersected = False

    def __str__(self):
        return f"({self.start},{self.end})"
    
    def __repr__(self):
        return str(self)
    
    def repr_id(self):
        return f"<{self.start.id},{self.end.id}>"
    
    def set_intersected(self):
        self.intersected = True
        
    def __eq__(self, other):
        if not isinstance(other, Road):
            return False
        return (self.start == other.start and self.end == other.end) or (self.end == other.start and self.start == other.end)
    
    def __hash__(self):
        return hash((min(self.start, self.end), max(self.start, self.end)))
        
        # return hash((self.start, self.end))