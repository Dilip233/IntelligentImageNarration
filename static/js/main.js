// Intelligent Image Narration System - Frontend JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const uploadForm = document.getElementById('upload-form');
    const imageInput = document.getElementById('image-input');
    const imagePreview = document.getElementById('image-preview');
    const previewContainer = document.getElementById('preview-container');
    const submitBtn = document.getElementById('submit-btn');
    const loading = document.getElementById('loading');
    const resultsSection = document.getElementById('results');
    const errorSection = document.getElementById('error');
    const captionText = document.getElementById('caption-text');
    const audioPlayer = document.getElementById('audio-player');
    const audioSource = document.getElementById('audio-source');
    const errorText = document.getElementById('error-text');
    const newImageBtn = document.getElementById('new-image-btn');
    const retryBtn = document.getElementById('retry-btn');
    const replayBtn = document.getElementById('replay-btn');

    // File input change handler - Show preview
    imageInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
                imagePreview.alt = 'Preview of ' + file.name;
            };
            reader.readAsDataURL(file);
        }
    });

    // Form submission handler
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const file = imageInput.files[0];
        if (!file) {
            showError('Please select an image file.');
            return;
        }

        // Hide previous results/errors
        hideAllSections();
        
        // Show loading
        loading.style.display = 'block';

        try {
            // Create form data
            const formData = new FormData();
            formData.append('image', file);

            // Send request to server
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok && data.success) {
                // Show results
                showResults(data);
            } else {
                // Show error
                showError(data.error || 'An error occurred while processing the image.');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Network error. Please check your connection and try again.');
        } finally {
            loading.style.display = 'none';
        }
    });

    // Show results
    function showResults(data) {
        captionText.textContent = data.caption;
        audioSource.src = data.audio_url;
        audioPlayer.load();
        
        resultsSection.style.display = 'block';
        
        // Auto-play audio for accessibility
        audioPlayer.play().catch(err => {
            console.log('Auto-play prevented:', err);
            // If auto-play is blocked, user can click the play button
        });

        // Announce to screen readers
        announceToScreenReader('Image analysis complete. ' + data.caption);
    }

    // Show error
    function showError(message) {
        errorText.textContent = message;
        errorSection.style.display = 'block';
        
        // Announce error to screen readers
        announceToScreenReader('Error: ' + message);
    }

    // Hide all sections
    function hideAllSections() {
        resultsSection.style.display = 'none';
        errorSection.style.display = 'none';
        loading.style.display = 'none';
    }

    // Reset form for new image
    function resetForm() {
        uploadForm.reset();
        imagePreview.style.display = 'none';
        imagePreview.src = '';
        hideAllSections();
    }

    // New image button handler
    newImageBtn.addEventListener('click', resetForm);

    // Retry button handler
    retryBtn.addEventListener('click', resetForm);

    // Replay audio button handler
    replayBtn.addEventListener('click', function() {
        audioPlayer.currentTime = 0;
        audioPlayer.play();
        announceToScreenReader('Replaying audio narration');
    });

    // Announce messages to screen readers
    function announceToScreenReader(message) {
        const announcement = document.createElement('div');
        announcement.setAttribute('role', 'status');
        announcement.setAttribute('aria-live', 'polite');
        announcement.className = 'sr-only';
        announcement.textContent = message;
        document.body.appendChild(announcement);
        
        // Remove after announcement
        setTimeout(() => {
            document.body.removeChild(announcement);
        }, 1000);
    }

    // Keyboard shortcuts for accessibility
    document.addEventListener('keydown', function(e) {
        // Alt + N: New image
        if (e.altKey && e.key === 'n') {
            e.preventDefault();
            resetForm();
            imageInput.focus();
        }
        
        // Alt + R: Replay audio (if available)
        if (e.altKey && e.key === 'r' && resultsSection.style.display === 'block') {
            e.preventDefault();
            replayBtn.click();
        }
    });
});
