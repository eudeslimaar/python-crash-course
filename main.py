import os

# Base directory where your files are located
base_directory = 'solutions'

def create_links(directory):
    links = []
    for root_folder, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root_folder, file)
            # Convert file path to a URL-friendly format
            url_path = file_path.replace(' ', '%20')
            link = f"[{file}]({url_path})"
            links.append(link)
    return links

generated_links = create_links(base_directory)

# Printing the generated links
for link in generated_links:
    print(link)