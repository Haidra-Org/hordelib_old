import torch
from PIL import Image
from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode


class Caption:
    def __init__(self, model):
        """
        model: The model to use for captioning. This comes from the ModelManager's loaded_models.
        """
        self.model = model

    def __call__(
        self,
        image,
        sample=True,
        num_beams=3,
        max_length=30,
        min_length=10,
        top_p=0.9,
        repetition_penalty=1.0,
    ):
        """
        image: The image to caption. This can be a PIL.Image.Image or a path to an image.
        sample: Whether to sample or not. If False, the model will return the most likely caption.
        num_beams: The number of beams to use. This is only used if sample is False.
        max_length: The maximum length of the caption.
        min_length: The minimum length of the caption.
        top_p: The top p to use. This is only used if sample is True.
        repetition_penalty: The repetition penalty to use. This is only used if sample is True.
        """
        if not isinstance(image, Image.Image):
            image = Image.open(image).convert("RGB")
        else:
            image = image.convert("RGB")
        gpu_image = (
            transforms.Compose(
                [
                    transforms.Resize((512, 512), interpolation=InterpolationMode.BICUBIC),
                    transforms.ToTensor(),
                    transforms.Normalize(
                        mean=[0.48145466, 0.4578275, 0.40821073],
                        std=[0.26862954, 0.26130258, 0.27577711],
                    ),
                ],
            )(image)
            .unsqueeze(0)
            .to(self.model["device"])
        )
        if self.model["half_precision"]:
            # Input must be half precision when using half precision model
            gpu_image = gpu_image.half()
        with torch.no_grad():
            caption = self.model["model"].generate(
                gpu_image,
                sample=sample,
                num_beams=num_beams,
                max_length=max_length,
                min_length=min_length,
                top_p=top_p,
                repetition_penalty=repetition_penalty,
            )[0]
        return caption
