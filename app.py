from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "<br/>".join(["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                         "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"])

@app.route('/image_mars')
def image_mars():
    return """
    <html>
    <head>
    <title>Привет, марс!</title>
    </head>
    <h1>Жди нас, Марс!</h1>
    <image src="https://asteropa.ru/wp-content/uploads/2019/09/-e1569874296830.jpg" style="width: 500px; height: 500px;">
    <p>Вот она какая, красная планета</p>
    </html>
    
    """
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
