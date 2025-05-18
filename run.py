import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ui.app import app

if __name__ == '__main__':
    print("Starting Patient Buddy...")
    
    os.makedirs(os.path.join('data', 'uploads'), exist_ok=True)
    os.makedirs(os.path.join('data', 'cache'), exist_ok=True)
    
    try:
        import subprocess
        subprocess.run(["ollama", "list"], check=True, capture_output=True)
        print("Ollama is installed and running.")
    except:
        print("\nWARNING: Ollama might not be installed or running.")
        print("Please install Ollama from https://ollama.ai/download")
        print("After installation, run: ollama pull phi3\n")
    
    print("Starting web server...")
    app.run(debug=True)