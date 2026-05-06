### 📰 News Fetcher
A simple Python CLI tool that fetches news articles by topic using the NewsAPI.

📁 Project Structure
news-fetcher/
├── main.py          # Entry point, ties modules together
├── getnews.py       # Fetches articles from NewsAPI
├── userinput.py     # Parses and cleans user input
├── .env             # Stores your API key (not committed to git)
└── requirements.txt

⚙️ Setup
1. Install dependencies
```bash
pip install requests python-dotenv
```
2. Create a .env file
envNEWS_API_KEY=your_api_key_here
Get a free key at newsapi.org.

🧩 Modules
userinput.py
Handles raw user input — splits a comma-separated string into a clean list of topics.
pythonsplit_input("AI, Climate Change, Sports")
# → ["ai", "climate change", "sports"]
getnews.py
Takes a list of topics and returns a dictionary mapping each topic to its list of articles from NewsAPI.
pythonget_news(["python", "nasa"])
# → {"python": [...], "nasa": [...]}

Fetches up to 20 articles per topic
Filters to English results only
Requires NEWS_API_KEY set in .env

main.py
Entry point. Prompts the user for input, parses it, fetches news, and returns results.

▶️ Usage
bashpython main.py
Then enter topics when prompted:
Enter topics (comma-separated): bitcoin, space, football

⚠️ Notes

If NEWS_API_KEY is missing, the program exits with an error message
Each function should be defined once, in its own module — duplicate definitions mean only the last one is used


📦 requirements.txt
streamlit 
requests
python-dotenv
```bash
pip install -r requirements.txt
```
