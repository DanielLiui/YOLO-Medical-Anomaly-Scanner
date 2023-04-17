/*
Medical Anomaly Scanner
=====
- A website that uses YoloV5 to detect brain tumours, hemorrhages, & scoliosis
in brain CT scans & spinal X-rays that the user uploads


Changes
-----
Home page:
1. New look

Demo:
1. Put content blocks over one another so fits mobile webpg & user can resize
their window
2. Omitted some info like the instructions & detection matrix
3. Fixed upload sample image feature
4.              local image feature


Model limitations:
1. Only detects one abnormality even if there are mult (eg. hemorrhage1)
2. Some issues detecting not so obvious / hard to see symptoms (eg. hemorrhage2)


Imgs with incorrect detections:
1. Imgs above
2. Sooliosis1 -> obvious but says no detection

*/