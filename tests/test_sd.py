from torch import autocast
from diffusers import StableDiffusionPipeline


def test_stable_diffusion_bootstrap():
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4", use_auth_token=True
    ).to("cuda")

    prompt = "a photo of an astronaut riding a horse on mars"
    with autocast("cuda"):
        image = pipe(prompt).images[0]

    image.save("images/astronaut_rides_horse.png")
    assert image.width > 64
