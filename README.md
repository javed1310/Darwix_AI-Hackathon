Digital Skeptic AI 🧠
Empowering Critical Thinking in an Age of Information Overload.

The Digital Skeptic is a command-line tool designed to be your critical thinking partner. In a world saturated with online information, it's easy to fall for bias, spin, or logical fallacies. This tool takes the URL of a news article, scrapes its content, and uses a high-speed Large Language Model (LLM) to perform a skeptical analysis.

It does not label articles as "true" or "false." Instead, it automates the initial analysis of claims, language, and potential red flags, freeing up your mental energy to make your own informed judgments.

Key Features
Intelligent Content Scraping: Uses the trafilatura library to accurately extract the main article text.

High-Speed AI Analysis: Powered by the Groq API with Llama 3 for incredibly fast, real-time analysis.


Secure API Key Management: Uses a .env file to securely manage your API key, keeping it out of the source code. 


Comprehensive Reporting: Generates a detailed Markdown report with distinct sections:

Core Claims: A summary of the main factual claims.

Language & Tone Analysis: Classification of the article's language.

Potential Red Flags: Highlights signs of bias or poor reporting.

Key Entities to Investigate: Identifies people and organizations for further research.

Verification Questions: Provides insightful questions to guide independent verification.

Counter-Argument Simulation: Presents a hypothetical opposing viewpoint to highlight potential biases.

Technology Stack ⚙️
Language: Python 3.8+

AI Backend: Groq API (Llama 3)

Web Scraping: trafilatura


Configuration: python-dotenv for API key management. 

🔧 Setup and Installation
Follow these steps to get the Digital Skeptic AI running on your local machine.

1. Prerequisites
Make sure you have Python 3.8 or newer installed.

2. Download the Project Files
Download digital_skeptic.py, requirements.txt, and .gitignore to a new folder on your computer.

3. Set Up Your API Key (Create a .env file)
This project securely manages your Groq API key using a 

.env file. 

Get your key from the GroqCloud Console.

In your project folder, create a new file named .env.

Add the following line to the .env file, replacing the placeholder with your actual key:

GROQ_API_KEY="gsk_YourActualApiKeyHere"
The included 

.gitignore file ensures this file is never accidentally committed to a repository. 

4. Install Dependencies
Open your terminal or command prompt, navigate to the project folder, and run the following command. This will read the requirements.txt file and install all the necessary libraries.

Bash

pip install -r requirements.txt
🚀 Usage
Open your terminal or command prompt.

Navigate to the directory where you saved the project files.

Run the script with the following command:

Bash

python digital_skeptic.py
The script will prompt you to enter the URL of the news article you wish to analyze. Paste the URL and press Enter.

📄 Example Output
After analyzing an article, the tool will produce a report similar to this:

Markdown

# Critical Analysis Report for: [Article Title]

### Core Claims
* Claim 1...
* Claim 2...
* Claim 3...

### Language & Tone Analysis
The language in this article appears neutral and factual, primarily using objective statements to report on the events.

### Potential Red Flags
* The article quotes experts from a single organization without presenting counterarguments from other experts in the field.
* A key statistic is mentioned without a direct link or reference to the source study.

### Key Entities to Investigate
* **The Global Research Institute:** Investigate the institute's primary funding sources to understand any potential commercial or political leanings.
* **Dr. Eva Rostova:** Research Dr. Rostova's previous publications and affiliations to determine her area of expertise and any known biases.

### Verification Questions
1. Can I find the original study that the article's key statistic is based on?
2. Are there reports from other news agencies that cover this same topic, and do they corroborate the findings?
3. What do other recognized experts in this field say about the claims made in this article?

### Counter-Argument Simulation
From an opposing viewpoint, the findings presented could be interpreted as an isolated incident rather than a widespread trend. Another perspective might argue that the data is preliminary and that drawing firm conclusions at this stage is premature without further peer review.
💡 Configuration
You can easily customize the AI's behavior by editing the CONFIG dictionary at the top of the digital_skeptic.py file.

"model_name": Change the Groq model used for analysis (e.g., from "llama3-8b-8192" to "llama3-70b-8192").

"prompt_template": Modify the main prompt to change the AI's instructions, tone, or the structure of the final report.

License
This project is licensed under the MIT License.
