# Vedantu


# 🎓 YouTube Automation for Educational Videos

This project automates the generation of educational video scripts, metadata, and avatar-style videos using AI tools such as Together AI, HeyGen, and a user-friendly Streamlit UI.

Perfect for teachers, YouTube creators, and EdTech startups who want to streamline the creation of curriculum-based educational videos.

---

## ✨ Features

- 📚 Generates video **topics**, **scripts**, and **YouTube metadata** (titles, tags, descriptions)
- 🧠 Uses **LLMs** (like Together AI) for natural, curriculum-aligned text generation
- 🎥 Integrates with **HeyGen API** to generate avatar videos from scripts
- 💾 Automatically saves each output to a clean folder structure
- 🖼️ Simple **Streamlit UI** for interaction — no coding needed
- 🗂 Organized by `grade_subject_topic` for easy content management

---

* Set up a virtual environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate


*Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
-

*Create .env file with your API keys
ini
Copy
Edit
TOGETHER_API_KEY=your_together_api_key
HEY_GEN_KEY_1=your_heygen_api_key


*Run the Streamlit UI
bash
Copy
Edit
streamlit run app.py



📂 Example Output Structure
bash
Copy
Edit
outputs/
└── 10_chemistry_chemical_bonding/
    ├── script.txt         # Generated lesson script
    ├── metadata.json      # Title, tags, description
    └── video_info.txt     #


🧠 Tech Stack
Tool / Lib	Role
Streamlit	Web interface
Together AI	Natural language generation
HeyGen API	Avatar-based video generation
Python	Backend scripting & automation
dotenv, requests	Environment & HTTP calls




🔮 Future Improvements
Here are upcoming enhancements and ideas for future development:

🌟 Core Functionality
 Direct YouTube Upload via YouTube Data API

 Add support for more subjects and languages

 Allow custom script editing before video generation

 Implement voice/style selection options in UI

 Multi-step retry logic for failed video generations




 💡 User Experience
 Add download buttons for script, metadata, and video

 Embed video preview directly in the Streamlit UI

 Show API usage quota warnings (e.g., HeyGen limits)

 Save session history and allow reusing previous results

 Responsive design for mobile/tablet support

📊 Admin & Analytics
 Track and log generation stats (topic popularity, success/fail rate)

 Export content as PDF lesson plans

 Integration with Google Classroom or LMS

