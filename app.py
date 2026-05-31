import gradio as gr

def echo_search(query):
    return f"EchoVault received: {query}"

demo = gr.Interface(
    fn=echo_search,
    inputs="text",
    outputs="text",
    title="EchoVault 🚀",
    description="AI Memory Search System"
)

demo.launch()