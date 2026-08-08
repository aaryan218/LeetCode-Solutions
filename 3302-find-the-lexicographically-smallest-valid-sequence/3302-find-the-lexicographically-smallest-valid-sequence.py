class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)


        suffix_match = [0] * (n + 1)
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suffix_match[i] = suffix_match[i + 1] + 1
                j -= 1
            else:
                suffix_match[i] = suffix_match[i + 1]
        

  
        res = []
        j = 0
        changed = False

        for i in range(n):

            if j == m:
                break
            

            if word1[i] == word2[j]:
                res.append(i)
                j += 1
    
            elif not changed:

                remaining_needed = m - j - 1

                if remaining_needed <= suffix_match[i + 1]:
                    res.append(i)
                    j += 1
                    changed = True
        
        if len(res) == m:
            return res
        return []