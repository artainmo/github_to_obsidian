import os
import sys
import base64

def read_file_as_string(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

def file_preface(file, repo):
    if file["path"] != "README.md":
        tags = "#from-github\n\n"
    else:
        formatted_topics = ' '.join(f'#{topic}' for topic in repo["topics"])
        tags = "#from-github " + formatted_topics + "\n\n"
    notice = f"View this page on [github]({file['html_url']}). " +\
            f"Only edit this page on [github]({file['html_url']}).\n\n"
    split = "---\n\n"
    return tags + notice + split

def decode_content(file):
    return base64.b64decode(file["content"]).decode('utf-8')

def code_file(file, repo):
    preface = file_preface(file, repo)
    file_content = decode_content(file)
    return preface + "```\n" + file_content + "```\n"

def markdown_file(file, repo):
    preface = file_preface(file, repo)
    file_content = decode_content(file)
    obsidian_markdown = file_content.replace("<br>", "")
    return preface + obsidian_markdown

def file_content_string(file, repo):
    if file["name"].endswith(".md"):
        return markdown_file(file, repo)
    else:
        return code_file(file, repo)

def path_to_name(repo_name, file_name):
    complete_path = repo_name + "/" + file_name
    transformed = complete_path.replace('/', '~')
    if transformed.startswith('.'):
        transformed = transformed[1:]
    if not transformed.endswith('.md'):
        transformed += '.md'
    return transformed

def create_file(obsidian_path, file, repo):
    content = file_content_string(file, repo)
    file_path = obsidian_path + "/" + path_to_name(repo["name"], file["path"])
    with open(file_path, 'w') as file:
        file.write(content)
        print(f"File '{file_path}' got created or updated.")

def file_changed(obsidian_path, file, repo):
    path = obsidian_path + "/" + path_to_name(repo["name"], file["path"])
    current_content = read_file_as_string(path)
    latest_content = file_content_string(file, repo)
    return current_content != latest_content

def file_exists(obsidian_path, file, repo):
    path = obsidian_path + "/" + path_to_name(repo["name"], file["path"])
    return os.path.exists(path)

def handle_file(obsidian_path, file, repo):
    if file_exists(obsidian_path, file, repo):
        if file_changed(obsidian_path, file, repo):
            create_file(obsidian_path, file, repo)
    else:
        create_file(obsidian_path, file, repo)


