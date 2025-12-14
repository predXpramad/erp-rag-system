def build_prompt(question: str, context_chunks: list) -> str:
    context_text = "\n\n".join(context_chunks)

    return f"""
You are an ERP and ML documentation assistant.

Answer the question ONLY using the information in the CONTEXT.
Do NOT add external knowledge.

FORMAT RULES (MANDATORY):
- Use a clear heading
- Use numbered points
- Highlight key terms in **bold**
- Each point should be on a new line
- Keep the answer concise and structured

If the answer is not found, say:
"Information not available in ERP documents."

CONTEXT:
{context_text}

QUESTION:
{question}

ANSWER (use structured format):
""".strip()
