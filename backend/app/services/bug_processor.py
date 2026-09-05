from typing import Optional


def process_bug(
    title: str,
    description: str,
    stack_trace: Optional[str] = None,
    error_log: Optional[str] = None
):
    combined_text = f"""
Title:
{title}

Description:
{description}

Stack Trace:
{stack_trace or "Not provided"}

Error Log:
{error_log or "Not provided"}
""".strip()

    return {
        "title": title,
        "description": description,
        "stack_trace": stack_trace,
        "error_log": error_log,
        "processed_text": combined_text
    }