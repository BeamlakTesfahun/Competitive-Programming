# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(0,len(grades)):
        if grades[i] < 38:
            continue 
        else:
            temporary = grades[i]
            temp = temporary % 5
            if temp == 3:
                temporary += 2
                grades[i] = temporary                
            if temp == 4:
                temporary += 1
                grades[i] = temporary 
            else:
                continue
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
