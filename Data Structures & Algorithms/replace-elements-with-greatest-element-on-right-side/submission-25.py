class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            for j in range(i-1, -1, -1):
                if arr[i] > arr[j]:
                    arr[j] = arr[i]
                else:
                    break
        
        arr.pop(0)
        arr.append(-1)

        return arr