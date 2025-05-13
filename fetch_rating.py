import requests
from typing import Literal
import re


def get_chess_com_ratings(
    username: str,
    mode: Literal["chess_rapid", "chess_bullet", "chess_blitz"],
    rating_type: Literal["last", "best"]
):
    
    url = f"https://api.chess.com/pub/player/{username}/stats"
    headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyChessBot/1.0; +https://github.com/peroute)"
    }

    response = requests.get(url, headers=headers)
    
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        return f"Http error: {err} "
    except requests.exceptions.RequestException as err:
        return f"Request error: {err} "
    data = response.json()
    return data[mode][rating_type]["rating"] 

def update_readme_rating(rating, text_before, text_after, readme_path):
    #check if the readme_path exists
    if not readme_path.exists():
        print(f"Error: {readme_path} does not exist.")
        return
    
    # Read the current content of the README file
    content = readme_path.read_text()
    
    
    pattern = re.escape(text_before) + " .+ " + re.escape(text_after)
    
    replacement = text_before + " " + str(rating) + " " + text_after

    updated_content = re.sub(pattern , 
                             replacement, 
                             content)
    
    if updated_content == content:
        print("No changes made to the README file.")
        
    else:
        readme_path.write_text(updated_content)
        print("README file updated successfully.")
    

update_readme_rating("hello", "hello", "world", "hello blah blah world")


'''
username = "carrypawn"  

rating = get_chess_com_ratings(username,"chess_rapid","last")

print(type(rating))'''