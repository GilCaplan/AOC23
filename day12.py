from functools import lru_cache

with open("input12.txt", "r") as file:
    lines = [line.strip().split() for line in file]

puzzle = [line[0] for line in lines]
groups = [tuple(map(int, line[1].split(','))) for line in lines]


# recursive function, check each possible character and break the string down to count permutations.
@lru_cache(maxsize=None)
def find_damaged_per(springs, nums):
    if len(springs) == 0:
        return 1 if len(nums) == 0 else 0

    if springs[0] == '.':
        return find_damaged_per(springs[1:], nums)

    if springs[0] == '#':
        if len(nums) == 0 or len(springs) < nums[0] or any(c == '.' for c in springs[:nums[0]]):
            return 0
        if len(nums) > 1:
            if len(springs) < nums[0] + 1 or springs[nums[0]] == "#":
                return 0

            return find_damaged_per(springs[nums[0] + 1:], nums[1:])
        else:
            return find_damaged_per(springs[nums[0]:], nums[1:])

    if springs[0] == '?':
        return find_damaged_per(springs.replace('?', '.', 1), nums) \
            + find_damaged_per(springs.replace('?', '#', 1), nums)


print('part 1: ', sum(find_damaged_per(springs, nums) for springs, nums in zip(puzzle, groups)))
print('part 2: ', sum(find_damaged_per(str('?'.join([springs]*5)), tuple(nums * 5)) for springs, nums in zip(puzzle, groups)))

