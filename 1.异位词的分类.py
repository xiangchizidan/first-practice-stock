# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词
class C:
    def groupAnagrams(self, strs):
        hashtable={}
        for item in strs:
            s=''.join(sorted(item))
            if s not in hashtable:
                hashtable[s]=[item]
            else:
                hashtable[s].append(item)
        return list(hashtable.values())

class Solution:
    def groupAnagrams(self, strs):
        table = {}
        for s in strs:
            s_ = "".join(sorted(s))
            if s_ not in table:
                table[s_] = [s]
            else:
                table[s_].append(s)
        return list(table.values())

