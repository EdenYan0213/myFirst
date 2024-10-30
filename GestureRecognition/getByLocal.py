
import time
import torch
from PIL import Image
import platform
import pathlib
plt = platform.system()
if plt == 'Windows':
   pathlib.PosixPath = pathlib.WindowsPath

# Load model
model = torch.hub.load('.', 'custom', path="runs/train/exp21/weights/best.pt", source='local')

img_paths = [
    "Gesture/images/val/7_0_1.jpg",
    "Gesture/images/val/7_0_2.jpg",
    "Gesture/images/val/6_0_3.jpg"
    # 添加更多的图片路径
]
images = []
for img_path in img_paths:
    img = Image.open(img_path)
    images.append(img)

start_time = time.time()

results = model(images)
end_time = time.time()
elapsed_time = end_time - start_time

# 将运行时间转换为毫秒
elapsed_time_ms = elapsed_time * 1000

print(f"程序运行时间：{elapsed_time_ms} 毫秒")
print(results)
print(dir(results))
imgs=results.render()
predict_class=results.pred

for img,result in zip(imgs,predict_class):
    print(int(result[0, -1].item()))
results.show()


