from flask import Flask, render_template, request
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    img = io.BytesIO()
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route("/", methods=["GET", "POST"])
def index():
    img_data = None
    if request.method == "POST":
        text = request.form["text"]
        if text.strip():  # Pastikan tidak kosong
            img_data = generate_wordcloud(text)
    return render_template("index.html", img_data=img_data)

if __name__ == "__main__":
    app.run(debug=True)
