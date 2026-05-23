import sys

sys.path.append("src")

from rag_chain import answer_question


while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    answer = answer_question(question)

    print("\nAnswer:\n")
    print(answer)