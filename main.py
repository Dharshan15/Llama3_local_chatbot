from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Convo history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model #piping - output of the prompt is fed into the model

def handle_convo():
    context = ""
    print("Welcome to the bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context": context,"question": user_input})
        print("Bot: ",result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_convo()
