class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic1, dic2 = Counter(ransomNote), Counter(magazine)
        return dic1 & dic2 == dic1
        