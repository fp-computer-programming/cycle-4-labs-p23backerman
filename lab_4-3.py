#this is to ask what school they go to and what their Job is
print('Enter your school')
school = input()
print('Enter your Job')
Job = input()
#If the school is longer than the job in letters, it will print School is more important, if the job is longer than the school in letters, it will print the Job is more important, if they are equal, it will print to focus on both
if school > Job:
    print('School is More important')
elif school < Job:
    print('Job is more important')
else:
    print('focus on both your job and school')

