student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)

print(total_exam_score)

sum = 0

for score in student_scores:
    sum += score

print(sum)

#PAUSE 1 - Max
total_max_score = max(student_scores)
print(total_max_score)

max_score = 0

for current_score in student_scores:
    if current_score > max_score:
        max_score = current_score

print(max_score)

