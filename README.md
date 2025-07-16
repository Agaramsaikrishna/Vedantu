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
- ✏️ **Edit script before video** generation (WYSIWYG editor)
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
