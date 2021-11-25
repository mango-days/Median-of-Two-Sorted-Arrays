# Median of Two Sorted Arrays
# Given two sorted arrays, a[] and b[], the task is to find the median of these sorted arrays, in O(log n + log m) time complexity, when n is the number of elements in the first array, and m is the number of elements in the second array. 
# This is an extension of median of two sorted arrays of equal size problem. Here we handle arrays of unequal size also.

# Input: ar1[] = {-5, 3, 6, 12, 15} , ar2[] = {-12, -10, -6, -3, 4, 10} --------Output : The median is 3.
# Explanation : The merged array is : ar3[] = {-12, -10, -6, -5 , -3, 3, 4, 6, 10, 12, 15}, So the median of the merged array is 3

# Input: ar1[] = {2, 3, 5, 8}, ar2[] = {10, 12, 14, 16, 18, 20 } -------Output : The median is 11.
# Explanation : The merged array is : ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20 },  if the number of the elements are even, so there are two middle elements, take the average between the two : (10 + 12) / 2 = 11

array1 = [ -5, 3, 6, 12, 15 ]
array2 = [ -12, -10, -6, -3, 4, 10 ]

def re_arrange ( array1 , array2 ) :
    ans = []
    index1 = 0
    index2 = 0
    while ( index1 < len(array1) and index2 < len(array2) ):
        if array1 [index1] > array2 [index2] :
            ans.append ( array2 [index2] )
            index2 += 1
        elif array1 [index1] < array2 [index2] :
            ans.append ( array1 [index1] )
            index1 += 1
        else :   # array1[index1]==array2[index2]:
            ans.append ( array1 [index1] )
            index1 += 1
            ans.append ( array2 [index2] )
            index2 += 1
        if index1 == len(array1) :
            while index2 != len(array2) : 
                ans.append ( array2 [index2] )
                index2 += 1
        elif index2 == len(array2) : 
            while index1 != len(array1) : 
                ans.append ( array1 [index1] )
                index1 += 1
                
        if len(ans) == len(array1) + len(array2) : break
    return ( ans )
    
array = re_arrange ( array1, array2 )

if len ( array ) % 2 == 1 :
    mid = int ( len ( array ) / 2 )
    print ( array [ mid ] )
else :
    mid1 = int ( len ( array ) / 2 )
    mid2 = mid1 + 1
    avg = ( array [ mid1 ] + array [ mid2 ] ) / 2 
    print ( int ( avg ) )