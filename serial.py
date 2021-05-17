"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Generate serial number from start input"""
        self.start = start 
        self.currNum = start

    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator(start={self.start}, next={self.next})>" 

    def __str__(self):
        """Show string representation"""
        return f"SerialGenerator start: {self.start}, currNum: {self.currNum}"

    def generate(self):
        """generate a the next serial number"""
        self.currNum += 1
        return self.currNum -1

    def reset(self):
        """reset the next serial number back to the start value (default: 0)"""
        self.currNum = self.start
