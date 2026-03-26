from flask import Flask
import multiprocessing

app = Flask(__name__)

def cpu_intensive_task():
    while True:
        [x*2 for x in range(10*6)]  # Keeps CPU busy

@app.route("/")
def home():
    p = multiprocessing.Process(target=cpu_intensive_task)
    p.start()  # Start a CPU-intensive process
    return "CPU Load Simulated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
