#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import json
from flask import Flask, request
from code1 import anagram
app = Flask(__name__)
app.config["DEBUG"] = True
@app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method == "POST":
        word= request.form["word1"]
        result1= json.dumps(anagram(word))
        return '''
            <html>
                 <body>
                    <br/>
		    <center><font size="5">The result is {result}</font></center>
                    <br/>
		    <center><a href="/"><font size="5">Click here to find again</font></a></center>
                </body>
            </html>
        '''.format(result=result1)
    return '''
        <html>
        <head>
        <style>
        p.big {
        line-height: 1.8;
        }
        </style>
        </head>
            <body>
             <p class="big">
		<h1 style ="font-family: verdana;"><center>This page will accept a single word and show all possible anagrams.</center></h1>                
		<center><font size="6">Enter word:</font></center>
                <br/>
                <form method="post" action=".">
                    <center><input name="word1" size="50"/></center>
		    <br/>
                    <center><input type="submit" value="Find Anagrams" style = "font-size:20px; height:40px; width:150px"/></center>
                </form>
             </p>
            </body>
        </html>
    '''
