from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(x: float) -> float:
    """param num: a number to be tripled
       return: the tripled value of num
    """
    return 3 * x

tools = [triple,TavilySearch(max_results=3)]

llm =  ChatOllama(model="qwen3:4b",temperature=0).bind_tools(tools)
