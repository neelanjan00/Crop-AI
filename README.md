<img src="https://firebasestorage.googleapis.com/v0/b/neelanjan-manna.appspot.com/o/project-images%2FCropAI.jpeg?alt=media&token=f0abab94-53d7-4c23-92bb-6931283f85e4" width="400" />
<h1 align="center">Welcome to Crop AI 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/NeelanjanManna" target="_blank">
    <img alt="Twitter: NeelanjanManna" src="https://img.shields.io/twitter/follow/NeelanjanManna.svg?style=social" />
  </a>
</p>

> [This is the backend API of the project, the frontend mobile application can be found <a href="https://github.com/neelanjan00/Crop-AI-Frontend"> here </a>] A diagnostic AI-enabled mobile app which is able to classify upto 38 different plant diseases ranging for 14 crops and vegetables. The application makes use of the VGG-Net CNN architecture for the purpose of multi-class classification of the images of infected plant leaves. The trained model was then deployed using a Flask backend server, along with a Flutter based frontend mobile application to interact with the REST API.

### 🏠 [Homepage](https://github.com/neelanjan00/Crop-AI)

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python app.py
```
## API Routes
| Route  | Method | Field Name | Input Type | Returns |
|:-------|--------|------------|------------|:------------|
| `/`  |    POST    | InputImg | Image File (png or jpg or jpeg) | Returns a string bearing the name of the plant disease. |

## Author

👤 **Neelanjan Manna**

* Website: https://neelanjanmanna.ml/
* Twitter: [@NeelanjanManna](https://twitter.com/NeelanjanManna)
* Github: [@neelanjan00](https://github.com/neelanjan00)
* LinkedIn: [@neelanjan00](https://linkedin.com/in/neelanjan00)

## Show your support

Give a ⭐️ if this project helped you!
