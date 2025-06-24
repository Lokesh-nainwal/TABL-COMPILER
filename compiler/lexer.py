# compiler/lexer.py

import re

TOKENS = [
    # Core SQL commands
    ("CREATE", r"\bbana\b"),            # CREATE
    ("INSERT", r"\bdaal\b"),            # INSERT
    ("DELETE", r"\bmita\b"),            # DELETE
    ("UPDATE", r"\bbadal\b"),           # UPDATE
    ("SET", r"\bset\b"),                # SET 
    ("SELECT", r"\bnikal\b"),           # SELECT
    ("FROM", r"\bse\b"),                # FROM
    ("INTO", r"\bmein\b"),              # INTO
    ("VALUES", r"\bvalue\b"),           # VALUES
    ("TABLE", r"\btable\b"),            # TABLE
    ("WHERE", r"\bjaha\b"),             # WHERE
    ("AND", r"\baur\b"),                # AND

    # Join & Group
    ("JOIN", r"\bjodo\b"),              # JOIN
    ("ON", r"\bon\b"),                  # ON
    ("GROUPBY", r"\bjodkar\b"),         # GROUP BY

    # Loop-related
    ("BAAR", r"\bbaar\b"),              # Loop keyword
    ("NUMBER", r"\b\d+\b"),             # Integer numbers

    # Operators & symbols
    ("OPERATOR", r"=|>=|<=|!=|>|<"),    # All operators
    ("COMMA", r","),                    # ,
    ("LPAREN", r"\("),                  # (
    ("RPAREN", r"\)"),                  # )

    # Data Types
    ("TYPE", r"\bint\b|\bvarchar\b"),   # int, varchar
    ("PRIMARY", r"\bprimary\b"),        # primary
    ("KEY", r"\bkey\b"),                # key

    # Literals
    ("STRING", r"'[^']*'"),             # Strings in single quotes

    # Identifiers (tables, columns) must come last to avoid keyword matching
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),

    # Whitespace & error handling
    ("SKIP", r"[ \t\n]+"),              # Ignore whitespace
    ("MISMATCH", r".")                  # Catch-all for invalid input
]

# Tokenizer function
def tokenize(code):
    tokens = []
    index = 0

    while index < len(code):
        matched = False
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, index)
            if match:
                value = match.group(0)
                if token_type == "SKIP":
                    pass  # Ignore whitespace
                elif token_type == "MISMATCH":
                    raise SyntaxError(f"Unexpected token: {value}")
                else:
                    tokens.append((token_type, value))
                index = match.end()
                matched = True
                break
        if not matched:
            raise SyntaxError(f"Illegal character at index {index}: {code[index]}")
    return tokens
