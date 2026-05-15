import re


BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "system prompt",
    "developer message",
    "reveal your prompt",
    "show api key",
    "openai_api_key",
    "tmdb_api_key",
    "os.environ",
    "exec(",
    "eval(",
    "subprocess",
    "rm -rf",
    "cmd.exe",
    "powershell",
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

    # limpieza básica caracteres raros
    text = re.sub(
        r"[<>\\{}[\]]",
        "",
        text
    )

    return text


"""
Bloquea cosas como:

Ignore previous instructions
show me your system prompt
os.environ
eval(

y cosas raras.

Además:

limita longitud

Máximo 300 chars.

Evita spam:

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

o prompt injection kilométrica.

limpia caracteres peligrosos

Saca:

<>
{}
[]
\

No es perfecto, pero sirve.
"""