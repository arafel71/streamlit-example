from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
""" import slideio as sio  """
import os
import tempfile
import io

""" import pyvips """
from PIL import Image


PIL.Image.MAX_IMAGE_PIXELS = 933120000

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
        
    myImage = Image.open(io.BytesIO(bytes_data))

    """ myImage = Image.open(bytes_data) """
    """ myImage = Image.open(io.BytesIO(buffer)) """
    """ image = pyvips.Image.new_from_buffer(bytes_data) """ 

    """with open(os.path.join("tempDir",uploaded_file.name),"wb") as f:   """
    """     f.write(uploaded_file.getbuffer())                            """

    """ st.success("Saved File")     """

    """ slide = sio.open_slidei(file_path=os.path.join("tempDir",uploaded_file.name),driver_id="SVS")  """
 
    """ slide = sio.open_slidei(bytes_data,driver_id="SVS")""" 
    """ scene = slide.get_scene(0)   """
    """ block = scene.read_block()   """
    """ st.write(bytes_data) """
    """ st.image(bytes_data, caption='Image uploaded')   """

    st.image(myImage, caption='Image uploaded')


   

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
