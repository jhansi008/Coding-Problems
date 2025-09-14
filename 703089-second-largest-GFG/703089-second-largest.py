class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        unique = sorted(set(arr), reverse=True)
        if len(unique)>1:
          return unique[1]
        else:
          return -1