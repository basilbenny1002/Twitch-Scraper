
# **Twitch Scraper**  

A Twitch scraper that fetches streamer information based on follower count and game category, extracting social media links and email contacts.  

## **Features**  
✅ Scrapes social media links (Discord, YouTube, etc.).  
✅ Extracts email addresses.  
✅ Filters streamers by **minimum followers** and **game category**.  
✅ Outputs results in a CSV file.  

## **Installation**  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/basilbenny1002/Twitch-Scraper.git  
   cd twitch-scraper  
   ```  
2. **Install Python dependencies:**  
   ```bash
   pip install -r requirements.txt  
   ```
   Additionally install playwright with:
   ```bash
   playwright install
   ```
3. **Install Node.js and Puppeteer:**  
   - You must install the required Node.js packages before running the scraper.  
   - Run the following command in the root directory:  
     ```bash
     npm install 
     ```  

## **Setup**  
1. **Get Your Twitch Client ID and Secret:**  
   - Go to the **[Twitch Developer Console](https://dev.twitch.tv/console/apps)**.  
   - Register a new application.  
   - Set OAuth redirect URL to anything (not needed for this script).  
   - Copy the **Client ID** and **Client Secret**.  

2. **Get an Access Token:**  
   Run this command in the terminal, replacing `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET`:  
   ```bash
   curl -X POST "https://id.twitch.tv/oauth2/token" \
   -d "client_id=YOUR_CLIENT_ID" \
   -d "client_secret=YOUR_CLIENT_SECRET" \
   -d "grant_type=client_credentials"
   ```  
   It will return a JSON response like this:  
   ```json
   {
     "access_token": "YOUR_ACCESS_TOKEN",
     "expires_in": 4915184,
     "token_type": "bearer"
   }
   ```  
   Copy the **access_token** and paste it into `main.py`.  

3. **Edit `main.py` and set:**  
   - **Access Token** (`ACCESS_TOKEN`)  
   - **Client ID** (`CLIENT_ID`)  
   - **Minimum Followers** (`MIN_FOLLOWERS`)  
   - **Game ID** (`GAME_ID`) – [Find Game IDs Here]([https://your-github-pages-link.com](https://dev.twitch.tv/docs/api/reference/#get-games))  

## **Usage**  
Run the script:  
```bash
python main.py  
```  

## **Project Structure**  
```
📂 twitch-scraper  
 ┣ 📜 main.py             # Main script to fetch streamers  
 ┣ 📜 functions.py        # Helper functions for API requests  
 ┣ 📜 scraper.js          # Puppeteer script for scraping social links & emails  
 ┣ 📜 package.json        # Node.js dependencies  
 ┣ 📜 requirements.txt    # Python dependencies  
 ┗ 📜 README.md           # Project documentation  
```  

## **Output Format**  
The script generates an **output.csv** file with the following columns:  
| Twitch Username | Followers | Viewer Count | Language | Game | Discord | YouTube | Contact |  
|----------------|----------|--------------|----------|------|---------|---------|---------|  

## **Contact**  
For any questions or further information, feel free to reach out at **basilbenny1002@gmail.com**.  

---
