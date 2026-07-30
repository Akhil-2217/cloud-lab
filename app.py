from flask import Flask

app = Flask(__name__)

@app.rout("/")
def home():
  return "Hello from PaaS"

if __name__ == "__main__":
  app.run()
