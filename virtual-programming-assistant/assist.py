import code
import jedi

def run_code(user_code, namespace):
    try:
        code_result = code.compile_command(user_code, "<stdin>", "single")
        if code_result:
            exec(code_result, namespace)
        else:
            return None
    except Exception as e:
        return str(e)
    return None

def suggest_code(user_code, namespace):
    script = jedi.Script(user_code, [namespace])
    suggestions = []
    for suggestion in script.suggestions():
        suggestions.append(suggestion.complete)
    return suggestions

def main():
    print("Bem-vindo ao Assistente de Programação Completo!")
    namespace = {}
    
    while True:
        user_input = input("Digite o código Python ou 'sair' para encerrar: ")
        
        if user_input.lower() == "sair":
            print("Até logo!")
            break
        
        suggestions = suggest_code(user_input, namespace)
        
        if suggestions:
            print("Sugestões de código:")
            for suggestion in suggestions:
                print(suggestion)
        else:
            error = run_code(user_input, namespace)
            if error:
                print("Erro:", error)

if __name__ == "__main__":
    main()
