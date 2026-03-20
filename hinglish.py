from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)

model = "llama-3.3-70b-versatile"

roles = {

    "1" : """You are a friendly Indian AI assistant.
            Always respond in Hinglish 
            (mix of Hindi and English).
            Use words like bhai, yaar, arre, 
            sahi hai, etc.
            Keep responses fun and casual!""",

    "2" : """You are a helpful Indian teacher.
            Explain concepts in simple Hinglish.
            Use examples that Indian students relate to.
            Be encouraging and say things like 
            bilkul sahi!, "bahut accha!""",

    "3" : """You are an Indian coding mentor.
            Explain code concepts in Hinglish.
            Use simple analogies from Indian daily life.
            Make coding fun and easy to understand!"""

}

temperature = {
    "1" : 0.8,
    "2" : 0.4,
    "3" : 0.3
}

print("1. Casusal Mode. ")
print("2. Padhi Mode. ")
print("3. Coding Mode. ")
choice = input("Enter Choice : ")
system = roles[choice]
temp = temperature[choice]


def user_request(message, text):
    user = {"role" : "user" , "content" : text}
    message.append(user)

def assistant_response(message, text):
    ai = {"role" : "assistant" , "content" : text}
    message.append(ai)


messages = []
messages.append({
    "role" : "system",
    "content" : system
})

while True: 
    user_input = input(">> You >_ ")

    if user_input == "exit":
        print(" BYE 👋🏻  ")
        break

    user_request(messages, user_input)

    full_response = ""

    with client.chat.completions.create(
        model = model,
        max_tokens = 250,
        messages = messages,
        stream = True 
    ) as stream :
        print(">> AI >_ " + full_response)
        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text:
                print(text , end = "", flush = True)
                full_response += text
        print()
    assistant_response(messages, full_response)
    print("------------------------------------------------------------------")