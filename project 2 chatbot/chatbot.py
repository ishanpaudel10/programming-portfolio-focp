import random
import json


def read_from_json():
    with open("keyword_file.json",'r') as f:
        data=json.load(f)
        return data

def agent_name():
    ls=['Messi','Ronaldo','Elon','Gabriel','Aristotle','Neymar','Suarez','Donald']
    return random.choice(ls)

def log_conversation(person,person_msg,agent_name,res):
    with open('log.txt','a') as f:
        f.write(f"{person}:{person_msg}\n")
        f.write(f"{agent_name}:{res}\n\n\n")

def end_of_chat():
    chat_end=['bye','exit','quit','end']
    return chat_end


def main():

    responses=read_from_json()
    agent_ls=agent_name()
    chatting_end=end_of_chat()
    

    print("Welcome to the University of Poppleton ChatBot") 
    user=input("What is your name: ").capitalize().strip()
    print(f"Hello {user} its nice to meet you I am your friendly chatbot {agent_ls}. How can I help you today?") 

    while True:
        user_msg=input(f'{user}: ').lower().strip()

        if user_msg in chatting_end:
            print(f'{agent_ls}: Bye! Have a great day {user}')
            break

        elif random.random()<0.05:
            print(f"{agent_ls}: Oops! Something is happening. Try again later ):")
            break
        
        
        response=None
        for key,val in responses.items():
            if key in user_msg:
                response=random.choice(val)
                
            elif response==None:             
                fixed=responses.get("random responses")
                response=random.choice(fixed)
               
    
        print(f"{agent_ls}:{response}")

        log_conversation(user,user_msg,agent_ls,response)



if __name__=="__main__":
    main()
