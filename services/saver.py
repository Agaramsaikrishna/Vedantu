import os
import json
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def sanitize_filename(name):
    """Sanitize topic name to create a safe folder name."""
    name = re.sub(r'[^\w\s-]', '', name)  # Remove non-alphanumeric characters
    name = re.sub(r'[-\s]+', '_', name.strip().lower())  # Replace spaces/hyphens with underscores
    return name


def save_outputs(subject, grade, topic, script, metadata, video):
    """
    Save topic, script, metadata, and video info to structured output directory.

    Args:
        subject (str): Subject name (e.g., "chemistry").
        grade (int): Grade level (e.g., 10).
        topic, script, metadata, video: Objects with a `.content` attribute.
    """
    # Extract and sanitize topic
    topic_text = getattr(topic, 'content', 'unknown_topic')
    safe_topic = sanitize_filename(topic_text)

    # Create output folder
    folder_path = os.path.join("outputs", f"{grade}_{subject}_{safe_topic}")
    os.makedirs(folder_path, exist_ok=True)

    # Save script
    script_file = os.path.join(folder_path, "script.txt")
    with open(script_file, "w", encoding="utf-8") as f:
        f.write(script.content or "")
    logging.info(f"✅ Script saved to: {script_file}")

    # Save metadata
    try:
        meta_json = json.loads(metadata.content)
    except json.JSONDecodeError:
        meta_json = {"raw_metadata": metadata.content}
    metadata_file = os.path.join(folder_path, "metadata.json")
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(meta_json, f, indent=2)
    logging.info(f"✅ Metadata saved to: {metadata_file}")

    # Save video info
    video_file = os.path.join(folder_path, "video_info.txt")
    with open(video_file, "w", encoding="utf-8") as f:
        f.write(video.content or "")
    logging.info(f"✅ Video info saved to: {video_file}")

    logging.info(f"📁 All files saved in: {folder_path}")
