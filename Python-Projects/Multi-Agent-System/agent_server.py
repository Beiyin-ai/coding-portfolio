# agent_server.py
# agent_server 模組

from llama_agents import (
    AgentService,
    AgentOrchestrator,
    ControlPlaneServer,
    SimpleMessageQueue,
)
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai_like import OpenAILike

llm = OpenAILike(
    model="model-name",
    api_base="http://localhost:8880/v1",
    api_key="fake",
    context_window=128000,
    is_chat_model=True,
    is_function_calling_model=False,
)

def get_the_secret_fact() -> str:
    """Returns the secret fact."""
    return "The secret fact is: A baby llama is called a 'Cria'."

tool = FunctionTool.from_defaults(fn=get_the_secret_fact)


agent1 = ReActAgent.from_tools([tool], llm=llm)
agent2 = ReActAgent.from_tools([], llm=llm)

# 多智能體
message_queue = SimpleMessageQueue(port=8000)
control_plane = ControlPlaneServer(
    message_queue=message_queue,
    orchestrator=AgentOrchestrator(llm=llm),
    port=8001,
)
agent_server_1 = AgentService(
    agent=agent1,
    message_queue=message_queue,
    description="Useful for getting the secret fact.",
    service_name="secret_fact_agent",
    port=8002,
)
agent_server_2 = AgentService(
    agent=agent2,
    message_queue=message_queue,
    description="Useful for getting random dumb facts.",
    service_name="dumb_fact_agent",
    port=8003,
)