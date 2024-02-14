import json
from difflib import get_close_matches

def load_db(file_path: str)-> dict:
    with open (file_path,"r") as file:
        data : dict = json.load(file)
    return data

def save_db(file_path: str, data: dict):
    with open(file_path,"w") as file:
        json.dump(data,file,indent=2)

def find_best_match(user_question: str, questions: list[str]) ->str | None:
    #cutoff : accuracy here we have an accuracy of 65%
    #n defines the number of responses.
    matches: list = get_close_matches(user_question,questions,n=1,cutoff=0.65)
    return matches[0] if matches else None

def get_answer(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def main():
    knowledge_base: dict = load_db('knowledge_base.json')

    while True:
        user_input: str = input('Vous : ')
        if user_input.lower() == 'quitter':
            print('Jeko : Au revoir !')
            break

        best_match: str | None = find_best_match(user_input, [q["question"]for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer(best_match, knowledge_base)
            print(f'Jeko: {answer}')
        else:
            print("Jeko : Désolée, je ne comprends pas votre question. Pouvez-vous reformuler ?") 

if __name__ == "__main__":
    print("Bonjour monde ! Je suis Jeko, votre assistant virtuel. Comment puis-je vous aider ? (Tapez 'quitter' pour quitter)")
    main()
