
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

    # Write your code here
    
    n=len(price)
    
    rp=price.copy()
    
    rp.sort(reverse=True)
    
    max_price=max(price)
    
    for i in range(n-1):
        
        if ((rp[i]-rp[i+1])<max_price and price.index(rp[i])<price.index(rp[i+1])):
            
            max_price=rp[i]-rp[i+1]
            
    return max_price




def highestValuePalindrome(s, n,k):


    # https://gist.github.com/Shaddyjr/cedf4da886c35e43fbf422eb2149a50b : orginal code
    

    # first count number of mismatch

    def count_mistmaches(s1,s2):

        assert len(s1)==len(s2)
        count=0

        for char_s1, char_s2 in zip(s1,s2):

            count+=char_s1!=char_s2

        return count
    

    def parse_palindromes(s):

        has_middle= len(s)%2!=0 # return True if len(s)%2==0

        center_i=len(s)//2

        left_part=s[:center_i]

        right_part=s[center_i+1:] if has_middle else s[center_i:]

        middle=s[center_i] if has_middle else ''

        return left_part, middle, right_part[::-1]
    
    final_left=''

    left_part, middle , rev_right_part=parse_palindromes(s)

    mistmaches=count_mistmaches(left_part,rev_right_part)

    if k>=n:

        return '9'*n
    if k<mistmaches:

        return '-1'
    
    
    for left_char,right_char in zip(left_part,rev_right_part):

        is_mismatch=left_char!=right_char

        count_not_9=int(left_char!='9')+int(right_char!='9')

        next_char=None

        if not is_mismatch: # if left_char==right_char

            next_char=left_char

            if k-2>mistmaches and count_not_9>0:

                k-=2

                next_char='9'
        else: # if its a mismatch

            if count_not_9==1:

                k-=1

                mistmaches-=1

                next_char='9'

            else:

                if k-2>=mistmaches-1:

                    k-=2
                    next_char=left_char

                else:

                    larger_num=max(int(left_char),int(right_char))

                    k-=1

                    mistmaches-=1
                    next_char=str(larger_num)

        final_left+=next_char

    if k and middle:

        middle='9'

    return final_left+middle+final_left[::-1]



def LCS(s1,s2):

    n,m=len(s1),len(s2)

    dp=[[0]*(m+1) for _ in range(n+1)]


    for i, c1 in enumerate(s1):

        for j , c2 in enumerate(s2):

            if c1==c2:

                dp[i][j]=1+ dp[i-1][j-1]

            else:

                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[n-1][m-1]



def connectedCell(matrix):


    def count_region(i,j):

        if i<0 or i>=rows or j>=cols or j<0 or matrix[i][j]!=1:

            return 0
        region=1

        matrix[i][j]=-1 # means visited

        for r in range(-1,2):

            for c in range(-1,2):

                if r==0 and c==0:

                    continue
                region+=count_region(i+r,j+c)

        return region 

    rows=len(matrix)

    cols=len(matrix[0])
    max_region=0

    for i in range(len(matrix)):

        for j in range(len(matrix[0])):

            if matrix[i][j]==1:

                region=count_region(i,j)

                max_region=max(max_region,region)

    return max_region



def Pairs(arr,k):


    dict_num={}
    count_difference=0

    for i in arr:

        if i in dict_num:

            dict_num[i]+=1

        else:

            dict_num[i]=1

    for i in arr:

        complement=k+i

        if (complement in dict_num and k>0) or (k==0 and dict_num[i]>1):

            count_difference+=1

    return count_difference    



def absolutePermutation(n,k):

    if k==0:return [ i for i in range(1,n+1)]

    # we need to assure that we have 2n places

    elif (2*n)%k!=0:
        return [-1]
    
    else:

        res=[None]*(n+1)

        for i in range(1,n+1):

            if res[i]==None:

                res[i]=i+k
                res[i+k]=i

    return res


def SteadyGene(gene:str):

    def extra_available(all_counts,max_nucleotide):

        for c in all_counts.values():

            if c>max_nucleotide:
                return True
        return False
    
    length_gene=len(gene)
    max_nucleotide=length_gene/4

    all_counts={"A":0,"C":0,"G":0,"T":0}

    for nucleotide in gene:

        all_counts[nucleotide]+=1

    if not extra_available(all_counts=all_counts,max_nucleotide=max_nucleotide):
        return 0
    
    right,left=0,0

    min_sub=float("inf")

    while right<length_gene:

        while right<length_gene and extra_available(all_counts=all_counts,max_nucleotide=max_nucleotide):

            nucleotide=gene[right]

            all_counts[nucleotide]-=1

            right+=1

        while left < length_gene and not extra_available(all_counts=all_counts,max_nucleotide=max_nucleotide):

            nucleotide=gene[left]
            all_counts[nucleotide]+=1

            left+=1


        min_sub=min(right-left+1,min_sub)

    return min_sub
if __name__=='__main__':
                    






    
    



