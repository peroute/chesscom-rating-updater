# chesscom-rating-updater
# ♟️ Chess.com Rating Updater Bot

This Python script fetches a user's chess.com rating (rapid, blitz, or bullet) using the [Chess.com Public API](https://www.chess.com/news/view/published-data-api) and updates the value inside a `README.md` file on your GitHub profile or project repository.

## 🔧 Features

- Fetches your current rating (best or last) from chess.com.
- Supports rapid, blitz, and bullet modes.
- Updates a section in your `README.md` file with the latest rating.
- Useful for GitHub profile READMEs to display live rating data.

---

## 📦 Requirements

- Python 3.7+
- `requests` library

Install dependencies:

```bash
pip install requests
```

---

## 🧠 How It Works

1. **Fetches rating data** from the Chess.com API using your username and the game mode.
2. **Updates your README.md** by finding a section between two marker texts (e.g. `<!-- RATING_START -->` and `<!-- RATING_END -->`) and replaces whatever is between them with your current rating.

---

## 🔍 Example Usage

### 1. Create markers in your README file

Magnus Carlsen's Rapid current rating: 111 in Chess.com