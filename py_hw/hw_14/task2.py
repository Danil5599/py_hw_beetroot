class Mathematician:
    def square_nums(self, nums):
        return [num**2 for num in nums]

    def remove_positives(self, nums):
        return [num for num in nums if num < 0]

    def filter_leaps(self, years):
        return [year for year in years if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
