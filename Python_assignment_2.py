#Q-1 Python Program for n-th Fibonacci number
#recursive approach
def Fibonacci(n):
   if n<0:
      print("Fibbonacci can't be computed")
   # First Fibonacci number
   elif n==1:
      return 0
   # Second Fibonacci number
   elif n==2:
      return 1
   else:
      return Fibonacci(n-1)+Fibonacci(n-2)
# main
n=10
print(Fibonacci(n))

#Q-2 Python Program for How to check if a given number is Fibonacci number?
import math as m  
   
# Here, we will create a utility function that will return true if K is a perfect square  
def is_Perfect_Square(K):  
    s = int(m.sqrt(K))  
    return s * s == K  
   
# Now, we will create a function which will return "true" if R is a Fibinacci Number,   
# else it will return "false"  
def is_Fibonacci(R):  
   
    # R is a Fibinacci number only if one of (5 * R * R + 4) or (5 * R * R - 4) or both   
   # of them are perferct square  
    return is_Perfect_Square(5 * R * R + 4) or is_Perfect_Square(5 * R * R - 4)  
      
# Now, we will create a utility function for testing the above functions  
for J in range(1, 22):  
     if (is_Fibonacci(J) == True):  
         print ("Number:", J, ": Yes, the given number is a Fibonacci_Number")  
     else:  
         print ("Number:", J, ": No, the given number is not a Fibonacci_Number")  

#Q-3 Python Program for n\’th multiple of a number in Fibonacci Series

# find function
def find(k, n):
   f1 = 0
   f2 = 1
   i =2;
   #fibonacci recursion
   while i!=0:
      f3 = f1 + f2;
      f1 = f2;
      f2 = f3;
      if f2%k == 0:
         return n*i
      i+=1
   return
# multiple of which number
n = 5;
# number
k = 4;
print("Position of n\'th multiple of k in""Fibonacci Series is: ", find(k,n));

#Q-4 Program to print ASCII Value of a character

# Python program to print 
# ASCII Value of Character
  
# In c we can assign different
# characters of which we want ASCII value 
  
c = 'g'
# print the ASCII value of assigned character in c
print("The ASCII value of '" + c + "' is", ord(c))

#Q-5 Python Program for Sum of squares of first n natural numbers

def sqsum(n) :
   sm = 0
   for i in range(1, n+1) :
      sm = sm + pow(i,2)
   return sm
# main
n = 5
print(sqsum(n))

#Q-6 Python Program for cube sum of first n natural numbers
def sumOfSeries(n):
   sum = 0
   for i in range(1, n+1):
      sum +=i*i*i
   return sum
# Driver Function
n = 3
print(sumOfSeries(n))

#Q-7 Python Program to find sum of array

# Python 3 code to find sum 
# of elements in given array 
def _sum(arr): 
      
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum=0
      
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
          
    return(sum) 
  
# driver function 
arr=[] 
# input values to list 
arr = [12, 3, 4, 15] 
  
# calculating length of array 
n = len(arr) 
  
ans = _sum(arr) 
  
# display sum 
print ('Sum of the array is ', ans) 

# Q-8 Python Program to find largest element in an array

# Python3 program to find maximum
# in arr[] of size n 
  
# python function to find maximum
# in arr[] of size n
def largest(arr,n):
  
    # Initialize maximum element
    max = arr[0]
  
    # Traverse array elements from second
    # and compare every element with 
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
  
# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)

#Q-9 Python Program for array rotation

# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
 
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))

#Q-10 Python Program for Reversal algorithm for array rotation?
def reverseArray(arr, start, end):
    while (start < end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1
  
def Rotate(a, d):
    if d == 0:
        return
    n = len(a)
    d = d % n
    reverseArray(a, 0, d-1)
    reverseArray(a, d, n-1)
    reverseArray(a, 0, n-1)
  
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i],end=" ")
  
a= [10, 20, 13, 24, 53, 6, 17]
n = len(a)
d = 2
printArray(a)  
Rotate(a, d)
print("\nShifted array: ")  
printArray(a)


#Q-11 Python Program to Split the array and add the first part to the end

def SplitArray(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = x		
arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
	print(arr[i], end = ' ')
    