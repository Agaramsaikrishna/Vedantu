import requests
from app import HEY_GEN_KEY
# url = "https://api.heygen.com/v2/voices"  #"https://api.heygen.com/v2/avatars"
# headers = {
#     "Accept": "application/json",
#     "X-Api-Key": HEY_GEN_KEY  # Replace with your actual API key
# }

# response = requests.get(url, headers=headers)

# # Print status code and JSON response
# print(f"Status Code: {response.status_code}")
# print(response.json())



# Abigail_expressive_2024112501

#'voice_id': '73c0b6a2e29d4d38aca41454bf58c955'





import requests
import json

def generate_heygen_video(
    
    input_text="Welcome to the HeyGen API!",
    avatar_id="Abigail_expressive_2024112501",
    voice_id="73c0b6a2e29d4d38aca41454bf58c955",
    avatar_style="normal",
    speed=1.1,
    width=1280,
    height=720
):
    """
    Generates a HeyGen video using the provided or default parameters.

    Parameters:
        
        input_text (str): The text to be spoken by the avatar.
        avatar_id (str): The avatar ID to use.
        voice_id (str): The voice ID to use.
        avatar_style (str): The style of the avatar (e.g., 'normal').
        speed (float): The speed of the speech.
        width (int): Width of the video.
        height (int): Height of the video.

    Returns:
        dict: Response JSON from the HeyGen API.
    """
    url = "https://api.heygen.com/v2/video/generate"
    headers = {
        "X-Api-Key": HEY_GEN_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": avatar_id,
                    "avatar_style": avatar_style
                },
                "voice": {
                    "type": "text",
                    "input_text": input_text,
                    "voice_id": voice_id,
                    "speed": speed
                }
            }
        ],
        "dimension": {
            "width": width,
            "height": height
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid JSON response", "raw": response.text}


# print(generate_heygen_video())

#{'error': None, 'data': {'video_id': '5355dd9c949645f594beb0b7510250b3'}}




def get_heygen_video_status(video_id):
    """
    Fetches the status of a HeyGen video using the video ID.

    Parameters:
        api_key (str): Your HeyGen API key.
        video_id (str): The video ID returned by the generate API.

    Returns:
        dict: JSON response with video status or error.
    """
    url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    headers = {
        "Accept": "application/json",
        "X-Api-Key": HEY_GEN_KEY
    }

    response = requests.get(url, headers=headers)

    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid JSON response", "raw": response.text}
    
    
    
# print(get_heygen_video_status('5355dd9c949645f594beb0b7510250b3'))


import requests
import time
import logging
from urllib.parse import urlparse
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_file(url, save_path):
    """Download file from URL and save locally."""
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        logging.info(f"File saved to: {save_path}")
    except Exception as e:
        logging.error(f"Failed to download file: {e}")

def get_filename_from_url(url):
    """Extract filename from URL path."""
    parsed = urlparse(url)
    return os.path.basename(parsed.path)

def poll_and_download_video(api_key, video_id, max_retries=20, wait_seconds=20):
    """
    Poll HeyGen API for video status until completed.
    Download the video file once ready.
    
    Params:
        api_key (str): Your HeyGen API key.
        video_id (str): Video ID to check.
        max_retries (int): Max number of polling attempts.
        wait_seconds (int): Seconds to wait between retries.
    """
    url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    headers = {
        "Accept": "application/json",
        "X-Api-Key": api_key
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()

            if result.get("code") != 100:
                logging.error(f"API Error: {result.get('message', 'Unknown error')}")
                return

            data = result.get("data", {})
            status = data.get("status", "unknown")

            logging.info(f"Attempt {attempt+1}/{max_retries} - Status: {status}")

            if status == "completed":
                video_url = data.get("video_url")
                if not video_url:
                    logging.error("No video URL found in response.")
                    return

                filename = get_filename_from_url(video_url)
                download_file(video_url, filename)
                return  # Done!

            elif status == "failed":
                logging.error("Video generation failed.")
                return

            # Not completed yet, wait and retry
            time.sleep(wait_seconds)

        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
            return
        except ValueError as e:
            logging.error(f"Failed to parse JSON response: {e}")
            return

    logging.warning("Max retries reached, video not ready yet.")

# # Example usage:
# api_key = HEY_GEN_KEY
# video_id = "5355dd9c949645f594beb0b7510250b3"
# poll_and_download_video(api_key, video_id)



