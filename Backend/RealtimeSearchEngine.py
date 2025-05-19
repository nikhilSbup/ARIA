from googlesearch import search
from groq import Groq   # Import the Groq liberary to use its API.
from json import load, dump     # Importing functions to read and write Json files.
import datetime     # Importing the datetime module for real-time date and time information.
from dotenv import dotenv_values    # Importing dotenv_values to read enviornment variables from a .env file.

# Load environment variables from the env. file.
env_vars = dotenv_values(".env")

#Retrieve specific environment variables for username, assistant name, API key.
Username= env_vars.get("Username")
Assistantname =env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

# Initialize the Groq Client Using the Provided API Key.
client = Groq(api_key=GroqAPIKey)

# Define the system instructions for the chatbot.
System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Just answer the question from the provided data in a professional way. ***"""

# Try to load chat log from a JSON file, or create an empty one if it doesn't exist.
try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except:
    with open(r"Data\ChatLog.json","w") as f:
        dump([], f)

#function to perform a Google search and format the results.
def GoogleSearch(query):
    results = list(search(query, advanced=True, num_results=5))
    Answer = f"The search results for '{query}' are: \n[start]\n"

    for i in results:
        Answer += f"title: {i.title}\nDescription: {i.description}\n\n"

    Answer += "[end]"
    return Answer

# Function to clean up the answer by removing empty lines.
def AnswerModifier(Answer):
    lines= Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

# Predefined chatbot conversation system message and an initial user message.
SystemChatBot = [
    {"role": "system","content":System},
    {"role": "user","content": "Hi"},
    {"role": "assistant","content":"Hello, how can I help You?"}
] 

# Function to get real-time information like the current date and time.
def Information():
    data =""
    current_date_time = datetime.datetime.now()     # Get the current date and time.
    day = current_date_time.strftime("%A")      # Day of the week.
    date = current_date_time.strftime("%d")     # day of the month.
    month = current_date_time.strftime("%B")    # Full month name.
    year = current_date_time.strftime("%Y")      # year.
    hour = current_date_time.strftime("%H")     # Hour in 24-hour format.
    minute = current_date_time.strftime("%M")   # minute.
    second = current_date_time.strftime("%S")   #Second.
    data += f"Use This Real-time Information if needed:\n"
    data += f"Day: {day}\n"
    data += f"Date: {date}\n"
    data += f"Month: {month}\n"
    data += f"Year: {year}\n"
    data += f"Time: {hour} hours, {minute} minutes, {second} seconds.\n"
    return data

#Function to handle real-time search and response generation.
def RealTimeSearchEngine(prompt):
    global SystemChatBot, messages

    # Load the chat log the JSON file.
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
    messages.append({"role":"user","content":f"{prompt}"})

    # Add Google search results to the system chatbot messages.
    SystemChatBot.append({"role":"system","content":GoogleSearch(prompt)})

    # Generate a response using the Groq Client.
    completion =client.chat.completions.create(
        model= "llama-3.3-70b-versatile",
        messages=SystemChatBot + [{"role": "system", "content": Information()}] + messages,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        stream=True,
        stop=None
    )

    Answer = ""

    # Concatenate response chunks from the streaming output.
    for chunk in completion:
        if chunk.choices[0].delta.content:
            Answer += chunk.choices[0].delta.content
   
    # Clean up response.
    Answer = Answer.strip().replace("</s>", "")
    messages.append({"role":"assistant","content": Answer})

    # Save the updated chat log back to the JSON file.
    with open (r"Data\ChatLog.json", "w") as f:
        dump(messages, f, indent=4)

    # Remove the most recent system message from the chatbot conversation
    SystemChatBot.pop()
    return AnswerModifier(Answer=Answer)
# Main entry point of the program for interactive querying.
if __name__ == "__main__":
    while True:
        prompt =input("Enter your query: ")
        print(RealTimeSearchEngine(prompt))