# tool for train and test image model

## Image Upload Functionality

We have added a new feature to upload images on the main page. This feature allows users to upload image files, which will be processed by the server.

### How to Use the Image Upload Feature

1. Open the main page of the application.
2. You will see a form to upload images.
3. Click on the "Choose File" button to select an image file from your device.
4. Click on the "Upload Image" button to upload the selected image.
5. The server will process the image and return a response indicating the success of the upload.

### Endpoint for Image Upload

The image upload functionality is handled by the `/uploadimage/` endpoint. You can use this endpoint to upload image files programmatically.

Example:
```
POST /uploadimage/
Content-Type: multipart/form-data
File: <image_file>
```

The server will respond with a JSON object containing the filename and a success message.
