from compiler.lexer import tokenize
from compiler.parser import parse
from compiler.semantic import check_ast

def run_command(cmd):
    try:
        tokens = tokenize(cmd)
        ast = parse(tokens)
        result = check_ast(ast)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    examples = [
        "bana table students",
        "daal mein students value naam = 'Shobhit' aur rollno = 22",
        "daal mein students value naam = 'Ankit' aur rollno = 19",
        "nikal se students",
        "nikal se students naam jaha rollno > 20",
        "nikal se students naam, rollno jaha naam = 'Ankit'",
        "bana table employees (id int primary key, naam varchar, salary int)",
        "daal mein employees value naam = 'John' aur salary = 50000 aur id = 1",
        "nikal se employees salary jaha naam = 'John'",
        "bana table students (id int primary key, name varchar)",
        "daal mein students value id = 1 aur name = 'Shobhit'",
        "nikal se students jaha id = 1 aur name = 'Shobhit'",
        "mita students jaha id = 1"
    ]

    for i, cmd in enumerate(examples):
        print(f"\nTest {i+1}: '{cmd}'")
        result = run_command(cmd)
        if isinstance(result, list):
            if result:
                for row in result:
                    print(row)
            else:
                print("No matching records.")
        else:
            print(result)

