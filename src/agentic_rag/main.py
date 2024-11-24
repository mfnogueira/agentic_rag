#!/usr/bin/env python
import sys
from agentic_rag.crew import AgenticRagCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {"query": "What was the year with the highest total expenses?"}
    result = AgenticRagCrew().crew().kickoff(inputs=inputs)

    if isinstance(result, str) and result.startswith("```python"):
        code = result[9:].strip()
        if code.endswith("```"):
            code = code[:-3].strip()

        with open("outputs/visualize.ipynb", "w") as f:
            f.write(code)
