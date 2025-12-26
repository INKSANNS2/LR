"""
Возведение чисел в степень через замыкания и класс-методы.
"""

def power_factory(exp):
    """Создает функцию, возводящую в степень exp."""
    def inner(x):
        return x ** exp
    return inner

class MathTools:
    """Математические инструменты."""
    
    @classmethod
    def power_list(cls, nums, n):
        """Возводит все числа из nums в степень n."""
        power = power_factory(n)
        return [power(x) for x in nums]
    
    @classmethod  
    def power_func(cls, exp):
        """Создает функцию для возведения в степень exp."""
        return power_factory(exp)

square = power_factory(2)
print(f"5² = {square(5)}")  # 25
print(f"3² = {square(3)}")  # 9
nums = [1, 2, 3, 4]
result = MathTools.power_list(nums, 2)
print(f"{nums}² = {result}")  # [1, 4, 9, 16]
cube = MathTools.power_func(3)
print(f"2³ = {cube(2)}")  # 8
print(f"4³ = {cube(4)}")  # 64