# Detect AI
## for detecting AI generated text, images, audio and vedio

## New Feature: Image Upload

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

## New Feature: JSON to CSV Conversion

We have added a new feature to convert JSON files to CSV format in the server directory. This feature allows users to easily convert JSON data to CSV format for further processing.

### How to Use the JSON to CSV Conversion Script

1. Place the JSON file you want to convert in the server directory.
2. Run the `json_to_csv.py` script located in the `server` directory.
3. The script will read the JSON file and create a corresponding CSV file in the same directory.

### Example Usage

To convert a JSON file named `example.json` to a CSV file named `output.csv`, run the following command:
```
python server/json_to_csv.py
```

The script will read the `example.json` file and create an `output.csv` file with the converted data.
