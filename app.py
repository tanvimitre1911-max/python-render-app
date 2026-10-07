from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    number_a = 15
    number_b = 5
    total_sum = number_a + number_b

    return f"The sum is:
    {total_sum}"

if __name__ == '__main__':
    app.run()
