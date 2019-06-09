# manga-scraper

Inspired from [Khed](https://github.com/bnu123/Khed) I've made this CLI application that searches and downloads manga from [Kissmanga](https://kissmanga.com).

clone this repository
```bash
cd manga-scraper
sudo apt-get install xvfb
pip install -r requirements.txt
source commands.sh
search "One Piece" #to search for manga and the select the choice from the list
  or
download https://kissmanga.com/Manga/One-Piece/945---O-Lin #to directly download the manga from the given link
```
The Manga is then downloaded in /home/username/Downloads

Don't forget to change the username and path to webdriver in scrape.py
