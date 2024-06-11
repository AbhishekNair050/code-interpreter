# Code Interpreter

## Overview

The **Code Interpreter** project is a Python-based application designed to interpret code from various file formats (PDF, XLSX, CSV, DOCX) using OpenAI's GPT-3.5 API. It allows users to upload files, input prompts, and receive generated Python code as output. The generated code can then be executed, and the results are displayed back to the user.

## Features

- **File Reading**: The application supports reading content from PDF, XLSX, CSV, and DOCX files using appropriate Python libraries.
- **Code Generation**: It leverages Gemini Pro API to generate Python code based on the content of the uploaded files and user prompts.
- **Code Execution**: The generated Python code is executed securely, and the output is captured.
- **User Interface**: Users can interact with the application through a user-friendly interface, providing file uploads and prompt inputs.
- **Robustness**: The system is designed to handle various file formats, user inputs, and edge cases effectively.
- **Security**: Measures are taken to ensure the safe execution of generated code, minimizing the risk of code injection or malicious execution.

## Usage

1. **File Upload**: Users can upload files in PDF, XLSX, CSV, or DOCX format by clicking the "Select File" button.
2. **Prompt Input**: Enter a prompt related to the uploaded file content in the provided input field.
3. **Code Generation**: Once a file and prompt are provided, click the "Generate Code" button to initiate code generation.
4. **Code Execution**: The generated Python code is executed securely, and the output is displayed in the designated area.
5. **Result Display**: The execution result, along with any errors or relevant information, is presented to the user for review.

## Setup

To run the **Code Interpreter** application locally, follow these steps:

1. Clone this repository to your local machine.
2. Replace your Gemini Pro API key in utils/code_writer
3. Navigate to the project directory:

```bash
cd Code-Interpreter
```

3. Run the application using the provided script:

```bash
start.bat
```
It will install all the necessary dependencies, for electron.js dependencies uncomment npm install to install it
```bash
@REM npm install
```
## Testing


https://github.com/AbhishekNair050/code-interpreter/assets/114457983/957b689c-e248-40f0-a21d-62d6c6017df3


To test the functionality of the **Code Interpreter** application, consider the following scenarios:

- Upload files of different formats (PDF, XLSX, CSV, DOCX) with varying content.
- Provide different prompts to observe the variation in generated Python code.
- Test edge cases, such as empty files or prompts, to ensure robustness.
- Verify the security measures implemented during code execution.

## Support

For any issues or inquiries regarding the **Code Interpreter** application, please contact [Abhishek Nair](mailto:abhishek.naiir@gmail.com).
