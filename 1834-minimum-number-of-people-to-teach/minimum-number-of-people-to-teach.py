class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:


        set_languages=[set(l) for l in languages]

        print(set_languages[0])

        bad_users=set()

        for u,v in friendships:

            u_lang=set_languages[u-1]
            v_lang=set_languages[v-1]

            if u_lang.isdisjoint(v_lang):

                bad_users.add(u)
                bad_users.add(v)

        
        min_to_learn=float('inf')

        for lan in range(1,n+1):

            count=0

            for user in bad_users:


                if lan not in set_languages[user-1]:

                    count+=1

            min_to_learn=min(min_to_learn,count)

        return min_to_learn