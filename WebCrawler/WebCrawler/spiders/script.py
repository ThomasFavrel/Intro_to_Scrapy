url = 'https://myanimelist.net/manga.php?letter=B'
fetch(url)

for sub_block in response.css('div.js-categories-seasonal tr ~ tr'):
    