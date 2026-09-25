class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for i, string in enumerate(strs):
            hash_map[''.join(sorted(string))].append(i)

        output = []

        for key in hash_map:
            temp = []
            for index in hash_map[key]:
                temp.append(strs[index])
            output.append(temp)
        
        return output

        