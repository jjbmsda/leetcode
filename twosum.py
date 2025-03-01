class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # 값 -> 인덱스를 저장할 딕셔너리
        for i, num in enumerate(nums):
            complement = target - num  # 필요한 값 (target - 현재 값)
            if complement in num_map:  # 이미 저장된 값이면 정답
                return [num_map[complement], i]
            num_map[num] = i  # 현재 숫자를 딕셔너리에 추가함
