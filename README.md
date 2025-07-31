# Task 05: Descriptive Stats & LLM Reasoning

## 📌 Objective
Use a small sports dataset and prompt a large language model (LLM) to answer natural language questions about player performance, game outcomes, and strategic decisions.

## ⚙️ How to Run
1. Install requirements:

    pip install pandas matplotlib seaborn

2. Run descriptive stats:
    
    python scripts/basic_stats.py

3. Generate visualizations:
    
    python scripts/visualize.py



## 🧠 Example Questions Asked
- How many games did the team play?
- Who scored the most goals?
- Who was the most improved player?
- What if the team wanted to win 2 more games—should they focus on offense or defense?

## 📊 Visuals
Included: bar charts of top scorers, scoring trendlines, defensive stats comparison.

## 🤖 LLM Performance
- Basic Q&A: Excellent accuracy
- Advanced reasoning (e.g. "most improved"): Required tailored prompt and metric definitions
- Some hallucinations when context wasn't clear

## 🔁 Lessons Learned
- Prompt clarity and structure heavily affect answer accuracy
- LLMs can reason about trends but lack statistical precision without clear guidance
- They struggle to invent metrics unless explicitly defined