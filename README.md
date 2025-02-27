# YOLO-Medical-Anomaly-Scanner
A website that lets you test a YoloV5 model that detects brain tumours, hemorrhages, and scoliosis in brain CT scans and spinal X-rays


# Model performance
mAP: 77.5%
Precision: 84%
Recall: 76.9%


# Run
1. Setup

Activate virtual environment by running

Windows terminal:
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> .venv\Scripts\activate

Mac terminal:
> source .venv/bin/activate

Install packages:
pip install -r requirements.txt


2. Run:
> python app.py

- Visit website URL