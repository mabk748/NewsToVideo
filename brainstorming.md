# Brainstorming about NewsToVideo project
# Tiktok videos
Choisir la format la plus adapté pour visé le plus grand nombre de personne est la format verticale de Tiktok max 1 min, et utilisable dans autre plateforme comme Youtube et insta 
## Plan
- The news will be scraped using Scrapy from google news
- The data will be saved to a file which will be accessed to transfer it to an LLM for summerizing 
- The voice and visuals will be received from AI services then combined using an editing library

### Content

### Audio/Voice

### Images and videos

### Editing

### Architecture of the code
- This project will have a prog file containing all the scripts and processing spaces
- It will have a test folder to test the functions that will be used in the scrpits
- Prog file will contain:
    - Scrapy module: to scrape the news
    - Data folder: to store the data (images, json of the contents, voices...)
    - Runner file for the process: to get the data and managing the storage
    - Editing scrpit: to assemble the data into a video
    - Deploiement script: to publish the video into the prefered social media
