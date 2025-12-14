import subprocess


def generate_answer(prompt: str) -> str:
    """
    Calls Ollama local LLM using UTF-8 encoding (Windows safe)
    """
    process = subprocess.Popen(
        ["ollama", "run", "mistral"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",     # ✅ FORCE UTF-8
        errors="ignore"       # ✅ Ignore invalid chars safely
    )

    stdout, stderr = process.communicate(prompt)

    if process.returncode != 0:
        raise RuntimeError(f"Ollama error: {stderr}")

    return stdout.strip()
