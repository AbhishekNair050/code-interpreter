const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
        },
    });

    mainWindow.loadFile('src/index.html');

    ipcMain.handle('select-file', async () => {
        const { canceled, filePaths } = await dialog.showOpenDialog(mainWindow, {
            properties: ['openFile'],
            filters: [{ name: 'Documents', extensions: ['pdf', 'xlsx', 'csv', 'docx'] }],
        });
        if (!canceled && filePaths.length > 0) {
            return filePaths[0];
        }
        return null;
    });

    ipcMain.handle('upload-file', async (event, filePath) => {
        try {
            const formData = new FormData();
            formData.append('file', fs.createReadStream(filePath));

            const response = await axios.post('http://localhost:5000/upload-file', formData, {
                headers: formData.getHeaders(),
            });

            return response.data;
        } catch (error) {
            console.error('Error uploading file:', error);
            return { error: 'Failed to upload file.' };
        }
    });

    ipcMain.handle('generate-code', async (event, data) => {
        try {
            const response = await axios.post('http://localhost:5000/generate-code', data, {
                headers: { 'Content-Type': 'application/json' },
            });
            return response.data;
        } catch (error) {
            console.error('Error generating code:', error);
            return { code: '', output: 'Failed to generate code.' };
        }
    });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
