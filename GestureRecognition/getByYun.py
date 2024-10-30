import time

from PIL import Image
import requests
import base64
from io import BytesIO

ua={"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
# 上传文件
url = 'http://222.201.134.240:5000/predict'
# files = {'file': open('Gesture/images/val/2_0_1.jpg', 'rb')}  # 替换为你的图像路径
files = [
    ('files', open('Gesture/images/val/2_0_1.jpg', 'rb')),
    ('files', open('Gesture/images/val/5_0_1.jpg', 'rb')),
    ('files', open('Gesture/images/val/3_0_1.jpg', 'rb'))
]
start_time=time.time()
response = requests.post(url, files=files,headers=ua)
end_time = time.time()
elapsed_time = end_time - start_time

# 将运行时间转换为毫秒
elapsed_time_ms = elapsed_time * 1000

print(f"程序运行时间：{elapsed_time_ms} 毫秒")
# 处理返回结果
if response.status_code == 200:
    datas = response.json()
    for data in datas['results']:
        predictions = data['predictions']
        image_base64 = data['image']
        print(predictions)
        img_data = base64.b64decode(image_base64)
        img = Image.open(BytesIO(img_data))
        img.show()  # 直接展示图像

else:
    print(f"Error: {response.status_code}, {response.text}")
