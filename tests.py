import subprocess

def run_tests():
    """
    Run the unit tests in the 'tests' directory.
    """
    try:
        result = subprocess.run(
            ['python', '-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v'],
            check=True,
            capture_output=True,
            text=True
        )
        print("Tests ran successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running tests:")
        print(e.stderr)

if __name__ == "__main__":
    run_tests()