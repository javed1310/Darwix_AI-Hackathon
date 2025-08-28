import os
import sys
import trafilatura
from groq import Groq
from typing import Tuple, Optional
from dotenv import load_dotenv

load_dotenv()

# Access your API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --- CENTRALIZED CONFIGURATION ---
CONFIG = {
    "model_name": "llama3-8b-8192",
    "prompt_template": """
    As a "Digital Skeptic" AI, your mission is to help users think critically about online content.
    Analyze the following news article text and generate a "Critical Analysis Report" in Markdown format.
    Do not make a final judgment of "true" or "false." Your goal is to highlight claims, analyze the language,
    and arm the reader with insightful questions.

    **Article Title:** {title}
    **Article Text:**
    ---
    {text}
    ---

    **Generate the report with the following sections:**

    ### Core Claims
    * A bulleted list summarizing the 3-5 most important factual claims the article makes.

    ### Language & Tone Analysis
    * A brief analysis and classification of the article's language (e.g., "Appears neutral and factual," "Uses emotionally charged language," "Reads as a strong opinion piece").

    ### Potential Red Flags
    * A bulleted list identifying any signs of bias or poor reporting, such as loaded terminology, over-reliance on anonymous sources, lack of cited data, or failure to present opposing viewpoints.

    ### Key Entities to Investigate
    * Identify 2-3 key people, organizations, or locations mentioned. For each, suggest a specific thing a reader should investigate.

    ### Verification Questions
    * A list of 3-4 specific, insightful questions a reader should ask to independently verify the article's content.

    ### Counter-Argument Simulation
    * Briefly summarize the main topic of this article from a hypothetical "opposing viewpoint" to starkly highlight its potential biases.
    """
}

# --- CORE FUNCTIONS ---

def fetch_article_content(url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Fetches and extracts the main content and title from a URL using trafilatura.
    Returns (title, text) or (None, error_message).
    """
    print(f"[INFO] Fetching content from: {url}")
    downloaded = trafilatura.fetch_url(url)
    if downloaded is None:
        return None, "Failed to download the article. The URL may be invalid or the site may be blocking requests."
    
    text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
    title = trafilatura.extract_metadata(downloaded).title
    
    if not text:
        return None, "Could not extract a meaningful article from the page."
        
    return title, text

def generate_analysis(title: str, text: str) -> str:
    """
    Generates the critical analysis report using the Groq API with the in-script key.
    """
    print("[INFO] Analyzing with Groq AI... This should be fast! ⚡️")
    try:
        # Initialize the client with the API key from the top of the script
        client = Groq(api_key=GROQ_API_KEY)
        
        prompt = CONFIG["prompt_template"].format(title=title, text=text)

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that analyzes news articles for critical thinking."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=CONFIG["model_name"],
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        error_message = f"An error occurred while communicating with the Groq API: {e}"
        print(f"[ERROR] {error_message}")
        return f"# Analysis Failed\n- {error_message}"

# --- MAIN EXECUTION ---

def main():
    """
    The main function to run the Digital Skeptic tool.
    """
    # Check if the user has replaced the placeholder API key
    if not GROQ_API_KEY or "PASTE_YOUR" in GROQ_API_KEY:
        print("[ERROR] Please paste your Groq API key into the `GROQ_API_KEY` variable at the top of the script.")
        sys.exit(1)
        
    print("🚀 Welcome to the Digital Skeptic AI (Powered by Groq) 🚀")
    print("="*50)
    
    url = input("Please enter the URL of the news article to analyze:\n> ")

    title, text = fetch_article_content(url)

    if text is None:
        # If text is None, the 'title' variable holds the error message
        print(f"[ERROR] {title}")
        return

    analysis_report = generate_analysis(title, text)

    print("\n" + "="*50)
    print("✅ [SUCCESS] Analysis complete! Here is your report:")
    print("="*50 + "\n")
    
    final_report = f"# Critical Analysis Report for: {title}\n\n{analysis_report}"
    print(final_report)
    print("\n" + "="*50)

if __name__ == "__main__":
    main()