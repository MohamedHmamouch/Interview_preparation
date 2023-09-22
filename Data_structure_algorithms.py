
from typing import List
def TwoSum(L:List,target:int)-> List:

    dict_diff={}

    for i, n in enumerate(L):

        diff=target-n

        if diff in dict_diff:

            return [dict_diff[diff],i]
        else:

            dict_diff[n]=i


def is_palindrome(x:int)-> bool:

    if x<0:
        return False
    
    div=1
    while x>=div*10:
        div=div*10

    while x!=0:

        if x%10!=x//div:
            return False
        
        x=(x%div)//10
        div=div/100
    return True


def LongestCommonPrefix(s):

    new_str=""

    for i in range(len(s[0])):

        for l in s:

            if i==len(l) or s[0][i]!=l[i]:

                return new_str
            
            else: 
                new_str+=s[0][i]



    return new_str


def FindDuplicate(nums:List):

    res=[]

    for i in nums:

        index=i-1
        nums[index]=-1*abs(nums[index])

    
    for i,n in enumerate(nums):

        if n>0:

            res.append(i+1)

    return res


def remove_duplicated(nums:List):

    c=1

    for i in range(1,len(nums)):

        if nums[i-1]!=nums[i]:

            nums[c]=nums[i]
            c+=1

    return c


def insertion_sort(l):
    
    for i in range(len(l)):

        for j in range(i):

            if l[i]<=l[j]:

                l[i],l[j]=l[j],l[i]
                print(*l)

    return l

def QuickSort(L):

    if len(L) <= 1:
        return L

    left_array,right_array,equal_array=[],[],[]

    pivot=L[-1]


    for i in L:

        if i<pivot:

            left_array.append(i)
        elif i>pivot:

            right_array.append(i)

        elif i==pivot:

            equal_array.append(i)

    return QuickSort(left_array)+equal_array+QuickSort(right_array)


def MergeSort(L):


    if len(L)>1:

        left_array=L[:len(L)//2]

        right_array=L[len(L)//2:]


        MergeSort(left_array)
        MergeSort(right_array)


        i,j,k=0,0,0

        while i <len(left_array) and j<len(right_array):

            if left_array[i]<right_array[j]:

                L[k]=left_array[i]

                i+=1
            else:

                L[k]=right_array[j]

                j+=1

            k+=1
        while i <len(left_array):

            L[k]=left_array[i]
            k+=1
            i+=1

        while j <len(right_array):

            L[k]=right_array[j]

            k+=1
            j+=1

    return L


def separateNumbers(s):
    
    
    l=[]
    
    for i in range(len(s)-1):
        
        if s[i]==s[i+1] or s[i+1]=='0':
            
            l.append(s[i]+s[i+1])
            
        elif s[i]!='0':
            
            l.append(s[i])

    return l 


from functools import reduce

    
def pgcd(a,b):
        
    if b==0:
            
            return a
    return pgcd(b,a%b)
    
def ppcm(a,b):
        
    return (a*b)/pgcd(a,b)
    

        
def circular_array(l,k):

    result=[0]*len(l)
    for i in range(len(l)):
        
        rotated_index=(i+k)%len(l)
        print("i%k",i+k)
        print(rotated_index)
        result[rotated_index]=l[i]

    return result
     

def extraLongFactorials(n):
 
    if n==0:
        return 1
    elif n>0:
        
       return n*extraLongFactorials(n-1)
    


def LargestPermutation(A,k):


    index={} #element:index

    for i in range(len(A)):

        index[A[i]]=i

    
    i,swap=0,0
    n=len(A)

    while i <len(A) and swap<k:

        #puisque les valeurs de A sont incrémenté par

        #donc larget est de vérifier si A{i}<n-i

        if A[i]<len(A)-i:

            id=index[n-i]

            A[i],A[id]=A[id],A[i]

            index[n-i]=i
            index[A[id]]=id

            swap+=1

        i+=1

    return A


def nonDivisibleSubset(k, s):
    # Write your code here
    repeated_count=[0]*k
    
    for i in s:
        
        remainder=i%k
        
        repeated_count[remainder]+=1
    ans=min(repeated_count[0],1)
    
    if k%2==0:
        
        ans+=min(repeated_count[k//2],1)
        
    for i in range(1,k//2+1):
        
        if i!=k-i:
            
            ans+=max(repeated_count[i],repeated_count[k-i])
            
    return ans


def minimumLoss(price):
    # Write your code here
    # O(n^2)
    # i=0
    min_loss=float('inf')
    # while i<=len(price)-2:
        
    #     for j in range(i+1,len(price)):
            
    #         if price[i]>price[j]:
                
    #             min_loss=min(min_loss,price[i]-price[j])
                
    #     i+=1
        
    # return min_loss

    n=len(price)

    l,r=0,1

    price.sort()

    while r<n:

        if -price[r]+price[l]<min_loss:

            min_loss=price[l]-price[r]

            l+=1

        r+=1

    return min_loss

if __name__=='__main__':

    print(minimumLoss([5,10,3]))



    
    



