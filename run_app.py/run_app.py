import subprocess
import sys
import os

# ------------------------------
# Paths
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# ------------------------------
# Run Backend
# ------------------------------
print("Starting Flask backend...")
backend_process = subprocess.Popen([sys.executable, "app.py"], cwd=BACKEND_DIR)

# ------------------------------
# Run Frontend
# ------------------------------
print("Starting frontend server on http://127.0.0.1:5500 ...")
frontend_process = subprocess.Popen([sys.executable, "-m", "http.server", "5500"], cwd=FRONTEND_DIR)

# ------------------------------
# Wait for both processes
# ------------------------------
try:
    backend_process.wait()
    frontend_process.wait()
except KeyboardInterrupt:
    print("\nStopping servers...")
    backend_process.terminate()
    frontend_process.terminate()
