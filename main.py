# import important libraries
import os

# initiate variables
NumberOfStudents = 0
InputFileName = "ResultsData.csv"
OutputFileName = "OutputInformation.txt"
# initiate two list to hole the name and scores
Names = []
Scores = []

# the following lines to be used to get the current working directory and change the location to it to get the ResultsSata.csv file.
cwd = os.path.dirname(os.path.abspath(__file__))
# the following print is to check the value
# print(cwd)
# change the directory to the current folder where we at
os.chdir(cwd)
# to open the file with data use the following
csv_file = open(InputFileName, "r")
# And put it into an array/list
reading = csv_file.readlines()
# open or create the output folder
new_file = open("OutputInformation.txt", "w")
# writing values to the list and prepare them
for Line in reading:
    StudentLine = Line.strip()
    # Separate the Name and Score values See: https://www.w3schools.com/python/ref_string_split.asp
    StudentAndResult = StudentLine.split(",")
    # Append them to the appropriate Lists
    Names.append(StudentAndResult[0])
    Scores.append(float(StudentAndResult[1]))
    # Increase the number of students
    NumberOfStudents = NumberOfStudents + 1

# adding the word scored to the name
scored = " scored "
name_scored = [ items + scored for items in Names]
#print(name_scored)
# making scors as string to join it with the names
strscore = Scores
strscore = [str(Scores) for Scores in strscore]
#print(strscore)
#join the two striings
combine = [name_scored + strscore for name_scored, strscore, in zip(name_scored, strscore)]
# writing to the output
with open(OutputFileName, 'w') as OP:
    for items in combine:
        OP.write(items)
        OP.write('\n')

#closing the opened files
new_file.close()
csv_file.close()

# printing results
print ("Reading information from: ",  InputFileName)

print (NumberOfStudents, " records output to: ", OutputFileName)
