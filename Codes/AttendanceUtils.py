'''
Attendance Utils
'''

# Imports
import os
import pandas

# Main Functions
def ReadCSV(path):
    '''
    Reads CSV file and returns a pandas dataframe
    '''
    return pandas.read_csv(path)

def SaveCSV(df, path):
    '''
    Saves a pandas dataframe to a CSV file
    '''
    df.to_csv(path)

def Parse_AttendedStudentRollNums(attendedStudentNames):
    '''
    Parses the attended student names and returns a list of roll numbers
    '''
    rollNums = []
    for studentName in attendedStudentNames:
        studentName = studentName.strip()
        rollNums.append(studentName.split(" ")[-1])
    return rollNums

# Driver Code
# Params
studentsDataPath = "StartFiles/StudentsData.csv"
attendancePath = "Week_1/Attendance of 28-01-2022, 02-43 PM.csv"

studentsData_NamesRowStartIndex = 5
# Params

# RunCode
# Read Student Data
studentsData = ReadCSV(studentsDataPath)
# Read Attendance
attendance = ReadCSV(attendancePath)

# Get Student Roll Numbers
studentRollNumbers = [r.upper() for r in studentsData["RollNo"]]
# Get Attended Student Names
attendedStudentNames = [r.upper() for r in attendance.iloc[studentsData_NamesRowStartIndex:][attendance.columns[0]]]
attendedRollNumbers = Parse_AttendedStudentRollNums(attendedStudentNames)

# print(studentRollNumbers)
# print(attendedRollNumbers)

# Display
print("DD Students:", len(studentRollNumbers))
print("Attended Students:", len(attendedRollNumbers))

# Find Common Students
attendedStudentsInData = set(attendedRollNumbers).intersection(set(studentRollNumbers))
print("Common Students:", len(attendedStudentsInData))
print(attendedStudentsInData)
print()

# Final Names
print("Final Names:")
finalCommonNames = []
for rollNum in attendedStudentsInData:
    name = attendedStudentNames[attendedRollNumbers.index(rollNum)]
    finalCommonNames.append(name)
    print(name)