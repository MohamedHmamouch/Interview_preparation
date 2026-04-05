class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        

        skill.sort()

        seen=set()

        l=0
        r=len(skill)-1

        res=0

        while l<r:

            total_skill=skill[r]+skill[l]

            seen.add(total_skill)

            if len(seen)>1:

                return -1

            else:

                res+=skill[r]*skill[l]
                r-=1
                l+=1
        return res