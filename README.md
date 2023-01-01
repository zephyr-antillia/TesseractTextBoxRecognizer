# TesseractTextBoxRecognizer
Tesseract Text Box Reconginizer

This a simple command line client to Google Cloud Vision Text Recognizer.<br>

<h2> 
1 Install
</h2>
Please download tesseract-ocr engine <b>tesseract-ocr-w64-setup-5.3.0.20221222.exe</b>
and install it. We use Windows11 OS.<br>
<br>
https://github.com/UB-Mannheim/tesseract/wiki
<br>

<br>
<h2>
2 Install python packages
</h2>
Please clone this repository to your local PC.<br>
We use Python3 venv on Windows11 OS.
<br>
>pip install requirements.txt
</h2>


<h2>
3 Sample Program
</h2>
Please open Windows Powershell console, and run the following command in the console window.<br>

> python TesseractTextBoxRecognizer.py

<br>
This TesseractTextBoxRecognizer.py script reads the recognition.conf file.<br>
<pre>
[parameter]
images_dir = "./samples"
output_dir = "./outputs"
image_format= ".png"

language_hints   = "ja"

[preprocessor]
preprocessing    = True
gray_image       = True
image_scaling    = 3
constrast        = 2
sharpness        = 3

[visualizer]
font_name        = "BIZ-UDMinchoM.ttc"

</pre>

Please note that we specify the language_hints in this config file to be "ja" to recognize Japanese text.<br>
You have to change this language_hints property depending on your text language.<br>

Example 1: 参考・教育漢字を除く常用漢字.png<br>
<img src="./samples/参考・教育漢字を除く常用漢字.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_参考・教育漢字を除く常用漢字.png"
     width="1280" height="auto">
<br>

Example 2: 付録常用漢字の一覧_付表<br>
<img src="./samples/付録常用漢字の一覧_付表.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_付録常用漢字の一覧_付表.png"
     width="1280" height="auto">
<br>


Example 3: 半角カタカナ一覧<br>
<img src="./samples/半角カタカナ一覧.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_半角カタカナ一覧.png"
     width="1280" height="auto">
<br>

Example 4: VSCodeScreenShot<br>
<img src="./samples/VSCodeScreenShot.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_VSCodeScreenShot.png"
     width="1280" height="auto">
<br>

Example 5: Symbols_Kakana<br>
<img src="./samples/Symbols_Kakana.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_Symbols_Kakana.png"
     width="1280" height="auto">
<br>


