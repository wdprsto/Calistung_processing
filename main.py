from fastapi import FastAPI, File, UploadFile
from image_preprocessing import RequestImageConverter
# from image_preprocessing import ImagePreprocessor
from image_preprocessing import TextRecognizer
from inferencing import TFLiteInferencer

app = FastAPI()

@app.get("/")
async def root():
    return "Hello World"

@app.post('/predict')
async def create_upload_file(image: UploadFile = File(...)):
    img_file = await image.read()
    converter = RequestImageConverter(img_file)
    converted_image = converter.convert()
    
    # preprocessor = ImagePreprocessor(converted_image)
    # processed_image = preprocessor.process()

    text_recognizer = TextRecognizer(converted_image)
    recognized_text = text_recognizer.recognize_text()

    inferencer = TFLiteInferencer(recognized_text)
    prediction = inferencer.predict()

    return prediction