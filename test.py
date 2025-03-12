# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:45:32 2023

@author: sanja
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/test' , methods=['GET'])
def test():
    print("rrrr")
    return render_template(r'D:\summer internship\question folder\form.html')
if __name__ == '__main__':
    app.run()