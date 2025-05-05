import os

class Assets:
    def __init__(self):
        self.asset_folder = os.path.join(os.getcwd(), "assets")
        self.blank_image_path = os.path.join(self.asset_folder, "blank.jpg")
        self.goat_image_path = os.path.join(self.asset_folder, "goat.jpg")
        self.tiger_image_path = os.path.join(self.asset_folder, "tiger.jpg")
        self.configuration_path = os.path.join(self.asset_folder, "config.ini")  # Optional
