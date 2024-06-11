const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
    selectFile: () => ipcRenderer.invoke('select-file'),
    uploadFile: (filePath) => ipcRenderer.invoke('upload-file', filePath),
    generateCode: (data) => ipcRenderer.invoke('generate-code', data),
});
