from flask import Flask, render_template, url_for, redirect, request, jsonify
from werkzeug.utils import secure_filename
import os, shutil
import torch

UPLOAD_FOLDER = 'static/user_images'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = torch.hub.load("ultralytics/yolov5", "custom", path='best.pt', force_reload=False)
sel_img = ""


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/demo/sample_img/<img_fName>')
def upload_sample(img_fName):
    global sel_img;  sel_img = img_fName
    print("sel img: " + sel_img)

    return render_template('demo2.html', sample_link=sel_img, img_uploaded=False)


@app.route('/demo')
def demo():

    shutil.rmtree("static/detections") 
    os.mkdir("static/detections")
    sel_img = ""
    return render_template('demo2.html', sample_link=sel_img, img_uploaded=False)


def get_fPath(f):
    base = (os.path.splitext(f.filename)[0]).replace(" ", "")
    f.filename = base + ".jpg"
    fpath = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(f.filename))  
    f.save(fpath);  print("Saving upload img to " + f.filename)

    return fpath, base
    

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    global sel_img     
    f = request.files['file']
    fpath = "";  base = ""

    if not f and len(sel_img) == 0:
        return render_template('demo2.html', sample_link="", 
        img_uploaded=False)

    if not f and len(sel_img) != 0:  #detect selected img
        fpath = "static/sample_imgs/" + sel_img
        base = sel_img.split('.')[0].replace(" ", "")

    else:  #f uploaded
        fpath, base = get_fPath(f)
        sel_img = ""


    print("fpath: " + fpath + ", base: " + base)    
    results = model(fpath)
    results.save(save_dir="static/detections/" + base)  #always creates new "dirX"

    detections = results.pandas().xyxy[0] 
    print("Detections: ");  print(detections)

    confidences = list(detections['confidence'])
    format_confidences = []

    for percent in confidences:
        format_confidences.append(str(round(percent*100)) + '%')

    labels = list(detections['name'])
    print("Detection labels: " + str(labels))
    print("Confidences: " + str(confidences))


    #render 
    if f: img_path = base + "/" + f.filename  
    else: img_path = base + "/" + sel_img
    print("img_path: " + img_path)

    if confidences == []:
        return render_template('demo2.html', sample_link=sel_img, img_uploaded=True, user_image=img_path, 
        det_info="No abnormalities detected")
    else:
        det_info = "Confidence that " + labels[0] + " is detected: " + format_confidences[0]
        return render_template('demo2.html', sample_link=sel_img, img_uploaded=True, user_image=img_path,
        det_info=det_info)   


if __name__ == "__main__":
    app.run(port=5000, debug=True)