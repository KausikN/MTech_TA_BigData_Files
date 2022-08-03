'''
TA Mapping
'''

# Imports
import math
import numpy as np
import pandas as pd

# Main Functions
def ReadCSV(path):
    '''
    Reads CSV file and returns a pandas dataframe
    '''
    return pd.read_csv(path)

def SaveCSV(df, path):
    '''
    Saves a pandas dataframe to a CSV file
    '''
    df.to_csv(path)

def TAMap_Random(students_df, TAs):
    '''
    Randomly assigns students to TAs
    '''
    # Copty students dataframe
    students_df = students_df.copy()

    # Calculate Student to TA ratio
    students_per_TA = int(students_df.shape[0] / len(TAs))
    # Generate TA indices
    ta_indices = []
    for i in range(len(TAs)-1):
        ta_indices.extend([i]*students_per_TA)
    ta_indices.extend([len(TAs)-1]*(students_df.shape[0] - len(ta_indices)))
    # Shuffle TA indices
    np.random.shuffle(ta_indices)

    # Print
    print("Students:", students_df.shape[0])
    print("Students per TA:", students_per_TA)
    _, ta_indices_counts = np.unique(ta_indices, return_counts=True)
    for i in range(len(TAs)):
        print("TA", i, "students:", ta_indices_counts[i])

    # Assign Students to TAs
    students_df["TA Name"] = students_df.index.map(lambda x: TAs[ta_indices[x]]["name"])
    students_df["TA Email"] = students_df.index.map(lambda x: TAs[ta_indices[x]]["email"])

    return students_df

# Driver Code
# Params
TAs = [
    {
        "name": "Person_1",
        "email": "person1@abc.com"
    },
    {
        "name": "Person_2",
        "email": "person2@abc.com"
    }
]

STUDENTS_DATA_PATH = "StartFiles/StudentsData.csv"
TA_MAP_PATH = "StartFiles/TA_Map.csv"
# Params

# RunCode
# Read Student Data
students_df = ReadCSV(STUDENTS_DATA_PATH)
# Assign TAs
students_df = TAMap_Random(students_df, TAs)
# Save
SaveCSV(students_df, TA_MAP_PATH)