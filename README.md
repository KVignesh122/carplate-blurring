# Car License Plate Blurring with AI Computer Vision

This repository contains a Python implementation for blurring car license plates in images using AI Computer Vision techniques. The project is designed to handle single cars, multiple cars, and even 360-degree images.

## Examples

### Single Car

<p float="left">
  <img src="https://github.com/KVignesh122/carplate_blurring/assets/55841532/96747f7f-3d2b-430e-9955-3e333ff090f6" alt="Single Car" width="500" />
  <img src="https://github.com/KVignesh122/carplate_blurring/assets/55841532/4b6d940b-d703-4372-987a-ca43d1bd0e39" alt="Single Car Blurred" width="500" />
</p>

### Multiple Cars

<p float="left">
  <img src="https://github.com/KVignesh122/carplate_blurring/assets/55841532/cb8784a9-bb3c-45ce-8dc5-464cfc37165c" alt="Muliple Cars" width="500" />
  <img src="https://github.com/KVignesh122/carplate_blurring/assets/55841532/6cee9939-f7e1-419b-b06c-151c067f7b5c" alt="Muliple Cars Blurred" width="500" />
</p>

### 360 Degree Images

<p float="left">
  <img src="https://github.com/KVignesh122/carplate_blurring/assets/55841532/948a25d1-ac64-4808-8a09-89d016dde584" alt="360" width="500" />
  <img src="https://github.com/KVignesh122/carplate_blurring/assets/55841532/2c7ec564-63e3-4286-83b1-ff8559555ef5" alt="360 Blurred" width="500" />
</p>

## Usage

1. Download the `carplate_blur.exe` file from the repository.

2. Open the Terminal in the location where this file is saved. (Right-click anywhere in your window and click "Open in Terminal" option)

3. Run the following command:

   ```bash
   .\carplate_blur.exe "path\to\your\image.jpg"
   ```

   Replace `path\to\your\image.jpg` with the actual path to your image file.

4. Hit Enter and wait around 2 seconds. A `<image_name>_blurred.jpg` file will be created in the same location as your original image.

### Example

```bash
.\carplate_blur.exe "C:\Users\YourUsername\Pictures\car.jpg"
```

## Technical Information

The code is written purely in Python 3 using the latest version of OpenCV. The implementation leverages computer vision techniques to detect and blur car license plates in images. The project is distributed under the Apache 2.0 License.
