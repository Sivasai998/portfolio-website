from flask import Flask, render_template, url_for, redirect

# Configure application
app = Flask(__name__)


@app.route("/")
def home():
    greeting = ' Welcome to my Data Science portfolio'
    return render_template('index.html', greeting=greeting)


@app.route("/about", methods=['GET', 'POST'])
def About():
    return render_template('About_me.html')


@app.route("/portfolio", methods=['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html')


@app.route("/certifications", methods=['GET', 'POST'])
def certifications():
    return render_template('certifications.html')


@app.route("/Netflix-and-movies-in-different-countries-of-the-world", methods=['GET', 'POST'])
def Netflix_and_movies_in_different_countries_of_the_world():
    return render_template('Netflix-and-movies-in-different-countries-of-the-world.html')


@app.route("/Sentiment-Analysis-of-Election-prediction-using-NLP", methods=['GET', 'POST'])
def Sentiment_Analysis_of_Election_prediction_using_NLP():
    return render_template('Sentiment-Analysis- of -Election-prediction-using-NLP.html')


@app.route("/English-premiere-league-Big-Data-Platforms", methods=['GET', 'POST'])
def English_premiere_league_Big_Data_Platforms():
    return render_template('English-premiere-league-Big-Data-Platforms.html')


@app.route("/News_articles_topic_modelling", methods=['GET', 'POST'])
def News_articles_topic_modelling():
    return render_template('News_articles_topic_modelling.html')


if __name__ == "__main__":
    app.run(debug=True)
