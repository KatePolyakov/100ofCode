programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
#Bug - key
#An error in a program that...- value

#retrieve items from a dictionary
#search_word = input('What word you would like to know?: ').capitalize()
#print(programming_dictionary[search_word])

#create an empty dictionary:
my_empty_dictionary = {}

#add new items to an existing dictionary:
#search_word['Logo'] = 'Company\'s label'

#edit an existing value in a dictionary:
#search_word['Logo'] = 'Company\'s photo'

#loop through a dictionary and print all the keys:
#for key in programming_dictionary:
    #print(key)
    #print(programming_dictionary[key])

#Grading Program

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}




for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"

print(student_grades)