
from clip_interrogator import Config, Interrogator, LabelTable, load_list
from PIL import Image

ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
image = Image.open("pipeline_stable_diffusion_hires_fix").convert("RGB")
table = LabelTable(load_list("terms.txt"), "terms", ci)
image_features = ci.image_to_features(image)

terms = None
with open("terms.txt") as termsFileHandle:
    terms = termsFileHandle.readlines()
terms = [term.rstrip() for term in terms]


similarities = ci.similarities(image_features=image_features, text_array=terms)
resultTable = zip(terms, similarities)

print(list(resultTable))