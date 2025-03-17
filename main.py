#necessary imports
from functions import get_follower_count, scrape_twitch_about, scrape_twitter_profile, extract_emails, scrape_youtube, get_live_streams
import pandas as pd
from tqdm import tqdm
import logging

access_token = "" #TODO: paste your access token here
client_id = "" #TODO: paste your client_id here
minimum_follower = 50000
game_id = "516575" #TODO: paste the game id you want to filter from
output_file_name = "Example.csv" #TODO: file name of the output, make sure to include .csv

streams = get_live_streams(game_id, client_id=client_id, access_token=access_token) #making the api request to get the list of live streamers

#Initialising empty lists to store values
username = []
followers = []
viewer_count = []
language = []
game_name = []
discord = []
youtube = []
gmail = []
streamers = []

for i in tqdm(range(len(streams)), desc="Collecting streamer list"):
    """
    Iterating over the API response and appending details of streamers with more than the specified number of followers to a list
    """
    follower = get_follower_count(client_id, access_token, user_id=streams[i]['user_id'])  #function to get follower count
    if follower > minimum_follower:
        streamer_info = {"user_name": streams[i]['user_name'], "viewer_count": streams[i]['viewer_count'], #Data format of the appended values
                         "language": streams[i]['language'], 'game_name': streams[i]['game_name'],
                         'followers': follower}
        streamers.append(streamer_info)


logging.info("Done collecting streamers with more than %d followers", minimum_follower)
logging.info("Colelcting other info")
for i in tqdm(range(len(streamers)), desc="Getting more info"):
    """
    Looping over the chosen streamers to get additional info
    """
    #Initializing empty lists to store different links and sets to prevent duplicate links
    yt_links = set()
    dc_links = []
    twitter_links = []
    mails_found = set()
    #appending values
    username.append(streamers[i]['user_name'])
    followers.append(streamers[i]['followers'])
    viewer_count.append(streamers[i]['viewer_count'])
    language.append(streamers[i]['language'])
    game_name.append(streamers[i]['game_name'])
    response = scrape_twitch_about(f"https://www.twitch.tv/{streamers[i]['user_name']}/about") #Scraping their twitch about section
    socials = response.get('links', [])
    mail = response.get('email', [])
    mails_found.update(mail)
    if len(socials) == 0: #checking the absence of any socials
        discord.append("Couldn't find discord")
        youtube.append("Couldn't find youtube")
        if len(mails_found) > 0:
            gmail.append(', '.join(str(element) for element in mails_found))
            continue
        else:
            gmail.append("Couldn't find a valid mail")
            continue
    #Collecting socials
    for social_links in socials:
        if "youtube" in str(social_links).lower():
            yt_links.add(social_links)
        if "discord" in str(social_links).lower():
            dc_links.append(social_links)
        if "x" in i or "twitter" in str(social_links).lower():
            twitter_links.append(social_links)

    if len(yt_links) == 0:
        youtube.append("Couldn't find youtube")
    else:
        youtube.append(", ".join(str(link) for link in yt_links))
    if len(dc_links) == 0:
        discord.append("Couldn't find discord")
    else:
        discord.append(dc_links[0])

    if len(twitter_links) > 0:
        bio = scrape_twitter_profile(twitter_links[0])['bio'] #Scraping twitter bio if present
        mail = extract_emails(bio)
        if mail:
            mails_found.update(mail)
    if len(yt_links) > 0:
        mails_found.update(scrape_youtube(yt_links)) #Scraping youtube if present
    if len(mails_found) == 0:
        gmail.append("Couldn't find a valid gmail")
    else:
        gmail.append(",".join([i for i in set(mails_found)]))

#Output structure
datas = {"Username": username, "Followers": followers, "Viewer_count": viewer_count, "Language": language,
         "Game": game_name, "Discord": discord, "Youtube": youtube, "Contact": gmail}

df = pd.DataFrame(datas)
df.to_csv(path_or_buf=output_file_name, index=False)
