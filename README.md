**📰# News Scraper with NewsAPI**

A Python script that fetches news articles from multiple sources and saves article links to a text file. ✨

## What It Does
Fetches news articles on a given topic or keyword 🗞️
Pulls articles from multiple sources (BBC, AP News, Reuters) 🌐

Retrieves both all articles matching the topic and top headlines 🏆
Saves article URLs to newslink.txt 💾

## How It Works
Uses the NewsAPI /v2/everything endpoint to fetch articles based on a keyword/topic 🔍
Uses the NewsAPI /v2/top-headlines endpoint to fetch top news headlines for a country 🌎
Processes the API response to extract article titles and URLs 📝
Writes the URLs to a file for easy reference 📂
