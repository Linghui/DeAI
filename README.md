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

## New Feature: Cat Control on Canvas

We have added a new feature to control a cat using the arrow keys on a new page created with canvas. This feature allows users to interact with a cat on a canvas element and control its movement using the arrow keys.

### How to Use the Cat Control Feature

1. Open the main page of the application.
2. Navigate to the `/cat_canvas` endpoint.
3. You will see a canvas element with a cat drawn on it.
4. Use the arrow keys (Up, Down, Left, Right) to control the movement of the cat on the canvas.

### Endpoint for Cat Control

The cat control functionality is handled by the `/cat_canvas` endpoint. You can use this endpoint to access the cat control feature.

Example:
```
GET /cat_canvas
```

The server will respond with an HTML page containing the canvas element and JavaScript code to control the cat.

## New Feature: Tetris Game with Backend Score Collection

We have added a new feature to play a Tetris game and collect scores using a backend endpoint. This feature allows users to play a Tetris game implemented using JavaScript and HTML5 Canvas, and submit their scores to the backend for storage.

### How to Access and Play the Tetris Game

1. Open the main page of the application.
2. Navigate to the `/tetris` endpoint.
3. You will see a canvas element with the Tetris game.
4. Use the arrow keys (Up, Down, Left, Right) to control the movement of the Tetris pieces.
5. The score will be displayed on the screen, and the game will end when the pieces reach the top of the canvas.

### Endpoint for Tetris Game

The Tetris game functionality is handled by the `/tetris` endpoint. You can use this endpoint to access the Tetris game.

Example:
```
GET /tetris
```

The server will respond with an HTML page containing the canvas element and JavaScript code to play the Tetris game.

### Backend Score Collection

The backend score collection functionality is handled by the `/submit_score/` endpoint. You can use this endpoint to submit scores to the backend for storage.

Example:
```
POST /submit_score/
Content-Type: application/json
{
    "score": <score_value>
}
```

The server will respond with a JSON object containing a success message.
