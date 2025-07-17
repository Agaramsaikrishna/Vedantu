#VEDANTU



# 🎓 YouTube Automation for Educational Videos

**Vedantu Automation Toolkit** is a smart, end-to-end system for generating educational video content using AI — from script to avatar-style video — with zero manual editing required.

Whether you're an educator, content creator, or EdTech founder, this tool simplifies curriculum-based video creation using AI services like **Together AI**, **HeyGen**, and **Streamlit**.

---

## 🚀 Key Features

- ✅ **Curriculum-Aligned Topic Generation**
- 🧠 **AI-Generated Scripts** using LLMs (e.g., Together AI)
- 🎯 **Optimized YouTube Metadata** (title, tags, and description)
- 🎥 **Avatar-Based Video Creation** using HeyGen API
- 🖥️ **Streamlit UI** for easy, no-code use
- 💾 **Automatic Saving** of generated assets
- 📁 **Organized Output** based on subject and grade

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/Agaramsaikrishna/vedantu.git
cd vedantu-ai-automation
```

2. **Create Virtual Environment**

```bash
python -m venv .venv
# Activate it:
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Add API Keys**

Create a `.env` file in the root directory:

```ini
TOGETHER_API_KEY=your_together_api_key
HEY_GEN_KEY_1=your_heygen_api_key
```

5. **Run the Streamlit App**

```bash
streamlit run app.py
```

---

## 🧠 Tech Stack

| Tool / Library   | Role                                |
|------------------|-------------------------------------|
| **Streamlit**    | Web-based UI                        |
| **Together AI**  | Natural language generation (LLM)   |
| **HeyGen API**   | Avatar video generation             |
| **Python**       | Backend scripting & logic           |
| **dotenv**       | Environment config management       |
| **requests**     | HTTP/API calls                      |




---





System Capabilities
✅ Key Automation Modules:
Module	Description
📈 Trend Finder	Scrapes YouTube and Google Trends based on grade/subject
🧠 Topic Selector	Uses curriculum + SEO signals to prioritize topics
✍️ Script Generator	LLM (Together AI) to generate grade-appropriate scripts
📝 Metadata Generator	Optimizes title, tags, and description using AI
🎥 Video Generator	Uses HeyGen to create avatar-led educational videos
📁 Asset Organizer	Outputs structured folders for each video
💻 Streamlit UI	Enables non-tech users (teachers, editors) to run the tool



Architecture Diagram
```
+------------------+
| Trend Finder     | <----- YouTube Search + Google Trends
+--------+---------+
				 |
				 v
+--------+---------+
| Topic Selector   | <---- Curriculum + Engagement Data
+--------+---------+
				 |
				 v
+--------+---------+
| Script Generator | <---- Together AI LLM
+--------+---------+
				 |
				 v
+--------+----------+
| Metadata Builder  | <---- SEO keywords + LLM prompts
+--------+----------+
				 |
				 v
+--------+----------+
| Video Generator   | <---- HeyGen API (Avatar + Voiceover)
+--------+----------+
				 |
				 v
+--------+----------+
| Streamlit UI      | <---- Run end-to-end in 1 click
+-------------------+

```

Problem Solved & Why It Matters
 
  Creating high-quality educational YouTube videos at scale is labor-intensive and dependent on Master Teachers. Vedantu publishes 1,000+ videos monthly across 25+ channels and has over 650M+ cumulative views—but scaling this further requires automation.

 This tool automates the entire video production pipeline, from identifying trending educational topics to generating scripts, metadata, and avatar-led videos. It ensures:

-Higher throughput of video content

-Consistent educational quality

-Reduced human effort

-Data-backed decisions on what to publish

-This matters because scaling high-quality content cost-effectively directly impacts engagement, reach, and lead generation.


DEMO 



https://github.com/user-attachments/assets/b177740e-fc63-4020-938b-194159eeb3f3


https://github.com/Agaramsaikrishna/Vedantu/raw/refs/heads/main/videos/Chemistry.mp4





## 🧪 Evaluation Criteria

| Category         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Functionality**| End-to-end pipeline (topic → script → metadata → video)                     |
| **Content Quality**| Aligned with curriculum; editable scripts possible                         |
| **Automation Depth**| Fully automated pipeline, minimal manual steps                            |
| **Code Quality** | Modular, documented, and logged                                            |
| **Relevance**    | Focused on YouTube content creation & engagement                            |
| **UI/UX**        | Simple interface for teachers and creators                                  |

---

## 🔮 Future Improvements

### 🧱 Core Enhancements

- 🔗 Direct **YouTube upload** (via YouTube Data API)
- 🌐 Support for **multi-language** content generation
- ✏️ **Edit script before video** generation 
- 🎙️ UI selection for **voice/avatar style**
- 🔁 Retry system for video generation failures

### 💡 User Experience

- 📥 Add **download buttons** for script/metadata/video
- ▶️ **Embed video preview** inside Streamlit app
- ⏱️ Display **API usage quota warnings**
- 📂 Save **session history** for easy reuse
- 📱 Responsive layout for mobile/tablet devices

### 📊 Admin & Analytics

- 📈 Track generation stats (e.g., most requested topics)
- 📤 Export **PDF lesson plans**
- 🔍 Monitor and log **error rates** & retry logic

---
