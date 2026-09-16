# Industrial Defect Detection

An AI-powered computer vision system for **UAV-based industrial surface inspection**.

This project focuses on developing an automated inspection pipeline that uses **RGB and thermal imagery** captured from UAVs to identify, localize, and analyze visible and thermal anomalies on industrial structures.

## Current Objective

The current development is focused on **V1 visible defect detection using RGB imagery**.

The objective is to build a reliable computer vision pipeline that can:

* Detect industrial inspection regions/panels.
* Localize visible defects.
* Segment defect regions where required.
* Extract defect-related measurements for further analysis.
* Provide a foundation for integrating thermal-based defect analysis.

## V1 Computer Vision Pipeline

```text
UAV Camera
    │
    ▼
RGB Image
    │
    ▼
Panel / Inspection Region Detection
    │
    ▼
Defect Detection
    │
    ▼
Defect Segmentation
    │
    ▼
Defect Analysis
    │
    ▼
Inspection Results
```

## Technology Stack

* Python
* PyTorch
* OpenCV
* Ultralytics YOLO
* Computer Vision
* Object Detection
* Image Segmentation
* UAV Inspection

## Development Status

### Completed

* RGB inspection dataset preparation
* Dataset analysis
* YOLO-based model development
* Model training
* Training metrics analysis
* Segmentation evaluation
* Prediction visualization

### In Progress

* Visible defect detection pipeline
* Defect localization and segmentation
* Model evaluation and optimization
* Inspection-result analysis

### Planned

* Thermal image processing
* RGB + Thermal inspection pipeline
* Defect severity / anomaly analysis
* UAV deployment pipeline
* Real-time inference
* Integration with the larger autonomous UAV inspection system

## Project Architecture

The long-term system is designed around a modular UAV inspection architecture:

```text
                    UAV
                     │
          ┌──────────┴──────────┐
          │                     │
       RGB Camera          Thermal Camera
          │                     │
          ▼                     ▼
   RGB Processing        Thermal Processing
          │                     │
          └──────────┬──────────┘
                     ▼
              Defect Analysis
                     │
                     ▼
             Inspection Report
```

The current implementation is concentrating on the **RGB branch first**, before introducing thermal data and multimodal defect analysis.

## Why This Project?

Manual industrial inspection can be time-consuming, difficult to scale, and dependent on human observation.

The goal of this project is to develop a vision-based inspection system that can automatically process UAV imagery and provide structured information about potential defects.

This project is being developed incrementally, starting with a reliable **V1 RGB visible-defect detection pipeline** and progressively moving toward a multimodal **RGB + Thermal UAV inspection system**.

## Status

**Project Status: 🚧 Active Development**

This repository documents the ongoing research, development, experiments, model training, evaluation, and deployment work for the system.
