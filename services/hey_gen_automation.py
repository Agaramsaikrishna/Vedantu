import requests
import json
import time
import logging
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get HeyGen API Key
HEY_GEN_KEY = os.getenv("HEY_GEN_KEY_1")

def download_file(url, save_path):
    """Download file from URL and save locally."""
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        logging.info(f"✅ File saved to: {save_path}")
    except Exception as e:
        logging.error(f"❌ Failed to download file: {e}")

def get_filename_from_url(url):
    """Extract safe filename from a URL."""
    parsed = urlparse(url)
    return os.path.basename(parsed.path.split("?")[0])

def generate_and_save_video(input_text):
    """
    Generates a video using HeyGen API, polls until it's ready, and saves it locally.
    
    Args:
        input_text (str): The script/text to be spoken in the video.
    
    Returns:
        str: Local path to saved video or error message.
    """
    avatar_id = "Abigail_expressive_2024112501"
    voice_id = "73c0b6a2e29d4d38aca41454bf58c955"
    avatar_style = "normal"
    speed = 1.1
    width = 1280
    height = 720
    max_retries = 30
    wait_seconds = 30
    videos_folder = "videos"

    # Step 1: Send video generation request
    logging.info("🎬 Starting video generation...")
    url_generate = "https://api.heygen.com/v2/video/generate"
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

    try:
        response = requests.post(url_generate, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        result = response.json()
        logging.info(f"Response from HeyGen: {result}")
    except Exception as e:
        logging.error(f"❌ Failed to generate video: {e}")
        return f"Failed to generate video: {e}"

    video_id = result.get("data", {}).get("video_id")
    if not video_id:
        logging.error("❌ No video ID returned.")
        return "Video ID not found in response."

    logging.info(f"📽️ Video generation started with ID: {video_id}")

    # Step 2: Poll status
    url_status = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    for attempt in range(max_retries):
        time.sleep(wait_seconds)
        try:
            status_resp = requests.get(url_status, headers=headers)
            status_resp.raise_for_status()
            status_data = status_resp.json()
            logging.info(f"🕒 Polling attempt {attempt + 1}: {status_data}")
        except Exception as e:
            logging.error(f"❌ Failed to get video status: {e}")
            return f"Failed to get video status: {e}"

        if status_data.get("code") != 100:
            msg = status_data.get("message", "Unknown error.")
            logging.error(f"❌ API returned error code: {msg}")
            return f"API error: {msg}"

        data = status_data.get("data", {})
        status = data.get("status")

        if status == "completed":
            video_url = data.get("video_url")
            if not video_url:
                logging.error("❌ No video URL found when status is completed.")
                return "No video URL found."

            # Step 3: Create folder if not exists
            if not os.path.exists(videos_folder):
                os.makedirs(videos_folder)

            filename = get_filename_from_url(video_url)
            save_path = os.path.join(videos_folder, filename)

            # Step 4: Download the video
            logging.info(f"⬇️ Downloading from: {video_url}")
            download_file(video_url, save_path)
            return f"✅ Video saved successfully at {save_path}"

        elif status == "failed":
            logging.error("❌ Video generation failed.")
            return "Video generation failed."

    logging.warning("⚠️ Max retries reached. Video not ready.")
    return "Max retries reached. Video is not ready yet."

# # ✅ Example usage
# if __name__ == "__main__":
#     script_text = "Welcome to the fascinating world of chemistry, where the building blocks of our universe come alive."
#     result = generate_and_save_video(script_text)
#     print(result)
