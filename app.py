import streamlit as st
import google.generativeai as genai

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Document Summarizer",
    page_icon="🤖",
    layout="centered"
)

# ── Header ─────────────────────────────────────────────────────────────────────
st.title(" AI Document Summarizer")
st.markdown("Powered by Google Gemini | Built by **Montajab Al-Hussein**")
st.divider()

# ── API Key Input ──────────────────────────────────────────────────────────────
api_key = st.text_input(
    "🔑 Enter your Gemini API Key",
    type="password",
    placeholder="AIza..."
)

# ── Language Selection ─────────────────────────────────────────────────────────
language = st.selectbox(
    " Summary Language",
    ["English", "Arabic (العربية)"]
)

# ── Summary Length ─────────────────────────────────────────────────────────────
length = st.selectbox(
    "Summary Length",
    ["Short (3-5 sentences)", "Medium (1 paragraph)", "Detailed (3 paragraphs)"]
)

# ── Text Input ─────────────────────────────────────────────────────────────────
st.markdown("###  Paste your text below:")
user_text = st.text_area(
    "",
    height=250,
    placeholder="Paste any article, document, or text here..."
)

# ── Summarize Button ───────────────────────────────────────────────────────────
if st.button("✨ Summarize", use_container_width=True, type="primary"):

    if not api_key:
        st.error("Please enter your Gemini API Key.")
    elif not user_text.strip():
        st.error("Please paste some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.0-flash")

                prompt = f"""
You are an expert summarizer.
Summarize the following text in {language}.
Length: {length}.
Be clear, concise, and preserve the key points.

Text:
{user_text}
"""
                response = model.generate_content(prompt)
                summary = response.text

                st.divider()
                st.markdown("### Summary:")
                st.success(summary)

                st.download_button(
                    label="⬇️ Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built with Streamlit + Google Gemini API | Montajab Al-Hussein 🇦🇪")