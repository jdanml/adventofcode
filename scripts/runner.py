import typer
from typing_extensions import Annotated
import subprocess

app = typer.Typer()

def run_script(script_path):
    subprocess.run(["python", script_path])

@app.callback()
def callback() -> None:
    """Helper script tool for running a solution for a challenge"""

@app.command()
def day(year: Annotated[str, typer.Argument()], day: Annotated[str, typer.Argument()]) -> None:
    code_dir = f"./{year}/{day}/code.py"
    run_script(code_dir)

if __name__ == "__main__":
    app()