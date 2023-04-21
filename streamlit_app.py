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
        

    slide = slideio.open_slide(os.path.join(pathtempDir,uploaded_file.name),"SVS")
   
    num_scenes = slide.num_scenes
    scene = slide.get_scene(0)   


    st.write(num_scenes, scene.name, scene.rect, scene.num_channels)


    """ A code snippet bellow. retrieves the whole image and scales it to 500 pixels width picture """
    myimage = scene.read_block(size=(500,0))

    st.image(myimage, caption='Image uploaded')


   


