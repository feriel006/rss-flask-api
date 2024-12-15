import feedparser
from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Function to parse RSS feeds
def get_rss_feed(url):
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary,
            'published': entry.published if 'published' in entry else "Unknown"
        })
    return articles

# Sample endpoint to fetch articles from an RSS feed
@app.route('/rss', methods=['GET'])
def fetch_rss():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'No RSS feed URL provided'}), 400
    try:
        articles = get_rss_feed(url)
        return jsonify({'articles': articles})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to fetch articles specifically from TrendHunter RSS feed
@app.route('/trendhunter', methods=['GET'])
def fetch_trendhunter():
    url = "https://www.trendhunter.com/rss"
    try:
        articles = get_rss_feed(url)
        return jsonify({'articles': articles})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to fetch articles specifically from Yatzer RSS feed
@app.route('/yatzer', methods=['GET'])
def fetch_yatzer():
    url = "https://www.yatzer.com/rss.xml"
    try:
        articles = get_rss_feed(url)
        return jsonify({'articles': articles})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
