# make_index.py
# This isn't a test.
# It's a 30 second hack to create an index.html that shows all our tests results.
import os
import glob


TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Page Title Here</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto&display=swap">
  <style>
    body {
        background-color: #333;
        color: #fff;
    }
    a {
        color: #fff;
        text-decoration: none;
    }
    .gallery {
        display: flex;
        flex-wrap: wrap;
        /*gap: 10px;*/
    }
    h1 {
        font-family: 'Roboto', sans-serif;
        font-size: 24px;
        text-align: left;
        margin-bottom: 20px;
    }
    .thumbnail {
        max-width: 160px;
        cursor: pointer;
    }
    figure {
        max-width: 160px;
        text-align: center;
        margin: 0 5px;
    }
    figcaption {
        font-family: 'Roboto', sans-serif;
        font-size: 12px;
        color: #fff;
        word-wrap: break-word; /* Force text to wrap onto multiple lines */
    }
  </style>
</head>
<body>
  <h1>Latest Build Results</h1>
  <div class="gallery">
    [images]
  </div>
</body>
</html>

"""


def href(filename):
    return f'<a href="{filename}"><figure><img class="thumbnail" src="{filename}"><figcaption>{filename.replace("_", " ")}</figcaption></figure></a>'


def create_index():
    # Get a list of images
    files = glob.glob("images/*.webp")
    refs = []
    for imagefile in files:
        filename = os.path.basename(imagefile)
        refs.append(href(filename))
    indexhtml = TEMPLATE.replace("[images]", "".join(refs))
    with open("images/index.html", "wt") as outfile:
        outfile.write(indexhtml)


if __name__ == "__main__":
    create_index()
