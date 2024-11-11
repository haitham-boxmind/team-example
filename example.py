# Import libraries
import math
import random

# Define constants
PI = math.pi
EULER = math.e

# Sample function to calculate area of a circle
def area_of_circle(radius):
    """Calculate area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return PI * (radius ** 2)

# Generate a list of random numbers
def generate_random_numbers(count, start=1, end=100):
    """Generate a list of random integers."""
    return [random.randint(start, end) for _ in range(count)]

# Fibonacci sequence generator
def fibonacci(n):
    """Generate Fibonacci sequence up to n."""
    a, b = 0, 1
    sequence = []
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example class to represent a simple counter
class Counter:
    def __init__(self, start=0):
        self.value = start
    
    def increment(self):
        """Increment counter by one."""
        self.value += 1
    
    def reset(self):
        """Reset counter to zero."""
        self.value = 0
    
    def __repr__(self):
        return f"Counter(value={self.value})"

# Usage examples
if __name__ == "__main__":
    print("Area of circle with radius 5:", area_of_circle(5))
    print("Random numbers:", generate_random_numbers(5))
    print("Fibonacci up to 20:", fibonacci(30))

    # Instantiate and use Counter
    counter = Counter()
    counter.increment()
    print("Counter after increment:", counter)
    counter.reset()
    print("Counter after reset:", counter)
