import io

import torch
import torchvision
from torchvision import transforms
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from torchvision.models.detection.mask_rcnn import MaskRCNNPredictor
#from torchvision.models.detection import FasterRCNN
#from torchvision.models.detection.rpn import AnchorGenerator

from PIL import Image

def transform_image(image_bytes):
  preprocess = transforms.Compose([
    transforms.Resize(255),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
      [0.485, 0.456, 0.406],
      [0.229, 0.224, 0.225]
    )
  ])

  img = Image.open(io.BytesIO(image_bytes))
  return preprocess(img).unsqueeze(0)

def segmentation(num_classes):
  model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
  in_features = model.roi_heads.box_predictor.cls_score.in_features
  model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)

  in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
  hidden_layer = 256
  model.roi_heads.mask_predictor = MaskRCNNPredictor(in_features_mask, hidden_layer, num_classes)

  return model