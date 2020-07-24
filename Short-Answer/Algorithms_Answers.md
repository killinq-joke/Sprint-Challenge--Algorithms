#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) while a < n * n * n: #this should be O(3n)
    a += n * n #but because of this line we can do (n * n * n / n * n == n)

#And because of that, the runtime complexity of this algorithm is O(n)

b) sum = 0 #this doesn't matter
    for i in range(n): #O(n)
      j = 1
      while j < n: #this depends on how j increases
        j *= 2 #since j *= 2, the while loop above turns into a O(log n)
        sum += 1

#The runtime complexity of this algorithm is O(n log n) since log n is nested in n (n * log n)


c)
def bunnyEars(bunnies): #considering that bunnies are >= 0
      if bunnies == 0: #O(1)
        return 0

      return 2 + bunnyEars(bunnies-1) #loops through each "n" aka "bunnies"

This function considering bunnies >= 0 is an O(n) else it is an O(infinite) which isn't that good :/
    

## Exercise II

mid = n // 2
throw and egg at mid
if it breaks:
    mid becomes mid // 2
else (doesn't break):
    mid becomes mid + mid // 2


