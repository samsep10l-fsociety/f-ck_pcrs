#Designed and Engineered by samsep10l --fsociety

from openai import OpenAI
import os
import json
from Scrape_PCRS import get_formatted_questions
from dotenv import load_dotenv
load_dotenv()


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    assistant_id = os.getenv("ASSISTANT_ID")
    # Get the formatted questions
    formatted_questions = get_formatted_questions()
    disclaimer = """
    Disclaimer:
    Hey there, friend. Saul Goodman here. 
    Before you dive into this code, let's get something straight. 
    This code is provided for educational and informational purposes only. 
    If you decide to use it to cut corners, bend the rules, or, dare I say, cheat—that's all on you. 
    I'm just the guy providing the tools; how you use them is your business. 
    Remember, consequences are like gravity—inevitable. 
    So if you find yourself in a sticky situation because of how you used this code, don't come knocking on my door. 
    I'm not liable for any mischief you get into. 
    Use wisely and responsibly.
                """
    print(disclaimer)
    file_name = input("Naming Format = 'WEEK_#__NAME_OF_EXERCISE' \nExercise NAME?: ")
    print(file_name)
    # Open the file to write the answers
    with open(f"{file_name}.txt", "w") as file:
        for question_title, question_content in formatted_questions:
            print(f"Processing question: {question_title}")
            # Get the assistant's answer
            print(f"Question Content: {question_content}")
            answer = process_pcrs_question(client, assistant_id, question_content)
            if answer:
                # Write the question title and the answer to the file
                file.write(f"{question_title}:\n")
                file.write("ANSWER:\n")
                file.write(f"{answer}\n\n")
                file.write("#Designed and Engineered by samsep10l --fsociety\n\n")
            else:
                print(f"No answer for question: {question_title}")


def process_pcrs_question(client, assistant_id, question_content):
    print("Processing question...")
    
    # Create a new thread
    thread = client.beta.threads.create()
    thread_id = thread.id

    # Send the question content to the assistant
    client.beta.threads.messages.create(thread_id=thread_id, role="user", content=question_content)
    
    # Run the assistant and wait for completion
    run = client.beta.threads.runs.create_and_poll(thread_id=thread_id, assistant_id=assistant_id)

    if run.status == "completed":
        # Retrieve the assistant's reply
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        assistant_reply = messages.data[0].content[0].text.value
        print(assistant_reply)
        # Attempt to parse the reply as JSON
        try:
            reply_json = json.loads(assistant_reply)
            # Format the JSON reply with indentation
            formatted_reply = json.dumps(reply_json, indent=2)
            return formatted_reply
        except json.JSONDecodeError:
            # If the reply is not valid JSON, return it as is
            return assistant_reply
    else:
        print(f"Run failed with status: {run.status}")
        return None

if __name__ == "__main__":
    main()
