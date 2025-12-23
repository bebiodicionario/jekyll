
import os
import re

base_dir = 'docs/projects'
projects = {
    'casa-fazenda-bocaina': ['PAISAGEM'],
    'casa-em-cunha': ['FORMA'],
    'casas-modulares-piracaia': ['ESTRUTURA'],
    'casa-af': ['ESTRUTURA'],
    'casa-ml': ['FORMA'],
    'casa-quinta': ['PAISAGEM'],
    'apartamento-guarapari': ['FORMA'],
    'cinema-da-praca': ['PAISAGEM']
}

for project_dir, tags in projects.items():
    md_path = os.path.join(base_dir, project_dir, 'index.md')
    if os.path.exists(md_path):
        with open(md_path, 'r') as f:
            content = f.read()
        
        # Check if tags already exist
        if 'tipo:' not in content:
            # Insert after layout: project
            tag_str = '[' + ', '.join(tags) + ']'
            new_line = f'tipo: {tag_str}\n'
             # Insert after the first --- line (ignoring the very first line of file)
            parts = content.split('---\n', 2)
            if len(parts) >= 3:
                 # parts[0] is empty (before first ---), parts[1] is front matter, parts[2] is body
                 front_matter = parts[1]
                 new_front_matter = front_matter + new_line
                 new_content = '---\n' + new_front_matter + '---\n' + parts[2]
                 
                 with open(md_path, 'w') as f:
                     f.write(new_content)
                 print(f"Updated {project_dir} with {tags}")
            else:
                 print(f"Skipping {project_dir}: weird front matter")
        else:
            print(f"Skipping {project_dir}: tags already exist")
    else:
        print(f"Not found: {md_path}")
