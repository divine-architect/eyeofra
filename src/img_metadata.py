from PIL import Image

def meta(image_path):
    with Image.open(image_path) as img:
      
        metadata = img.info
        print(f"metadata {metadata}")
        print(f"size {img.size}")  
        print(f"format {img.format}")
        with open('metada.txt','w') as f:
            f.write(str(metadata))


meta("england-london-bridge.jpg")
