import subprocess
import sys

def run_python_module(module, args):
    """
    Runs a Python module command using the active executable.
    Example: run_python_module('pip', ['install', 'requests'])
             run_python_module('pytest', ['tests/'])
    """
    if "exit" in args or module.lower() == "exit":
        return

    command = [sys.executable, '-m', module] + args
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("=== STDOUT ===")
        print(e.stdout)
        print("=== STDERR ===")
        print(e.stderr)

def main():
    # CLI Argument Mode (e.g., python PythonCommand.py pip install requests)
    if len(sys.argv) >= 3:
        module = sys.argv[1]
        args = sys.argv[2:]
        run_python_module(module, args)
        return

    # Interactive Repl Mode
    print("=== Python Module Command Runner ===")
    print("Enter a module command (e.g. 'pip install requests' or 'pytest'). Type 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input(">>> ").strip()
            if not user_input or user_input.lower() == "exit":
                print("Exiting runner.")
                break

            parts = user_input.split()
            module = parts[0]
            args = parts[1:]

            run_python_module(module, args)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting runner.")
            break

if __name__ == "__main__":
    main()
