from fastapi import FastAPI
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground, serve_playground_app
import os
import uvicorn

# Configurar o agente com OpenAI (é preciso definir OPENAI_API_KEY como variável de ambiente)
agent = Agent(
    name="Meu Primeiro Agente",
    agent_id="primeiro-agente",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Você é um assistente útil.",
        "Responda as perguntas de forma clara e concisa.",
    ],
    markdown=True,
)

# Criar o playground da Agno para interface de usuário
app = Playground(agents=[agent]).get_app()

if __name__ == "__main__":
    # Obter a porta do ambiente ou usar 7777 como padrão
    port = int(os.environ.get("PORT", 7777))
    # Iniciar o servidor
    uvicorn.run(app, host="0.0.0.0", port=port)
