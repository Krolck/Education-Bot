choices = [
    'View the Schedule ',
    'View Announcements ',
    'View your Grades ',
    'Quit ',
]


schedule = {
'Sunday' : 'No Event',
'Monday' : 'Number Sense Meet',
'Tuesday' : 'Band Rehearsal, PIF Meet',
'Wednesday' : 'Band Rehearsal, Pep Rally',
'Thursday' : 'Band Rehearsal',
'Friday' : 'Football Game @Vandigrift HS',
'Saturday' : 'Band Competition',
}


grades = {
'Math' : 100,
'Science' : 60,
'English' : 85,
'Computer Science' : 100,
'History' : 80,
}


announcements = 'Hello students,\nThere will be free chicken nuggets in the cafeteria all week!\nHave a great week!\n-Mr. Principal'




userName = input('Hello, my name is Bob, and I am an AI Chatbot. What is your name? ')




while True:
    print(f'\nHow many I assist you, {userName}?')
    for i, v in enumerate(choices):
        print(f'\n-{v}: {i + 1}')


    action = int(input())


    if action == 1:
        for day in (schedule):
            print(f"\n{day} - {schedule[day]}")

    elif action == 2:
        print(announcements)

    elif action == 3:
        avg = 0
        for subject in (grades):
            avg += grades[subject]
            print(f"\n{subject} - {grades[subject]}")

        avg /= len(grades)
        print(f"\nAverage: {avg}")
         
    elif action == 4:
        print(f'Goodbye {userName}. Have a wonderful day!')
        break






