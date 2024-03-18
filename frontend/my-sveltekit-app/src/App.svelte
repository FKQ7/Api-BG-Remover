<script>
    let file = null;
    let decodedImage = null;

    async function uploadImage() {
        if (!file) {
            console.error('No file selected');
            return;
        }

        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await fetch('http://127.0.0.1:8000/api/upload_image/', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            console.log('Image uploaded successfully:', data);
            if (data && data.image_data) {
                decodeImage(data.image_data);
            } else {
                console.error('No image data received');
            }
        } catch (error) {
            console.error('Error uploading image:', error);
        }
    }

    function decodeImage(imageData) {
        const binaryString = atob(imageData);
        const byteArray = new Uint8Array(binaryString.length);
        for (let i = 0; i < binaryString.length; i++) {
            byteArray[i] = binaryString.charCodeAt(i);
        }
        const blob = new Blob([byteArray], { type: 'image/png' });
        decodedImage = URL.createObjectURL(blob);
    }

    function handleFileInput(event) {
        const [uploadedFile] = event.target.files;
        file = uploadedFile;
    }
</script>

<main>
    <h1>Upload Image</h1>
    <input type="file" accept="image/*" on:change={handleFileInput}>
    <button on:click={uploadImage}>Upload</button>

    {#if decodedImage}
        <h2>Decoded Image</h2>
        <img src={decodedImage} alt="Decoded Image">
    {/if}
</main>
