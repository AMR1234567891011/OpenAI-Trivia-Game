import openai
import getpass
import time

#Trivia python game which is powered by openai
width = 236#amount of chars on one line of cm
gameLength = 10
Topics = "Geography History Science Politics Music Art Math Pop-Culture"
moreTopics = ""#User input topics
teamCount = 4 #Number of participating teams
difficulty = "normal"
Teams = []#Should be an array of dicitonaries containing the team name and team score
Questions = []#["How many Letters in the Alphabet", "What is the capitial of Texas", "What is the biggest volcano"]#an array of questions to be asked



def generate():
    print("AI: Now generating questions. Please wait a few seconds")
    prompt = "generate "+gameLength+" trivia questions of a "+ difficulty+ "difficulty, on the topics of " + Topics + ". format the questions as a numbered list from 1-40 do not give the topic headers and do not include anything else. Only generate "+gameLength+" questions."
    raw = chat(prompt)
    return raw.split("\n")

def check(answer,x):
    prompt = "on a scale from 0-100 how close is the answer '"+answer+"' for the question "+Questions[x]+ "only give a number from 0-100 do not answer with any words"
    num = chat(prompt)
    return num

def answer(x):
    prompt = "what is the best answer for the question "+ Questions[x]
    return chat(prompt)

openai.api_key = "KEY GOES IN HERE"
def chat(prompt):#An Example of a normal chat 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    print("##################  Welcome to Trivia !  ##################")
    flag = True
    while flag:
        try:
            teamCount =  input("AI: Please enter the number of teams participating:")
            num = int(teamCount)
        except ValueError:
            print("AI: That was not a number.")
            flag = True
        else:
            flag = False
            Teams = [{"name":"none","score":0,"answer":0}for x in range(int(teamCount))]
    for x in range(int(teamCount)):
        Teams[x]["name"] = input("AI: please enter team name: ")
    
    flag = True
    while flag:
        try:
            gameLength =  input("AI: Please enter the number of questions asked:")
            num = int(gameLength)
        except ValueError:
            print("AI: That was not a number.")
            flag = True
        else:
            flag = False

    moreTopics = input("AI: The base topics are Geography, History, Science, Biology, Politics, Music, Art, and Math. Please enter any other topics(space seperated). \nAI: Type here:")
    difficulty = input("AI: Please choose between easy, normal, and hard for your difficulty. \nAI: Type here: ")
    Topics+=moreTopics
    Questions = generate() 
    i = 0
    for x in Questions:
        if i>=int(gameLength):
            break
        print("\n\n\nAI: # Question Number "+x+ "\nAI: teams now have 10 seconds to come up with an answer #")
        time.sleep(10)
        for y in range(int(teamCount)):
            guess = getpass.getpass("AI: Team "+ Teams[y]["name"] +" please enter your answer: ")
            Teams[y]["score"]+=int(check(guess,i))
        print("AI: The correct answer was "+answer(i))
        for y in range(int(teamCount)):
            print("AI: ## Team "+Teams[y]["name"]+" you have "+str(Teams[y]["score"])+" points. ##")
        i += 1
    print("\n\n\nAI: ##### Game Finished! #####")
    for y in range(int(teamCount)):
            print("AI: Team "+Teams[y]["name"]+" you have "+str(Teams[y]["score"])+" points.")
    input("Press Enter to End")
