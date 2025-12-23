import os
import urllib.request
import ssl

# List of 25 URLs extracted from ArchDaily
image_urls = [
  "https://images.adsttc.com/media/images/65c2/99de/f2f1/3e07/5fcf/6593/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_15.jpg?1707252203",
  "https://images.adsttc.com/media/images/65c2/99eb/f2f1/3e07/5fcf/659b/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_8.jpg?1707252215",
  "https://images.adsttc.com/media/images/65c2/99e7/f2f1/3e07/5fcf/6598/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_18.jpg?1707252211",
  "https://images.adsttc.com/media/images/65c2/99ef/f2f1/3e0b/443b/ebe2/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_6.jpg?1707252217",
  "https://images.adsttc.com/media/images/65c2/99d9/f2f1/3e07/5fcf/6590/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_4.jpg?1707252199",
  "https://images.adsttc.com/media/images/65c2/99ef/b451/ce01/7ceb/aee4/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_14.jpg?1707252219",
  "https://images.adsttc.com/media/images/65c2/99d9/f2f1/3e07/5fcf/658f/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_1.jpg?1707252198",
  "https://images.adsttc.com/media/images/65c2/99ec/f2f1/3e07/5fcf/659c/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_13.jpg?1707252216",
  "https://images.adsttc.com/media/images/65c2/99e5/f2f1/3e07/5fcf/6596/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_5.jpg?1707252207",
  "https://images.adsttc.com/media/images/65c2/99ce/f2f1/3e07/5fcf/658c/large_jpg/ad-apartamento-guarapari-arquipelago-e-pianca-arquitetura-corte-contexto-1.jpg?1707252204",
  "https://images.adsttc.com/media/images/65c2/99f8/f2f1/3e07/5fcf/659f/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_2.jpg?1707252227",
  "https://images.adsttc.com/media/images/65c2/99dd/f2f1/3e07/5fcf/6591/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_3.jpg?1707252200",
  "https://images.adsttc.com/media/images/65c2/99f7/f2f1/3e0b/443b/ebe4/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_1.jpg?1707252226",
  "https://images.adsttc.com/media/images/65c2/99e1/b451/ce01/7ceb/aedf/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_10.jpg?1707252205",
  "https://images.adsttc.com/media/images/65c2/99e0/b451/ce01/7ceb/aede/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_12.jpg?1707252204",
  "https://images.adsttc.com/media/images/65c2/99f0/f2f1/3e0b/443b/ebe3/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_16.jpg?1707252219",
  "https://images.adsttc.com/media/images/65c2/99eb/f2f1/3e07/5fcf/659a/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_17.jpg?1707252213",
  "https://images.adsttc.com/media/images/65c2/99dd/f2f1/3e07/5fcf/6592/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_2.jpg?1707252203",
  "https://images.adsttc.com/media/images/65c2/99f8/f2f1/3e07/5fcf/659e/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_5.jpg?1707252228",
  "https://images.adsttc.com/media/images/65c2/99ea/b451/ce01/7ceb/aee3/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_7.jpg?1707252213",
  "https://images.adsttc.com/media/images/65c2/99d8/f2f1/3e07/5fcf/658e/large_jpg/apartamento-guarapari-arquipelago-arquitetos-plus-pianca-arquitetura_9.jpg?1707252195",
  "https://images.adsttc.com/media/images/65c2/99d6/b451/ce01/7ceb/aedd/large_jpg/ad-apartamento-guarapari-arquipelago-e-pianca-arquitetura-planta-existente-4.jpg?1707252194",
  "https://images.adsttc.com/media/images/65c2/99d2/b451/ce01/7ceb/aedc/large_jpg/ad-apartamento-guarapari-arquipelago-e-pianca-arquitetura-planta-demolicao-3.jpg?1707252192",
  "https://images.adsttc.com/media/images/65c2/99d3/f2f1/3e07/5fcf/658d/large_jpg/ad-apartamento-guarapari-arquipelago-e-pianca-arquitetura-planta-leyout-5.jpg?1707252193",
  "https://images.adsttc.com/media/images/65c2/99d0/b451/ce01/7ceb/aedb/large_jpg/ad-apartamento-guarapari-arquipelago-e-pianca-arquitetura-corte-2.jpg?1707252199"
]

target_dir = "/Users/pedrokok/Documents/GitHub/jekyll-arqsite/docs/projects/apartamento-guarapari"
project_name = "apartamento-guarapari"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Create a custom context to avoid certification errors if any
ssl_context = ssl._create_unverified_context()

for i, url in enumerate(image_urls):
    try:
        # Format: 'apartamento-guarapari-01.jpg'
        filename = f"{project_name}-{str(i+1).zfill(2)}.jpg"
        filepath = os.path.join(target_dir, filename)
        
        # Don't use requests, use urllib
        with urllib.request.urlopen(url, context=ssl_context) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
            
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Create cover.jpg from the first image
cover_path = os.path.join(target_dir, "cover.jpg")
first_image_path = os.path.join(target_dir, f"{project_name}-01.jpg")

if os.path.exists(first_image_path):
    import shutil
    shutil.copy(first_image_path, cover_path)
    print("Created cover.jpg from 01.jpg")
