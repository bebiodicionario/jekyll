import os
import subprocess

directory = "/Users/pedrokok/Documents/GitHub/jekyll-arqsite/docs/projects/apartamento-guarapari"
files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

for file in files:
    filepath = os.path.join(directory, file)
    print(f"Processing {file}...")
    try:
        # Convert to sRGB using sips
        # --matchTo profile
        # Profile path: /System/Library/ColorSync/Profiles/sRGB Profile.icc
        subprocess.run([
            "sips", 
            "--matchTo", "/System/Library/ColorSync/Profiles/sRGB Profile.icc", 
            filepath
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing {file}: {e}")
