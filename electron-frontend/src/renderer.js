document.addEventListener('DOMContentLoaded', () => {
    const selectFileButton = document.getElementById('selectFileButton');
    const executeCodeButton = document.getElementById('execute-code');

    selectFileButton.addEventListener('click', async () => {
        const filePath = await window.electron.selectFile();
        if (filePath) {
            const result = await window.electron.uploadFile(filePath);
            if (result.fileContent) {
                document.getElementById('file-content').value = result.fileContent;
            } else {
                document.getElementById('file-content').value = `Error: ${result.error}`;
            }
        } else {
            document.getElementById('file-content').value = 'No file selected.';
        }
    });

    executeCodeButton.addEventListener('click', async () => {
        const fileContent = document.getElementById('file-content').value;
        const prompt = document.getElementById('prompt').value;

        const response = await window.electron.generateCode({ fileContent, prompt });
        const generatedCodeElement = document.getElementById('generated-code').querySelector('code');

        generatedCodeElement.textContent = response.code;
        Prism.highlightElement(generatedCodeElement);  // Apply Prism syntax highlighting

        document.getElementById('output').textContent = `Execution Result:\n${response.output}`;
    });
});
