
from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang=\"ar\" dir=\"rtl\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>مرحبًا بكم في قناتي</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
            direction: rtl;
            text-align: right;
        }
        header {
            background-color: #6200ea;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        main {
            padding: 20px;
        }
        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        a {
            color: #6200ea;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>مرحبًا بكم في قناتي</h1>
        <p>اكتشفوا مزيجًا من الكوميديا والمعرفة!</p>
    </header>
    <main>
        <section>
            <h2>عن القناة</h2>
            <p>
                في هذه القناة، نقدم لكم فيديوهات مضحكة بدون وجه تعتمد على الميمز
                والتعليق الصوتي. نستكشف مواضيع متنوعة تشمل المعرفة، والعلم،
                والتاريخ، والقضايا الاجتماعية بطريقة ممتعة ومسلية.
            </p>
        </section>
        <section>
            <h2>تابعوني</h2>
            <p>
                لا تفوتوا أي فيديو جديد! اشتركوا في القناة وتابعوني على
                <a href=\"#\">وسائل التواصل الاجتماعي</a>.
            </p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 قناتي - جميع الحقوق محفوظة</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    # Use a default port and allow environment variable override
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=port, host="0.0.0.0")
