class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()

        left=0

        boat=0

        right=len(people)-1

        while left<=right:


            if people[left]+people[right]<=limit:

                boat+=1

                left+=1

                right-=1

            elif people[right]<=limit:

                right-=1

                boat+=1

            else:

                left+=1

                boat+=1

        return boat
        