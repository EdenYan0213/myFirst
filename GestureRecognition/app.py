from flask import Flask, request, jsonify
import torch
from PIL import Image
import io
import base64

import platform
import pathlib
plt = platform.system()
if plt == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath
app = Flask(__name__)


model = torch.hub.load('.', 'custom', path="runs/train/exp21/weights/best.pt", source='local')



@app.route('/predict', methods=['POST'])
def predict():
    if 'files' not in request.files:
        return jsonify({'error': 'No file part'})

    files = request.files.getlist('files')
    results = []
    images = []


    for file in files:
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            image = Image.open(file.stream)
            images.append(image)

    result = model(images)
    imgs = result.render()
    predict_classes = result.pred
    
    for img, predict_class in zip(imgs, predict_classes):
        output_image = Image.fromarray(img)
        clas = int(predict_class[0, -1].item())
        img_byte_arr = io.BytesIO()
        output_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')
        results.append({
            'predictions': clas,
            'image': img_base64
        })
    
    return jsonify({'results': results})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)