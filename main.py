student_score = int(input (" Enter a list of score : ").split())

for n in range(0,len(student_score)):
  student_score[n] = student_score[n]
print(student_score)   

highest_score = 0
for score in student_score :
  if score > highest_score :
    highest_score = score
print(f"The highest score is {highest_score}")  