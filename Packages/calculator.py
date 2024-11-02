def add(*nums) -> int:
    """Add given numbers

    Args:
        nums: Numbers to add
    
    Returns:
        int: Sum of given numbers
    """
    total = 0
    
    for num in nums:
        total += num
    
    return total

def sub(*nums) -> int:
    """Subtract given numbers

    Args:
        nums: Numbers to subtract
    
    Returns:
        int: Subtraction of given numbers
    """
    total = nums[0]
    
    for num in nums[1:]:
        total -= num
    
    return total