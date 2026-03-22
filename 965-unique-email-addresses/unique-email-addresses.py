class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        s=set()

        for email in emails:

            local_name,domain_name=email.split('@')

            plus_char='+'
            periods='.'

            if plus_char in local_name:

                local_name=local_name.split('+')[0]

    

            local_name=''.join([s for s in local_name if s!=periods])

            email=local_name+'@'+domain_name

            s.add(email)

        print(s)

        return len(s)
        