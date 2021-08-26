
from fastapi import FastAPI
from omr import omr_image, omr_folder


p = "/Users/huan/Desktop/projects/music/Mozart/testcases/02.PNG"
# omr_folder("/Users/huan/Desktop/projects/music/omr/testcases","/Users/huan/Desktop/projects/music/omr/output/txt")

app =FastAPI()

# @app.get("/omr/image/{image_path}")
# def omr_single_path(image_path:str):
#     res = omr_image(image_path)
#     return {'omr_result':res}

@app.get("/omr/image")
def omr_single_path():
    res = omr_image(p)
    return {'omr_result':res}