class Road:
    def __init__(self, start, end, id = -1):
        self.start = start
        self.end = end
        self.id = id
        self.intersected = False

    def __str__(self):
        return f"road{self.id}:({self.start}=>{self.end})"
    
    def __repr__(self):
        return str(self)
    
    def set_intersected(self):
        self.intersected = True