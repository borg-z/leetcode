from python.two_sum import Solution


CASES = [
[[2,7,11,15],9, [0,1]],
[[3,3],6,[0,1]]
]

solution = Solution()

def test_solution():
    for case in CASES:
        assert case[2] == solution.twoSum(case[0],case[1])
