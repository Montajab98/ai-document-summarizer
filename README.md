# AI Document Summarizer

A Streamlit app that summarizes pasted text using the Google Gemini API.
Supports English and Arabic, with adjustable summary length.

## Features

- Summarize pasted articles, documents, and other text
- Choose English or Arabic output
- Select a short, medium, or detailed summary
- Download the summary as a text file
- Change the Gemini model through Model settings
- Keep the generated summary visible across interface interactions

## Tech Stack

- Python
- Streamlit
- Google Gen AI SDK (`google-genai`)

## Getting Started

### Installation

```bash
git clone https://github.com/Montajab98/ai-document-summarizer.git
cd ai-document-summarizer

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

### Run

```bash
streamlit run app.py
```

## Usage

1. Create a Gemini API key in [Google AI Studio](https://aistudio.google.com/).
2. Enter your API key in the app.
3. Under **Model settings**, select a model available for your API key.
4. Choose the summary language and length.
5. Paste your text and click **Summarize**.
6. Optionally download the summary.

API access is subject to Google's model availability, quotas, and pricing.

## Model Configuration

The model name can be changed through **Model settings**.

You can also set its initial value with the `GEMINI_MODEL` environment
variable before starting the app:

```bash
export GEMINI_MODEL="your-available-model-id"
streamlit run app.py
```

Use a model available for your API key that supports content generation.
If a model is retired or unavailable, update the model name.

## Project Structure

```text
ai-document-summarizer/
├── app.py
├── requirements.txt
└── README.md
```

## Troubleshooting

| Issue | What to check |
|---|---|
| ImportError: cannot import `genai` | Install dependencies from `requirements.txt`. This app uses `google-genai`, not the older `google-generativeai` package. |
| Model unavailable / 404 | Enter an available model ID in Model settings. |
| Access denied / 401 or 403 | Check your API key and permissions. |
| Rate limit or quota / 429 | Check your Gemini API quota and billing. |
| Empty response | Try different input; the response may have been blocked. |

## Privacy and Limitations

- Your pasted text is sent to Google Gemini for processing.
- Do not commit API keys to GitHub.
- This version accepts pasted text; it does not upload or extract files.
- AI-generated summaries may omit details or contain errors. Review
  important summaries against the original text.
- Requested summary lengths are instructions to the model, not strict limits.

## Author

**Montajab Al-Hussein**  
AI Engineer · Sharjah, UAE

[LinkedIn](https://www.linkedin.com/in/moontajab/) ·
[GitHub](https://github.com/Montajab98)
