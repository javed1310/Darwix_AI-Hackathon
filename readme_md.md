# 🧐 Digital Skeptic

Digital Skeptic is a Python-based tool powered by the **Groq API** that helps users think critically about online content.  
It analyzes news articles and generates a **Critical Analysis Report** in Markdown format, highlighting claims, tone, potential biases, and verification questions.  

---

## 🚀 Features
- Extracts article content and metadata from a given URL using [trafilatura](https://github.com/adbar/trafilatura).  
- Uses Groq's LLM (default: `llama3-8b-8192`) for **fast AI-powered analysis**.  
- Produces structured reports with:
  - **Core Claims**  
  - **Language & Tone Analysis**  
  - **Potential Red Flags**  
  - **Key Entities to Investigate**  
  - **Verification Questions**  
  - **Counter-Argument Simulation**  

---

## 📦 Requirements
Install dependencies using:

```bash
pip install trafilatura groq
```

Python 3.8+ is recommended.

---

## 🔑 Setup
1. Open the file `digital_skeptic.py`.  
2. Replace the placeholder in the script with your Groq API key:

```python
GROQ_API_KEY = "your_api_key_here"
```

3. Save the file.

---

## ▶️ Usage
Run the script:

```bash
python digital_skeptic.py
```

Enter the URL of a news article when prompted:

```bash
Please enter the URL of the news article to analyze:
> https://example.com/sample-article
```

The program will fetch the article, analyze it, and display a **Critical Analysis Report**.

---

## 📋 Example Output
```
# Critical Analysis Report for: Sample Article

### Core Claims
* Claim 1
* Claim 2
* Claim 3

### Language & Tone Analysis
Appears neutral and factual.

### Potential Red Flags
* Heavy use of anonymous sources
* No supporting data

### Key Entities to Investigate
* Person A – Check background and affiliations
* Organization B – Review prior controversies

### Verification Questions
* Is there independent data supporting this claim?
* Has this topic been covered by other credible outlets?

### Counter-Argument Simulation
From an opposing viewpoint, this article could be interpreted as...
```

---

## ⚠️ Disclaimer
This tool does **not** decide whether content is true or false.  
It is designed to **encourage critical thinking** and help readers evaluate online information more carefully.  

---

## 📜 License
MIT License. Free to use and modify.
