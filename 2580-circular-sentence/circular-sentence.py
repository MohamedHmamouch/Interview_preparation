class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        

        sentence_list=sentence.split(' ')
        print(sentence_list)
        print(len(sentence_list))

        if len(sentence_list)==1:

            first=sentence_list[0][0]

            end=sentence_list[0][-1]

            print(first,end)

            if first.lower()==end.lower():

                return True

            else:
                return False


        left,right=0,1

        while right<len(sentence_list):

            left_sentence=sentence_list[left]

            right_sentence=sentence_list[right]

            if left_sentence[-1]!=right_sentence[0]:

                return False


            right+=1
            left+=1

        print(sentence_list[left][-1],sentence_list[0][0])

        return False if sentence_list[left][-1]!=sentence_list[0][0] else True