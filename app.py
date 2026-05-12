import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------
# PAGE CONTENT
# -----------------------------------

st.title("My Streamlit App")

st.write("""
This is the main page content.

You can place:
- text
- charts
- tables
- controls
- filters
- metrics

above the Pyvis graph.
""")

st.divider()

# -----------------------------------
# LOAD EXISTING PYVIS HTML FILE
# -----------------------------------

html_file = "graphs/graph_1.txt_Preso.html"

with open(html_file, "r", encoding="utf-8") as f:
    pyvis_html = f.read()

# -----------------------------------
# DISPLAY PYVIS GRAPH AT THE BOTTOM
# -----------------------------------

st.subheader("Interactive Network")

components.html(
    pyvis_html,
    height=800,
    scrolling=True
)