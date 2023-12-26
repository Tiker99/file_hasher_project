async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch('/upload/', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        alert('File uploaded. File ID: ' + data.file_id);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function getFileMD5() {
    try {
        const fileID = document.getElementById('fileIdInput').value
        const response = await fetch(`/files/${fileID}`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        alert('File md5 is: ' + data.md5_hash);

    } catch (error) {
        console.error('Error:', error.message);
        return null;
    }
}

