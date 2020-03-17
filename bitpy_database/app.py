from flask import Flask, redirect, url_for, request, render_template, jsonify
import os
import cv2
import SIFT_final_copy


app = Flask(__name__)

@app.route('/')
def success():
    return 'hello, flask'

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/api/jsonlisttest')
def jsonlisttest():
    searchimg = cv2.imread('D:/image_test/big_test.jpg', cv2.IMREAD_COLOR)
    findlist_x2 = SIFT_final_copy.histogram(searchimg)
    lst2 = SIFT_final_copy.matching(searchimg, findlist_x2)

    return jsonify(lst2)


if __name__ == '__main__':
    app.run(debug=True)