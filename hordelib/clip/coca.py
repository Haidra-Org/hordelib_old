import os
from typing import Union

import open_clip
from PIL import Image


class CoCa:
    def __init__(self, model, transform, device="cuda", half_precision=True):
        self.model = model
        self.transform = transform
        self.device = device
        self.half_precision = half_precision

    def __call__(self, input_image: str | Image.Image):
        if isinstance(input_image, str):
            if not os.path.exists(input_image):
                raise ValueError(f"Image path {input_image} does not exist")
            try:
                input_image = Image.open(input_image)
            except Exception as e:
                raise ValueError(f"Could not open image {input_image}: {e}")

        image = self.transform(input_image).unsqueeze(0).to(self.device)
        if self.half_precision:
            image = image.half()
        generated = self.model.generate(image)

        return open_clip.decode(generated[0]).split("<end_of_text>")[0].replace("<start_of_text>", "")
