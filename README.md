# README: Solo Leveling Chapter Scraper

A Python script to scrape and save all chapters of the *Solo Leveling* novel from [novelsonline.org](https://www.novelsonline.org).

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 Description
This script automates the download of *Solo Leveling* chapters (1-270) using web scraping. It leverages multi-threading for faster processing and saves each chapter as a separate `.txt` file in a dedicated `chapters` directory. The script also cleans the content by removing ads, JavaScript messages, and sponsor notes.

---

## ✨ Features
- **Multi-threaded scraping** for faster chapter retrieval.
- **Automatic text cleaning** to remove unwanted content (ads, scripts, sponsor messages).
- **Chapter organization** into individual text files.
- **Progress tracking** with runtime statistics.

---

## ⚙️ Prerequisites
- Python 3.6+
- `requests` and `beautifulsoup4` libraries
- An internet connection

---

## 🛠️ Installation
1. Clone/download the script and navigate to its directory.
2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Create a `chapters` folder in the script directory (required to save files):
   ```bash
   mkdir chapters
   ```

---

## 🚀 Usage
Run the script:
```bash
python solo-requests.py
```
The script will:
1. Fetch all chapters concurrently.
2. Clean and save them to `chapters/ch{1-270}.txt`.
3. Display the total execution time.

**Sample Output:**
```
Chapter 1:
The cold air blew past him as Jin-Woo...
...
⏱️ Time taken: 42.19 seconds
✅ Done!
```

---

## 📂 Project Structure
```
solo-requests/
├── chapters/          # Generated folder with chapter files
│   ├── ch1.txt
│   ├── ch2.txt
│   └── ...
├── solo-requests.py   # Main script
└── README.md
```

---

## 📝 Notes
- The script is configured for chapters **1-270**. Modify the range in the `for` loops to adjust.
- If blocked by the website, uncomment `time.sleep(0.5)` to throttle requests.
- Content structure changes on the source website may require script updates.

---

## ⚠️ Disclaimer
This script is for **educational purposes only**. Respect website terms of service and robots.txt rules. The maintainers are not responsible for misuse or legal consequences.

---

## License

MIT License. See `LICENSE` for details.
