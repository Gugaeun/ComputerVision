# 👁 Computer Vision Study

OpenCV와 딥러닝을 활용한 컴퓨터 비전 실습 코드를 정리한 저장소입니다.
이미지 처리 기초부터 딥러닝 기반 객체 탐지·분할, 실시간 영상 분석, Vision Transformer, 3D 데이터 처리까지 단계적으로 학습했습니다.

---

## 📚 Study Overview

| 단계 | 챕터 | 주제 |
|---|---|---|
| 1. 영상 처리 기초 | ch3 ~ ch5 | 이미지 입출력, 필터링, Edge Detection, 특징 추출, OCR 기반 미니 프로젝트 |
| 2. GUI & 실시간 처리 | ch6 | PyQt5 기반 비디오 특수 효과 애플리케이션 |
| 3. 딥러닝 기초 | ch7 ~ ch8 | MLP·CNN으로 MNIST/CIFAR-10 분류 |
| 4. 객체 탐지 & 분할 | ch9 | **YOLOv3 객체 탐지**, DeepLab 시맨틱 분할, Mask R-CNN 인스턴스 분할, 배경 합성 |
| 5. 실시간 영상 분석 | ch10 | Optical Flow 모션 추적, **YOLOv3 + SORT 실시간 다중 객체 추적**, MediaPipe(얼굴/손/포즈/AR) |
| 6. 최신 아키텍처 | ch11 | **Vision Transformer(ViT)**로 CIFAR-10 분류 |
| 7. 3D 비전 | ch12 | 3D 포인트클라우드 분류 (ModelNet10) |

---

## ⭐ 주요 실습 내용

### 🔹 영상 처리 기초 (ch3~ch5)
- 색상 공간 변환, 필터링(Blur/Gaussian/Median)
- Canny/Sobel Edge Detection, Contour 추출
- 계산기·전화번호 인식 등 미니 프로젝트

### 🔹 딥러닝 기반 객체 인식 (ch7~ch9)
- MLP/CNN으로 MNIST, CIFAR-10 이미지 분류
- **YOLOv3**로 정지 영상에서 다중 객체 탐지
- DeepLabV3(ADE20K)로 시맨틱 분할, Mask R-CNN으로 인스턴스 분할
- pixellib 기반 배경 블러·합성 GUI

### 🔹 실시간 영상 분석 (ch10)
- Farneback / Lucas-Kanade Optical Flow로 모션 추적
- **YOLOv3 + SORT 알고리즘**으로 웹캠 실시간 인물 탐지·추적 (ID 부여)
- MediaPipe로 얼굴 검출, 얼굴 랜드마크(Face Mesh), 손 추적, 포즈 추정 + AR 필터(증강현실 오브젝트 합성) 구현

### 🔹 최신 딥러닝 아키텍처 (ch11~ch12)
- Vision Transformer(ViT)를 직접 구현하여 CIFAR-10 분류 (Patch Embedding, Multi-Head Attention 등)
- PointNet 계열 구조로 3D 포인트클라우드(ModelNet10) 분류

---

## 💡 What I Learned

- 고전적 영상 처리(필터링, 엣지 검출)부터 딥러닝 기반 인식까지 컴퓨터 비전의 전체 흐름을 경험
- YOLO 기반 객체 탐지 모델을 실시간 영상에 적용하고, SORT로 프레임 간 객체를 추적하는 파이프라인 구현
- 시맨틱/인스턴스 분할의 차이를 실습을 통해 체감
- Transformer 구조가 이미지 분류에 어떻게 적용되는지 직접 구현하며 이해
- 2D 이미지뿐 아니라 3D 포인트클라우드 데이터 처리 경험

---

## 📝 관련 저장소

- [기초 실습 모음 (Practicum)](https://github.com/Gugaeun/Practicum)
- [메인 프로젝트: CNN Multi-Framework](https://github.com/Gugaeun/cnn-multi-framework) — 이 저장소에서 다룬 CNN·CIFAR-10 학습 경험을 NumPy/PyTorch/Keras 비교, ONNX 변환, API 서빙으로 확장한 프로젝트

---

## 🛠 Tech Stack

`Python` `OpenCV` `TensorFlow/Keras` `YOLOv3` `SORT` `MediaPipe` `pixellib (DeepLab, Mask R-CNN)` `PyQt5`
