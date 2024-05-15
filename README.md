# Car License Plate Blurring with AI Computer Vision

This repository contains a Python implementation for blurring car license plates in images using AI Computer Vision techniques. The project is designed to handle single cars, multiple cars, and even 360-degree images.

## Table of Contents
- [Usage](#usage)
- [Technical Information](#technical-information)
- [Examples](#examples)
- [License](#license)

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

## Examples

<>

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
