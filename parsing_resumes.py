from groq import Groq
from dotenv import load_dotenv
import os

# Load GROQ_API_KEY from .env file
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("system_prompt/resume_parsing_and_skill_score.txt", "r") as file:
    system_prompt = file.read()

clear_json = input("do you want to clear the existing json file? (y/n): ")
if clear_json.lower() == 'y':
    open("parsed_resumes_with_skill_score.json", "w").close() # clear the file

main_json = {}

no_of_resumes = 30
main_json_file = open("parsed_resumes_with_skill_score.json", "w", encoding="utf-8")

def parse_resume(resume_text, system_prompt):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": resume_text
            }
        ],

        model="llama-3.3-70b-versatile"
    )

    return chat_completion.choices[0].message.content

for i in range(no_of_resumes):
    with open(f"Final_resumes_txt/Resume_of_ID_{i}.txt", "r", encoding="utf-8") as file:
        resume_text = file.read()

    parsed_resume = parse_resume(resume_text, system_prompt)
    parsed_resume_json = {i: eval(parsed_resume)} # convert string to dictionary
    main_json.update(parsed_resume_json)

main_json_file.write(str(main_json) + "\n") # write each resume's json in new line
main_json_file.close()


    