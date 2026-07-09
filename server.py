from fastapi import FastAPI, Request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


@app.get("/")
def home():
    return {
        "status": "TradingView Gemini MCP Server Running"
    }


@app.post("/tradingview")
async def tradingview(request: Request):

    data = await request.json()

    prompt = f"""
    You are an expert financial market analyst.

    Analyze this TradingView alert:

    {data}

    Provide:
    1. Market trend
    2. Technical analysis
    3. Risk assessment
    4. Possible trading plan
    """

    result = model.generate_content(prompt)

    return {
        "analysis": result.text
    }
