from dotenv import load_dotenv
import replicate

load_dotenv()

CLASSES = ["Data Science", "Cryptocurrency", "Bitcoin", "Poetry", "Life"]

def get_prompt(input_data, classes=CLASSES):
    prompt = f'''Classify to which class does the data belong, classes - {", ".join(CLASSES)}. Assume single classification. Text to classify - {input_data}. Just output the class name.'''
    return prompt

def get_response(prompt):

    output = replicate.run(
    "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
    input={
        "debug": False,
        "top_k": 50,
        "top_p": 1,
        "prompt": prompt,
        "temperature": 0.5,
        "max_new_tokens": 50,
        "min_new_tokens": -1
        }
    )

    answer = [item for item in output]
    answer = "".join(answer).strip().split(".")[0]

    return answer