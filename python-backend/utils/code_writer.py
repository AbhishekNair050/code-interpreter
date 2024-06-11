import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = " "
llm = ChatGoogleGenerativeAI(model="gemini-pro")


import re


def preprocess_code(code):
    # Remove triple backticks for code blocks
    code = re.sub(r"```python\n?", "", code, flags=re.MULTILINE)
    code = re.sub(r"\n?```", "", code, flags=re.MULTILINE)

    # Split the code into lines
    lines = code.split("\n")

    # Calculate the minimum indentation level
    min_indent = float("inf")
    for line in lines:
        if line.strip():
            min_indent = min(min_indent, len(line) - len(line.lstrip()))

    # Remove the minimum indentation from each line
    preprocessed_lines = []
    for line in lines:
        if line.strip():
            preprocessed_lines.append(line[min_indent:])
        else:
            preprocessed_lines.append("")

    # Join the lines back into a single string
    preprocessed_code = "\n".join(preprocessed_lines)

    return preprocessed_code


def generate_code(file_content, prompt):
    try:
        input_text = f"File content: {file_content}\n\nUser prompt: {prompt}\n\nGenerate Python code that can be executed using the exec() function. call the function as well. NO TEXT AT ALL assume if required Ensure that the generated code is safe and secure, without any malicious or potentially harmful operations."
        result = llm.invoke(input_text)
        raw_code = result.content

        processed_code = preprocess_code(raw_code)

        return processed_code
    except Exception as e:
        print(f"Error generating code: {e}")
        return None
