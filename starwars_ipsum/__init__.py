import markdown
import os


PARENT_DIR = os.path.dirname(os.path.dirname(__file__))


def paragraphs():
    paragraphs = []

    filename = os.path.join(PARENT_DIR, 'data', 'a_new_hope.txt')
    with open(filename, 'r') as file_data:
        paragraph = ''
        for line in file_data:
            if line == '\n':
                paragraphs.append(paragraph)
                paragraph = ''
            else:
                paragraph.append(line.replace('\n', ' '))

    return paragraphs


def html():
    html = ''

    filename = os.path.join(PARENT_DIR, 'data', 'a_new_hope.txt')
    with open(filename, 'r') as file_data:
        html = markdown.markdown(file_data.read())

    return html
