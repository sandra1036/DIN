color_to_factor={'R': 0.3, 'G': 0.5, 'B': 0.2}
def is_balanced(color_to_factor):
 """ (dict of {str: float}) -> bool
 Return True if and only if color_to_factor represents a balanced color.
 >>> is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7})
 False
 >>> is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})
 True
 """
 values = list(color_to_factor.values())
 total = sum(values)
 return total == 1.0

if __name__=="__main__":
    print(is_balanced(color_to_factor))