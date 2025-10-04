 # number of test cases


N = int(input("enter the number of students => "))
R = int(input("enter the number of records => "))
print("N =", N, "R =", R)

ids = list(map(int, input("enter the student ids (space-separated) => ").split()))
codes = list(map(int, input("enter the subject codes (space-separated) => ").split()))

d = dict(zip(ids, codes))   # pair ids with codes
print("Dictionary is:", d)  


student_subjects = {}
for i in range(R):
    student_id = ids[i]
    subject_code = codes[i]

    # If student not in dictionary, add with empty list
    if student_id not in student_subjects:
        student_subjects[student_id] = []

    # Add the subject to that student's list
    student_subjects[student_id].append(subject_code)

print("Dictionary is:", student_subjects)
