class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        counter=0
        left,right=0,len(people)-1

        while left<=right:

            total=people[left]+people[right]

            if total>limit:

                counter+=1

                right-=1


            elif total<=limit:

                left+=1
                right-=1

                counter+=1

        return counter


        