class Solution:
    # hash_memo = {}
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        
        i = 2
        result = "11"
        while True:
            if i >= n:
               break

            arr = list(result)
            print(arr)
            temp = int(arr[0])
            counter = 0
            
            j=0
            while True:
                print(counter)
                if int(arr[j]) != temp or j==len(arr)-1:
                    if counter == 1:
                        arr=arr[:j] + ['1'] + arr[j:]
                        counter = 0
                        j += 2

                    elif counter > 1:
                        arr [j-counter] = counter
                        arr = arr[:j-counter] + arr[j:]
                        j -= counter
                        counter = 0

                    
                else:
                    counter+=1
                if j>=len(arr)-1:
                    break
                temp = int(arr[j])

            i +=1
            result = "".join(arr)
        
        return result[-1]

        






solution = Solution()
solution.countAndSay(5)
