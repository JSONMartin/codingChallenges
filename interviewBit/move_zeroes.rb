# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
  i = 0
  while i < nums.length
    if nums[i] === 0
      if nums[i..nums.length].reduce(:+) == 0
        break
      end
      nums.push(nums.slice!(i))
      i-=1
    end
    i+=1
  end

  return nums
end

#move_zeroes([0, 1, 0, 3, 12])
puts move_zeroes([0,0,1]).to_s
