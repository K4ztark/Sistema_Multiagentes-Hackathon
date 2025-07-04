#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crewhackathon.crew import Crewhackathon

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .config import Variable
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information
def run():
    inputs = {
        'topic': input("aumentar/disminuir precio n % (n entero) (el precio se relaciona con el presupuesto), aumentar/disminuir produccion n % (n entero): "),
        'current_year': str(datetime.now().year)
    }
    Variable.topic=inputs['topic']
    try:
        Crewhackathon().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": input("Aumentar/disminuir precios, aumentar/disminuir producción, aumentar/dismunuir cantidad de empleados y presupuesto:"),
        'current_year': str(datetime.now().year)
    }
    try:
        Crewhackathon().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Crewhackathon().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": input("Aumentar/disminuir precios, aumentar/disminuir producción, aumentar/dismunuir cantidad de empleados y presupuesto:"),
        "current_year": str(datetime.now().year)
    }

    try:
        Crewhackathon().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

