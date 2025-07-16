import streamlit as st
from agents import multi_agent_pipeline, save_outputs  # Replace with your real module
import json


# Page config
st.set_page_config(page_title="EduVideo Generator", layout="centered")

st.title("🎓 Educational Video Script Generator")
st.markdown("Generate video scripts and metadata for a YouTube channel based on grade & subject.")


# --- Input Form ---
with st.form("video_input_form"):
    subject = st.text_input("Enter Subject (e.g., Chemistry)", "Chemistry")
    grade = st.number_input("Enter Grade (e.g., 10)", min_value=1, max_value=12, value=10)
    submitted = st.form_submit_button("Generate Video Content")

# --- Output Area ---
if submitted:
    with st.spinner("Generating content, please wait... ⏳"):
        try:
            topic, script, metadata, video = multi_agent_pipeline(subject, grade)

            # Display outputs
            st.subheader("🧠 Topic")
            st.success(topic.content)

            st.subheader("📜 Script")
            st.text_area("Generated Script", script.content, height=300)

            st.subheader("📦 Metadata")
            try:
                metadata_json = json.loads(metadata.content)
                st.json(metadata_json)
            except json.JSONDecodeError:
                st.text_area("Raw Metadata", metadata.content)

            st.subheader("🎬 Video Info")
            st.code(video.content)

            # Save all
            save_outputs(subject, grade, topic, script, metadata, video)
            st.success("✅ All content saved to your outputs folder.")

        except Exception as e:
            st.error(f"❌ Something went wrong:\n{str(e)}")
