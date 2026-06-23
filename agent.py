import pandas as pd
from langchain_groq import ChatGroq
from langchain.agents import create_agent as _create_agent
from langchain.tools import tool
from dotenv import load_dotenv
import os
import io
import contextlib

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override=True)

_df: pd.DataFrame = None

@tool
def python_repl(code: str) -> str:
    """Run Python code to analyze the dataframe `df`. Use print() to show results."""
    local_vars = {"df": _df, "pd": pd}
    stdout = io.StringIO()
    try:
        with contextlib.redirect_stdout(stdout):
            exec(code, {}, local_vars)
        output = stdout.getvalue()
        if not output and "result" in local_vars:
            output = str(local_vars["result"])
        return output or "Done (no output)"
    except Exception as e:
        return f"Error: {e}"


def create_agent(df: pd.DataFrame):
    global _df
    _df = df

    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"), override=True)

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    system_prompt = """You are a data analyst assistant.
Answer questions about the dataframe clearly and concisely.
Always explain your findings in plain language after showing any numbers.
If the user writes in Thai, respond in Thai.
Use the python_repl tool to run code against the dataframe `df`."""

    return _create_agent(model=llm, tools=[python_repl], system_prompt=system_prompt)


def ask_agent(agent, question: str) -> str:
    try:
        response = agent.invoke({"messages": [{"role": "user", "content": question}]})
        messages = response.get("messages", [])
        return messages[-1].content if messages else "ไม่มีคำตอบ"
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}"
