<h2>Fovea-crop</h2>

<p>fovea-crop is a simple Python script that locates and crops the fovea from a laser image of the eye. The aim of this script is to automate the process of cropping the fovea manually for further analysis. The SimpleCV library is used, however no machine learning or trained neural networks are used to locate the fovea. The simpler approach considering the images are taken from lasers was to binarise the image with a relatively high white threshold to first locate the optic disc, and then crop the image again to get the fovea.</p>

<h3>Installation</h3>
<p>The requirements.txt file contains the Python requirements for the script, all of which can be installed through pip. Install the requirements: <code>pip install -r requirements.txt</code></p>

<p><b>Note: OpenCV is a requirement of the SimpleCV libary and must be installed for this script to work.</b></p>
