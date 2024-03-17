

if __name__=='__main__':

    n,m=map(int,input().split())

    best_marks={}
    grades=[]

    for _ in range(n):

        marks=list(input())
        grades.append(marks)

        for i in range(len(marks)):

            best_marks[i]=max(int(best_marks.get(i,0)),int(marks[i]))
    successful_student=set()

    for i in range(len(grades)):

        for j in range(len(grades[i])):

            if int(grades[i][j])==best_marks[j]:

                successful_student.add(i)

    print(len(successful_student))