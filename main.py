from secrets import choice
import json

with open('config.json') as json_data:
    parsedFile = json.load(json_data)

def pickSubjectType():
    "Returns an index for the subject type that user decided to study.\nThe index indicates one the json hashmap keys (a subject type) which are specified in the config file."
    print("Which subject type would you like to study today:")

    correctlyInputted = False
    while correctlyInputted == False:
        try:
            for i in range(len(parsedFile)):
                print(i, "-", list(parsedFile.keys())[i])
            return int(input("\n=> "))
        except:
            print("\nNOTE: To choose a subject, type that number next to it.")

def generateSubject(subjectTypeIndex):
    "Randomly returns the subject within a specific subject type that someone may want to study."
    subjectSelected = list(parsedFile.keys())[subjectTypeIndex]
    return choice(parsedFile[subjectSelected])

print(f"\nYou can revise: {generateSubject(pickSubjectType())}")
