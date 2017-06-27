class Solution(object):
    def sortColors(self, nums):
        return self.insertionSort(nums)
        #return self.selectionSort(nums)
        #return self.bubbleSort(nums)
        #return self.mergeSort(nums) # Works, but is not in place
    
    # Insertion Sort
    def insertionSort(self, nums):
        LENGTH = len(nums) - 1
        i = 1

        while i <= LENGTH:
            print(nums)
            if nums[i] < nums[i - 1]:
                # Find the place in in the array to swap
                j = 0
                while j <= LENGTH:
                    if nums[i] <= nums[j]:
                        nums.insert(j, nums.pop(i))
                        nums.insert
                        break
                    j += 1
            i += 1
        
        print(nums)

    # Selection sort
    def selectionSort(self, nums):
        LENGTH = len(nums) - 1
        i = 0
        
        while i <= LENGTH:
            j = i + 1
            minVal = nums[i]
            minIdx = i

            while j <= LENGTH:
                if nums[j] < minVal:
                    minVal = nums[j]
                    minIdx = j
                j += 1
            
            if i != minIdx:
                nums[i], nums[minIdx] = nums[minIdx], nums[i]
            
            i += 1
        
        print(nums)



    # Merge Sort (Works, but is not in place)
    def mergeSort(self, nums):
        LENGTH = len(nums)

        def merge(left, right):
            LEFT_LENGTH = len(left); RIGHT_LENGTH = len(right)
            
            #print(left, right)
            if LEFT_LENGTH > 1:
                left = merge(left[0:LEFT_LENGTH // 2], left[LEFT_LENGTH // 2:])
            if RIGHT_LENGTH > 1:
                right = merge(right[0:RIGHT_LENGTH // 2], right[RIGHT_LENGTH // 2:])

            #print("FINAL:")
            #print(left, right)
            
            LEFT_LENGTH = len(left); RIGHT_LENGTH = len(right)
            sortedList = []
            i, j = 0, 0
            while i < LEFT_LENGTH and j < RIGHT_LENGTH:
                if left[i] <= right[j]:
                    sortedList.append(left[i])
                    i += 1
                else:
                    sortedList.append(right[j])
                    j += 1
            
            while i < LEFT_LENGTH:
                sortedList.append(left[i])
                i += 1
            
            while j < RIGHT_LENGTH:
                sortedList.append(right[j])
                j += 1
            
            return sortedList

        nums = merge(nums[0:LENGTH // 2], nums[LENGTH // 2:])
        #print("FINAL END RESULT!!!")
        print(nums)

    # Bubble Sort
    def bubleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        done = False

        while not done:
            print(nums)
            done = True

            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i] # Swap
                    done = False
        
        print(nums)

#Solution().sortColors([1, 0])
Solution().sortColors([1, 0, 0, 1, 2, 2, 0, 1])
