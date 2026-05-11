from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

def process_command(command):
    command = command.lower()

    if "hello" in command:
        return {"type": "text", "data": "Hello! How can I help you?"}

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return {"type": "text", "data": f"Current time is {now}"}

    elif "date" in command:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return {"type": "text", "data": f"Today's date is {today}"}

    elif "open youtube" in command:
        return {"type": "action", "data": "https://www.youtube.com"}

    elif "open google" in command:
        return {"type": "action", "data": "https://www.google.com"}

    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        return {"type": "action", "data": url}

    else:
        return {"type": "text", "data": "Sorry, I didn't understand that."}


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    command = data.get("command")

    result = process_command(command)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)