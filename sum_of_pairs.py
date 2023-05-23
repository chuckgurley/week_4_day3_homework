#  def sum_pairs(numbers, sum):


def sum_pairs(numbers, sum2):
    seen = {}
    for i, value in enumerate(numbers):
        diff = sum2 - value
        if diff in seen:
            return [diff, value]
        seen[value] = i
    return None
