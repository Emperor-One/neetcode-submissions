class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)
        for string in strs:
            bucket[tuple(sorted(string))].append(string)

        output = []
        for key in bucket:
            output.append(bucket[key])

        return output
        