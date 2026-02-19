import base64
##-----------------------------------------------------------##
def logo(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
##-----------------------------------------------------------##

def jarvis_logo():
    img_path = r"img_logo/jarvis_Logo_1.png"
    image = logo(img_path)
    return image
if __name__ == "__main__":
    print(jarvis_logo())      # Optional testing

def dashboard_logo():
    img_path = r"img_logo/dash_logo_1.png"
    image = logo(img_path)
    return image
if __name__ == "__main__":
    print(dashboard_logo())


def state_map_logo(map:str):
    img_path = rf"img_logo/{map}"    
    image = logo(img_path)
    return image
if __name__ == "__main__":
    print(state_map_logo())      
