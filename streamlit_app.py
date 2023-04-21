from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
""" import slideio as sio  """
import os
import tempfile
import io

import slideio


""" import pyvips """

from PIL import Image 
Image.MAX_IMAGE_PIXELS = 1000000000 



directory = os.getcwd()


pathtempDir = os.path.join(directory + r'/tempDir/')

# solve dll hell
"""os.environ['PATH'] = pathOpenslide + ";" + os.environ['PATH']"""



"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
uploaded_file = st.file_uploader("Choose a file")


if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    with open(os.path.join(pathtempDir,uploaded_file.name),"wb") as f:
      f.write(uploaded_file.getbuffer())
        

    """ slide = slideio.open_slidei(file_path=os.path.join(pathtempDir,uploaded_file.name),driver_id="SVS") """
    slide = slideio.open_slide(file_path=os.path.join(pathtempDir,uploaded_file.name),driver_id="SVS")
    scene = slide.get_scene(0)    
    """ myImage = Image.open(io.BytesIO(bytes_data)) """
    """ mySlideWrap = openslide.ImageSlide(myImage)  """


    """print(mySlideWrap.level_count)"""


    st.image(scene, caption='Image uploaded') 


   


