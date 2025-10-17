import torch

import onnx
onnx_model = onnx.load("my_model.onnx")
onnx.checker.check_model(onnx_model)

import onnxruntime as ort
import numpy as np

s = ort.InferenceSession('my_model.onnx')
# outputs = ort_sess.run(None, {'input': text.numpy(),
#                               'offsets':  torch.tensor([0]).numpy()})
# # Print Result
# result = outputs[0].argmax(axis=1)+1
# print("This is a %s news" %ag_news_label[result[0]])

