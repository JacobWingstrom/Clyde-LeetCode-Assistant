'''
    File: Clyde.py
    Author: Jacob Wingstrom
    Description: This file is a Chat GPT wrappper named Clyde meant to assist people when they are
        doing LeetCode style questions. It uses the OpenAI API and requires the user to 
        input their API key into the api_key variable. Read the README file in order to
        set up the program. 
'''
import openai

'''
    Class: Clyde
    Description: This class represents the wrapper and initializes it into the correct
        use case 
'''
class Clyde:
    def __init__(self, api_key, description, model="gpt-4o"):
        openai.api_key = api_key
        self.model = model
        self.messages = [{"role": "system", "content": description}]

    '''
        Function: ask
        Description: takes in the user_input and messages the openAI api and returns the
            response while saving the messages
    '''
    def ask(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = openai.chat.completions.create(
            model=self.model,
            messages=self.messages
        )
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

def main():
    api_key = "INSERT OPENAI KEY HERE"
    
    file = open("Clydeinstructions.txt", "r")
    chatbot = Clyde(api_key, file.read())
    
    print("Ask Clyde a Question to Help With Your Coding Question\nType \"quit\" to Close Program.")
    question = input("Ask Clyde a Question: ")
    while (question.strip().lower() != "quit"):
        chatbot.ask(question)
        question = input("Ask Clyde a Question: ")

main()