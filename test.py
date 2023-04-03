from clip_interrogator import Config, Interrogator, LabelTable, load_list
from PIL import Image

ci = Interrogator(Config(blip_model_type=None))
image = Image.open("pipeline_stable_diffusion_hires_fix.png").convert('RGB')
table = LabelTable(load_list('terms.txt'), 'terms', ci)
best_match = table.rank(ci.image_to_features(image), top_count=1)[0]
print(best_match)