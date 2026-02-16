# Computer Vision homework for Lady Margaret Hall, University of Oxford

This repository contains a series of six comprehensive homework assignments from the "Advanced Artificial Intelligence and Machine Learning: Computer Vision" summer school at Lady Margaret Hall, University of Oxford. 
The projects are implemented in **PyTorch** and cover a progression from supervised image classification to generative adversarial networks (GANs) and multimodal transformers.

## 📂 Project Overview

| Assignment | Task | Model Architecture | Key Concepts |
| :--- | :--- | :--- | :--- |
| **HW1** | Image Classification | CNN with Inception Bottlenecks | Optimization, Regularization, CIFAR-10 |
| **HW2** | Object Detection | Faster R-CNN (MobileNetV3) | RPN, ROI Pooling, COCO Metrics |
| **HW3** | Image Translation | Pix2Pix (Conditional GAN) | U-Net, PatchGAN, Paired Translation |
| **HW4** | Style Transfer | CycleGAN | Cycle Consistency, Unpaired Translation |
| **HW5** | Video Classification | 3D ResNet-18 | Spatiotemporal Features, UCF101 |
| **HW6** | Multimodal AI | CLIP (Contrastive Learning) | Dual Encoders, Zero-Shot Learning |

---

## 🏗️ Architecture Documentation

### 1. Inception-style CNN (HW1)
Designed for efficient feature extraction on the CIFAR-10 dataset.
* **Bottleneck Layers**: Parallel paths with $1 \times 1$, $3 \times 3$, and $5 \times 5$ convolutions to capture multi-scale features.
* **Global Average Pooling**: Replaces heavy fully-connected layers to reduce overfitting.
* **Optimization**: Implements AdamW with Cosine Annealing learning rate scheduling.

### 2. Faster R-CNN (HW2)
A two-stage object detection framework used for vehicle recognition.
* **Backbone**: MobileNetV3-Large with a Feature Pyramid Network (FPN).
* **Region Proposal Network (RPN)**: Learns to propose candidate object bounding boxes.
* **ROI Heads**: Performs Region of Interest (ROI) pooling to classify proposals and refine coordinates.

### 3. Pix2Pix cGAN (HW3)
A conditional generative adversarial network for paired image-to-image translation (Edges2Shoes).
* **Generator**: A **U-Net** architecture with skip connections to preserve low-level structural detail from input sketches.
* **Discriminator**: A **PatchGAN** that classifies $N \times N$ patches as real or fake, encouraging high-frequency crispness.
* **Loss Function**: Combined Adversarial Loss + $L_1$ Reconstruction Loss.

### 4. CycleGAN (HW4)
Enables style transfer between domains (Selfie $\leftrightarrow$ Anime) without paired examples.
* **Cycle Consistency**: Enforces the constraint $G_{BA}(G_{AB}(A)) \approx A$ to ensure the model doesn't lose the original content.
* **Residual Blocks**: The generators utilize ResNet blocks to maintain stable gradients in deep translation layers.
* **Identity Loss**: Prevents the generator from changing the color palette unnecessarily.

### 5. 3D ResNet-18 (HW5)
Extends 2D convolutions into the temporal dimension for action recognition.
* **3D Convolutions**: Filters of shape $(C, T, H, W)$ capture motion across frames.
* **Temporal Pooling**: Aggregates information over the duration of a video clip.
* **Fine-tuning**: Leverages weights pretrained on the Kinetics-400 dataset for the UCF101 task.

### 6. CLIP: Contrastive Language-Image Pre-training (HW6)
A multimodal architecture that connects text and images in a shared embedding space.
* **Image Encoder**: ResNet-50 backbone.
* **Text Encoder**: DistilBERT transformer.
* **Contrastive Loss**: Uses a symmetric cross-entropy loss over a similarity matrix to maximize the cosine similarity of correct (image, text) pairs.

---
### Prerequisites
* Python 3.9+
* PyTorch 2.x
* CUDA-enabled GPU (Highly recommended)
