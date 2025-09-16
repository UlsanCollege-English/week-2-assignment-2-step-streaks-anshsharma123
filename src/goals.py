from typing import List, Tuple, Optional

def max_window_sum(nums: List[int], k: int) -> Optional[Tuple[int, int]]:
    if k <= 0:
        raise ValueError("Window size k must be positive")
    if len(nums) < k:
        return None

    max_sum = current_sum = sum(nums[:k])
    max_index = 0

    for i in range(1, len(nums) - k + 1):
        current_sum = current_sum - nums[i-1] + nums[i+k-1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i

    return max_index, max_sum


def count_goal_windows(nums: List[int], k: int, goal: float) -> int:
    if k <= 0:
        raise ValueError("Window size k must be positive")
    if len(nums) < k:
        return 0

    count = 0
    current_sum = sum(nums[:k])
    if current_sum / k >= goal:
        count += 1

    for i in range(1, len(nums) - k + 1):
        current_sum = current_sum - nums[i-1] + nums[i+k-1]
        if current_sum / k >= goal:
            count += 1

    return count


def longest_rising_streak(nums: List[int]) -> int:
    if not nums:
        return 0

    max_streak = current_streak = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak
