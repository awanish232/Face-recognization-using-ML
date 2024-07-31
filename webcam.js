// webcam.js
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
        video.play();
    })
    .catch((err) => {
        console.error('Error accessing the webcam:', err);
    });

video.addEventListener('play', () => {
    setInterval(() => {
        context.drawImage(video, 0, 0, 640, 480);
        const imageData = canvas.toDataURL('image/jpeg');

        // Send imageData to the server for prediction using Axios
        axios.post('/predict', imageData)
            .then(response => {
                const predictedEmotion = response.data.emotion;
                // Display the predicted emotion on the webpage
                document.getElementById('prediction').innerText = `Predicted Emotion: ${predictedEmotion}`;
            })
            .catch(error => {
                console.error('Error making prediction:', error);
            });
    }, 100);
});
