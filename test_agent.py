from services.agent_service import ask_agent

question = input("Preguntá: ")

response = ask_agent(question)

print("\n🤖 RESPUESTA:\n")

print(response)