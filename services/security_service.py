import re


BLOCKED_PATTERNS = [

    # Prompt Injection
    "ignore previous instructions",
    "ignore all instructions",
    "ignore instructions",
    "system prompt",
    "developer message",
    "reveal your prompt",
    "show prompt",
    "reveal the prompt",

    # Secrets
    "show api key",
    "openai_api_key",
    "tmdb_api_key",
    "os.environ",
    ".env",

    # Dangerous Python
    "exec(",
    "eval(",
    "subprocess",
    "__import__",

    # Shell / OS
    "rm -rf",
    "cmd.exe",
    "powershell",
    "bash",
    "sudo",
    "chmod",
    "curl",
    "wget",

    # SQL Injection
    "or 1=1",
    "union select",
    "drop table",
    "insert into",
    "delete from",
    "--",

    # XSS / HTML Injection
    "<script",
    "</script",
    "javascript:",
    "onerror=",
    "onload=",
    "<iframe",
    "<img",
    "<svg",
]


def sanitize_input(text):

    if not text:
        return None

    text = text.strip()

    # límite tamaño
    if len(text) > 300:
        return None

    lower_text = text.lower()

    # bloquear patrones peligrosos
    for pattern in BLOCKED_PATTERNS:

        if pattern in lower_text:
            return None

    # caracteres peligrosos
    suspicious_regex = re.search(
        r"[<>\\{}[\];`$]",
        text
    )

    if suspicious_regex:
        return None

    return text