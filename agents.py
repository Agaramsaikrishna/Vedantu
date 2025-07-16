from agno.agent import Agent, RunResponse, AgentMemory
from agno.models.groq import Groq
#from agno.storage.agent.sqlite import SqlAgentStorage
from agno.memory.db.sqlite import SqliteMemoryDb
from agno.playground import Playground, serve_playground_app
from agno.models.together import Together
from utils.prompts import *
import streamlit as st
from services.saver import save_outputs
import os 
from services.file_reader import read_math_pdf_text , read_science_pdf_text
from services.hey_gen_automation import generate_and_save_video
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
BASE_URL_TOGETHER_AI=os.getenv("BASE_URL")
BASE_URL_GROQ=os.getenv("BASE_URL_GROQ")
VISION_MODEL=os.getenv("VISION_MODEL")
TEXT_FREE_MODEL=os.getenv("TEXT_FREE_MODEL")
MULTI_MODEL=os.getenv("MULTI_MODEL")

DISTILL_LLAMA_GROQ=os.getenv("DISTILL_LLAMA_GROK-70B")
HEY_GEN_KEY=os.getenv("HEY_GEN_KEY_1")


agent = Agent(
    model=Groq(id="llama3-8b-8192",  api_key=GROQ_API_KEY),
    markdown=True,
    
)

# # Print the response in the terminal
# agent.print_response("Generate trending YouTube topics for Class 10 Science")



Trend_discover_agent= Agent(
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  api_key=TOGETHER_API_KEY),
    markdown=True,
    instructions=trend_agent_instruction,
    tools=[read_science_pdf_text, read_math_pdf_text]
    
)

# Trend_discover_agent.print_response("Generate trending YouTube topics for Class 10 chemistry")

Topic_pick_agent= Agent(
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  api_key=TOGETHER_API_KEY),
    markdown=True,
    
    instructions=topic_pick_instructions,
    tools=[Trend_discover_agent]
    
)

# topic_pick_agent.print_response("Generate trending YouTube topics for Class 10 chemistry")

Script_generation_agent=Agent(
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  api_key=TOGETHER_API_KEY),
    markdown=True,
    instructions=script_instructions,
    tools=[Topic_pick_agent]
    
)

# ss=Script_generation_agent.run("Generate trending YouTube topics for Class 10 chemistry")

# print(ss.content[:200])

Meta_data_generation_agent=Agent(
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct",  api_key=GROQ_API_KEY),
   # model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  api_key=TOGETHER_API_KEY),
    markdown=True,
    instructions=meta_data_instructions
    
)


Video_generation_Agent=Agent(
    model=Together(id="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  api_key=TOGETHER_API_KEY),
    markdown=True,
    tools=[generate_and_save_video],
    #instructions=   video_generation_instructions
)


# Video_generation_Agent.print_response(ss.content[:200])


# def multi_agent_pipeline(subject, grade):
#     # Step 1: Get trending topics list
#     trend_response = Trend_discover_agent.run(f"Generate trending YouTube topics for Class {grade} {subject}")
#     print("Trending Topics:", trend_response)
    
#     # Step 2: Pick best topic from topics
#     best_topic_response = Topic_pick_agent.run(f"Choose the best topic from these:\n{trend_response}")
#     print("Best Topic:", best_topic_response)
    
#     # Step 3: Generate script for best topic
    
#     script_response = Script_generation_agent.run(f"Write a detailed script about:\n{best_topic_response}")
#     print("Script:", script_response)
    
#     # Step 4: Generate metadata (title, description, tags)
#     # short_script = script_response[:3000] 
#     metadata_response = Meta_data_generation_agent.run(f"Generate YouTube metadata for topic:\n{best_topic_response}\nScript:\n{script_response}")
#     print("Metadata:", metadata_response)
    
#     if isinstance(script_response.content, str):
#         short_script = script_response.content[:215]
#     else:
#         raise TypeError("Expected string content in RunResponse.")

#     video_response = Video_generation_Agent.run(short_script)
#     print("Video Response (status):", video_response)
    
#     # Step 6: Save all outputs locally in one folder
#     save_outputs(subject, grade, best_topic_response, script_response, metadata_response, video_response)



def multi_agent_pipeline(subject, grade):
    # Step 1: Get trending topics list
    trend_response = Trend_discover_agent.run(f"Generate trending YouTube topics for Class {grade} {subject}")
    
    # Step 2: Pick best topic from topics
    best_topic_response = Topic_pick_agent.run(f"Choose the best topic from these:\n{trend_response}")
    
    # Step 3: Generate script for best topic
    script_response = Script_generation_agent.run(f"Write a detailed script about:\n{best_topic_response}")
    
    # Step 4: Generate metadata
    metadata_response = Meta_data_generation_agent.run(
        f"Generate YouTube metadata for topic:\n{best_topic_response}\nScript:\n{script_response}"
    )

    # Step 5: Generate short summary to pass to video tool
    if isinstance(script_response.content, str):
        short_script = script_response.content[:215]
    else:
        raise TypeError("Expected string content in RunResponse.")

    # Step 6: Generate video via HeyGen tool
    video_response = Video_generation_Agent.run(short_script)

    # Step 7: Save locally
    save_outputs(subject, grade, best_topic_response, script_response, metadata_response, video_response)

    # ✅ FIX: Return the four key outputs
    return best_topic_response, script_response, metadata_response, video_response
