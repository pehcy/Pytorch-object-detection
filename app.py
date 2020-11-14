from flask import Flask, render_template, jsonify, request
from werkzeug.utils import secure_filename
import os
from model import transform_image, segmentation

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index(name=None):
  return render_template('index.html', name=name)

@app.route('/segmentation', methods=['POST'])
def detect_obj():
  if request.method == 'POST':
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return render_template('segmentation.html')
    # img_tensor = transform_image(image_bytes=f.read())
    # model = segmentation(2)
    # model.eval(img_tensor)

    #model.segmentation(f.filename)

if __name__ == '__main__':
  app.run()
  app.debug = True
  # port = int(os.environ.get('PORT', 80))
  # app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 80)), debug=True)