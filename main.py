import asyncio

import streamlit as st
from kiota_abstractions.api_error import APIError

from api import execute_ap, resolve_ap, serialize

TITLE = "API Generation Demo"
QUESTIONS = {
    "Select a question…": None,
    "Discrete Mathematics": True,
}

st.set_page_config(page_title=TITLE, layout="centered")

st.title(TITLE)
st.markdown("Pick a question below to transform it into an AP")

selected = st.selectbox("Choose a question", list(QUESTIONS.keys()))

if not QUESTIONS.get(selected):
    st.info("Select a question from the dropdown to see results here.")
    st.stop()


# ── Resolve AP ──────────────────────────────
with st.spinner("Fetching…"):
    try:
        data = asyncio.run(resolve_ap(selected))
    except APIError as exc:
        st.error(f"Request failed with status {exc.response_status_code}")
        st.stop()

st.divider()
if data.source == "found":
    st.success(
        "**200 OK** — Analytical Pattern retrieved from the database.",
        icon="✅",
    )
else:
    st.warning(
        "**201 Created** — No matching AP was found; a new one was generated.",
        icon="⚙️",
    )
if data.score and data.score.double:
    st.metric("Similarity score", f"{data.score.double:.6f}")

st.subheader("Analytical Pattern")
st.json(serialize(data))


# ── Execute AP ──────────────────────────────
if st.button("▶ Run AP", type="secondary", use_container_width=True):
    with st.spinner("Running AP…"):
        result = asyncio.run(execute_ap(data))

    st.subheader("Execution Result")
    st.json(serialize(result))
