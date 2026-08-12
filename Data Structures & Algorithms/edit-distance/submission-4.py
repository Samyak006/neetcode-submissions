class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            word 1 -> word 2
            edit(i,j):{
                if word1[i] == word2[j]:
                    edit(i+1, j+1)
                else:
                    #replace/
                    1+edit(i+1,j+1)
                    #delete
                    1+edit(i+1,j)
                    #insert
                    1+edit(i,j+1)
            }
        """
        cache = {}
        def edit(i,j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i,j) in cache:
                return cache[(i,j)]
            if word1[i] == word2[j]:
                cache[(i,j)] = edit(i+1,j+1) 
                return cache[(i,j)]
            else:
                cache[(i,j)] = 1 + min(edit(i+1,j+1),edit(i+1,j),edit(i,j+1))
                return cache[(i,j)]      
        return edit(0,0)
        
