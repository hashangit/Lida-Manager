from lida import Manager, TextGenerationConfig , llm  
from dotenv import load_dotenv
import os
import openai
import base64
from PIL import Image
from io import BytesIO
from GoogleSheetsDataLoader import GoogleSheetsDataLoader

class DataLoader:
    def __init__(self):
        self.loader = GoogleSheetsDataLoader()

    def load_data(self):
        return self.loader.load_gadst_df()

class LidaEDA:
    def __init__(self, data):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.data = data
        self.lida = Manager(text_gen = llm("openai")) 
        self.textgen_config = TextGenerationConfig(n=1, temperature=0.5, model="gpt-3.5-turbo-0301", use_cache=True)

    @staticmethod
    def base64_to_image(base64_string):
        byte_data = base64.b64decode(base64_string)
        return Image.open(BytesIO(byte_data))

    @staticmethod
    def save_image(base64_str, filename):
        img = LidaEDA.base64_to_image(base64_str)
        img.save(f"{filename}.png")
        print(f"Image saved as {filename}.png")

    def process_data(self):
        images = []  # List to store the images
        summary = self.lida.summarize(self.data, summary_method="default", textgen_config=self.textgen_config)
        goals = self.lida.goals(summary, n=5, textgen_config=self.textgen_config, persona='digital marketing manager with data analytics background')
        for i, goal in enumerate(goals):
            library = "seaborn"
            textgen_config = TextGenerationConfig(n=5, temperature=0.2, use_cache=True)
            charts = self.lida.visualize(summary=summary, goal=goal, textgen_config=textgen_config, library=library)  
            if charts:
                image_base64 = charts[0].raster
                img = LidaEDA.base64_to_image(image_base64)
                images.append(img)
            else:
                print(f"No charts generated for goal {i}")
        return images

class LidaChat:
    def __init__(self, data):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.data = data
        self.lida = Manager(text_gen = llm("openai")) 
        self.textgen_config = TextGenerationConfig(n=1, temperature=0.5, model="gpt-3.5-turbo-0301", use_cache=True)

    @staticmethod
    def base64_to_image(base64_string):
        byte_data = base64.b64decode(base64_string)
        return Image.open(BytesIO(byte_data))

    def process_query(self, user_query):
        summary = self.lida.summarize(self.data, summary_method="default", textgen_config=self.textgen_config)
        charts = self.lida.visualize(summary=summary, goal=user_query, textgen_config=self.textgen_config)  
        if charts:
            image_base64 = charts[0].raster
            img = self.base64_to_image(image_base64)
            return img
        else:
            print("No charts generated for the given query.")
            return None



