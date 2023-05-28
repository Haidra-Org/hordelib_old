## hordelib Changelog

## [v1.3.9](https://github.com/Haidra-Org/hordelib/compare/v1.3.8...v1.3.9)

29 May 2023

- feat: Add seeking loras by ID and unicode [`4d6bb2d`](https://github.com/Haidra-Org/hordelib/commit/4d6bb2d6f6e3c02982617041e3a73659c1fc9cb0)  (db0)
- fix: avoid crash when resetting adhoc loras [`213a743`](https://github.com/Haidra-Org/hordelib/commit/213a743cd9d1eae8da56b3e12c4f5bb3de64313c)  (db0)

## [v1.3.8](https://github.com/Haidra-Org/hordelib/compare/v1.3.7...v1.3.8)

27 May 2023

- fix: logging error with loading cnet [`#332`](https://github.com/Haidra-Org/hordelib/pull/332) (Jug)

## [v1.3.7](https://github.com/Haidra-Org/hordelib/compare/v1.3.6...v1.3.7)

27 May 2023

- feat: keeping some unused loras as adhoc [`c81f2da`](https://github.com/Haidra-Org/hordelib/commit/c81f2da7ecafb704b99b11e6a5edc96e896e39fc)  (db0)
- chore: re-added copyright notes to nataili ports [`568738d`](https://github.com/Haidra-Org/hordelib/commit/568738d68b63431fbd5db250b003166122f2defd)  (db0)
- feat: More robust tracking of lora downloads [`28ae6a1`](https://github.com/Haidra-Org/hordelib/commit/28ae6a1ecbeabc42ef0f4040008e4c7246a98f7c)  (db0)

## [v1.3.6](https://github.com/Haidra-Org/hordelib/compare/v1.3.5...v1.3.6)

26 May 2023

- tests: Added test for lora model_reference wipe [`eac465d`](https://github.com/Haidra-Org/hordelib/commit/eac465dd9d80f07e5878f749aa8b7a62d541229e)  (db0)
- fix: wipe reference only when valid [`8b11641`](https://github.com/Haidra-Org/hordelib/commit/8b11641de44e4ac71e4f9745c1e7735aa01e736d)  (db0)
- feat: add changelog link to release annoucement [`c577b8a`](https://github.com/Haidra-Org/hordelib/commit/c577b8a1268b01e334e19919412777b6299a9077)  (Jug)

## [v1.3.5](https://github.com/Haidra-Org/hordelib/compare/v1.3.4...v1.3.5)

25 May 2023

- fix: allow all types of downloads to display progress [`#324`](https://github.com/Haidra-Org/hordelib/pull/324) (Jug)
- fix: make index uses .png files [`#321`](https://github.com/Haidra-Org/hordelib/pull/321) (Divided by Zer0)

## [v1.3.4](https://github.com/Haidra-Org/hordelib/compare/v1.3.3...v1.3.4)

25 May 2023

- tests: Compare test images with expected output [`#319`](https://github.com/Haidra-Org/hordelib/pull/319) (Divided by Zer0)
- feat: add support for download progress indicators [`#318`](https://github.com/Haidra-Org/hordelib/pull/318) (Jug)
- ci: set IMAGE_DISTANCE_THRESHOLD [`7a09e1a`](https://github.com/Haidra-Org/hordelib/commit/7a09e1afa8746ee25fc54647f40bb40e55afcf4e)  (db0)
- doc: restore PR unit test image link [`bf00539`](https://github.com/Haidra-Org/hordelib/commit/bf005391d174be84de987b0fa96c697747a424e1)  (Jug)
- doc: remove link to PR image tests which were removed [`c21453e`](https://github.com/Haidra-Org/hordelib/commit/c21453e706a2d5d516046fadca473e0815c94bd4)  (Jug)

## [v1.3.3](https://github.com/Haidra-Org/hordelib/compare/v1.3.2...v1.3.3)

25 May 2023

- fix: make fakescribble controlnet work again [`#314`](https://github.com/Haidra-Org/hordelib/pull/314) (Jug)

## [v1.3.2](https://github.com/Haidra-Org/hordelib/compare/v1.3.1...v1.3.2)

25 May 2023

- fix: hangs and random processing results with multiple threads regression [`#311`](https://github.com/Haidra-Org/hordelib/pull/311) (Jug)
- fix: ensure lora folder exists before starting download [`#309`](https://github.com/Haidra-Org/hordelib/pull/309) (Divided by Zer0)

## [v1.3.1](https://github.com/Haidra-Org/hordelib/compare/v1.3.0...v1.3.1)

24 May 2023

- fix: more robust downloads; resume, retry, don't delete files so hastily.  [`#307`](https://github.com/Haidra-Org/hordelib/pull/307) (Jug)

## [v1.3.0](https://github.com/Haidra-Org/hordelib/compare/v1.2.1...v1.3.0)

24 May 2023

- fix: moved lora downloads outside of init [`#304`](https://github.com/Haidra-Org/hordelib/pull/304) (Divided by Zer0)
- Lora Model Manager [`#302`](https://github.com/Haidra-Org/hordelib/pull/302) (Divided by Zer0)
- fix: fix some tests and update docs for Linux [`#301`](https://github.com/Haidra-Org/hordelib/pull/301) (Jug)
- feat: Added trigger injection to loras [`5080df8`](https://github.com/Haidra-Org/hordelib/commit/5080df8e8a50211f02a47837da279fc83499ace5)  (db0)
- feat: allow searching triggers [`8f4c7d9`](https://github.com/Haidra-Org/hordelib/commit/8f4c7d98659abcdf6f34d29679bd2a7bac45f871)  (db0)
- fix: tweak lora tests and node loader [`b986a98`](https://github.com/Haidra-Org/hordelib/commit/b986a98705a5130c4fe2f8e9576ec88a5952ab94)  (Jug)

## [v1.2.1](https://github.com/Haidra-Org/hordelib/compare/v1.2.0...v1.2.1)

22 May 2023

- fix: remove "No job ran for x seconds" warning [`#298`](https://github.com/Haidra-Org/hordelib/pull/298) (Jug)
- fix: ignore unknown loras, search case insensitively for them [`#297`](https://github.com/Haidra-Org/hordelib/pull/297) (Jug)

## [v1.2.0](https://github.com/Haidra-Org/hordelib/compare/v1.1.2...v1.2.0)

21 May 2023

- fix: unit tests use about 6GB VRAM max now. [`#293`](https://github.com/Haidra-Org/hordelib/pull/293) (Jug)
- feat: refactor for clarity, tweak img2img and inpainting, tidy tests [`#290`](https://github.com/Haidra-Org/hordelib/pull/290) (Jug)
- Add alt pipeline design for img2img with mask [`#279`](https://github.com/Haidra-Org/hordelib/pull/279) (Wolfgang Meyers)

## [v1.1.2](https://github.com/Haidra-Org/hordelib/compare/v1.1.1...v1.1.2)

19 May 2023

## [v1.1.1](https://github.com/Haidra-Org/hordelib/compare/v1.1.0...v1.1.1)

19 May 2023

- fix: minimum version of horde_model_reference [`27c003b`](https://github.com/Haidra-Org/hordelib/commit/27c003b6ba2635b074a6319092a33e787c4026e7)  (tazlin)
- fix: typo in minimum requirement [`b54fc18`](https://github.com/Haidra-Org/hordelib/commit/b54fc180cb19293a22c0485e1fc9e9b6bd6458d4)  (tazlin)

## [v1.1.0](https://github.com/Haidra-Org/hordelib/compare/v1.0.5...v1.1.0)

19 May 2023

- fix: correctly output pipeline json during development [`#284`](https://github.com/Haidra-Org/hordelib/pull/284) (Jug)
- fix: auto fix bad cfg values [`#282`](https://github.com/Haidra-Org/hordelib/pull/282) (Jug)
- feat: add lora support and reduce cnet memory requirements by 50% [`#270`](https://github.com/Haidra-Org/hordelib/pull/270) (Jug)

## [v1.0.5](https://github.com/Haidra-Org/hordelib/compare/v1.0.4...v1.0.5)

19 May 2023

- refactor: get_mm_pointers accommodates `type` as well [`1007d69`](https://github.com/Haidra-Org/hordelib/commit/1007d69c5f70bebc2f47f1b1fb41bb24e3282fc5)  (tazlin)
- fix: unsupport 'diffusers' [`0c9592d`](https://github.com/Haidra-Org/hordelib/commit/0c9592d6579fe3fb1463ed0e2bbba79736d09462)  (tazlin)
- feat: move stable_diffusion_inpainting if in diffusers directory [`d8ddb01`](https://github.com/Haidra-Org/hordelib/commit/d8ddb01b2ac4f3038098b0e08924aaee0c0b055b)  (tazlin)

## [v1.0.4](https://github.com/Haidra-Org/hordelib/compare/v1.0.3...v1.0.4)

18 May 2023

- Increase read/write sizes during download/checksums [`#274`](https://github.com/Haidra-Org/hordelib/pull/274) (Andy Pilate)
- feat: support prepending proxy URL to github downloads [`653a729`](https://github.com/Haidra-Org/hordelib/commit/653a7296a1da400f04d4262e982537de678d2f12)  (tazlin)
- ci: fix: allow release workflow repo write permissions [`2a8e8d7`](https://github.com/Haidra-Org/hordelib/commit/2a8e8d7356a9310bdb527577a17df386183a8a3e)  (tazlin)

## [v1.0.3](https://github.com/Haidra-Org/hordelib/compare/v1.0.2...v1.0.3)

15 May 2023

- When gathering loaded/available names, allows filtering by model manager type [`#254`](https://github.com/Haidra-Org/hordelib/pull/254) (Divided by Zer0)
- feat: upgrade to the latest comfyui [`#255`](https://github.com/Haidra-Org/hordelib/pull/255) (Jug)
- feat: add option to enable/disable batch optimisation [`#252`](https://github.com/Haidra-Org/hordelib/pull/252) (Jug)
- fix: untrack automatically downloaded model reference jsons [`b7514e1`](https://github.com/Haidra-Org/hordelib/commit/b7514e13d33dd4c4a2c729808798f4cc3aa5b273)  (tazlin)
- fix: remove unused model 'db.json' [`551f9bb`](https://github.com/Haidra-Org/hordelib/commit/551f9bba20e340627ec9ac432a6c6740eeab92d0)  (tazlin)
- fix: ignore automatically downloaded model references [`4a00c71`](https://github.com/Haidra-Org/hordelib/commit/4a00c71b0d7d789e1489d1a3c5ce9a603d1f45ff)  (tazlin)

## [v1.0.2](https://github.com/Haidra-Org/hordelib/compare/v1.0.1...v1.0.2)

14 May 2023

- fix: correctly unload models from gpu under stress [`#249`](https://github.com/Haidra-Org/hordelib/pull/249) (Jug)

## [v1.0.1](https://github.com/Haidra-Org/hordelib/compare/v1.0.0...v1.0.1)

14 May 2023

- fix: benchmark looks harder for model directory [`#247`](https://github.com/Haidra-Org/hordelib/pull/247) (Jug)
- doc: remove changelog from main [`2319a32`](https://github.com/Haidra-Org/hordelib/commit/2319a32e4336f9e59ef58ab88544d6a37b58436c)  (Jug)
- doc: update readme [`532c7a3`](https://github.com/Haidra-Org/hordelib/commit/532c7a3c1493885bd66a247a3adeab826261b735)  (Jug)
- doc: update readme [`2b7cd76`](https://github.com/Haidra-Org/hordelib/commit/2b7cd76bc9a41a695baf44e357bade964361c307)  (Jug)

# [v1.0.0](https://github.com/Haidra-Org/hordelib/compare/v0.19.15...v1.0.0)

14 May 2023

- feat: release v1.0.0 [`#246`](https://github.com/Haidra-Org/hordelib/pull/246) (Jug)

## [v0.19.15](https://github.com/Haidra-Org/hordelib/compare/v0.19.14...v0.19.15)

14 May 2023

- chore: prep for v1.0.0 [`#245`](https://github.com/Haidra-Org/hordelib/pull/245) (Jug)

## [v0.19.14](https://github.com/Haidra-Org/hordelib/compare/v0.19.13...v0.19.14)

14 May 2023

- fix: better memory management [`#239`](https://github.com/Haidra-Org/hordelib/pull/239) (Jug)
- fix: remove some pointless dependencies like libcario [`#240`](https://github.com/Haidra-Org/hordelib/pull/240) (Jug)
- Revert "fix: pin timm version to 0.6.13" [`407bee9`](https://github.com/Haidra-Org/hordelib/commit/407bee9deb997147c8b78a30f04df5171e28aa7b)  (Jug)
- feat: adds code to generate all models test page [`6c8d882`](https://github.com/Haidra-Org/hordelib/commit/6c8d88253f820ae03e19a80492554905f90bb5ed)  (Jug)
- doc: update readme with all models link [`f34bcce`](https://github.com/Haidra-Org/hordelib/commit/f34bcce43c4cd1b8de7125c5f435f333f3ec227e)  (Jug)

## [v0.19.13](https://github.com/Haidra-Org/hordelib/compare/v0.19.12...v0.19.13)

13 May 2023

- fix: better memory management [`#243`](https://github.com/Haidra-Org/hordelib/pull/243) (Jug)

## [v0.19.12](https://github.com/Haidra-Org/hordelib/compare/v0.19.11...v0.19.12)

13 May 2023

- fix: remove some pointless dependencies like libcario [`#240`](https://github.com/Haidra-Org/hordelib/pull/240) (Jug)

## [v0.19.11](https://github.com/Haidra-Org/hordelib/compare/v0.19.10...v0.19.11)

13 May 2023

- fix: pin timm library to v0.6.12 [`ae2e8b0`](https://github.com/Haidra-Org/hordelib/commit/ae2e8b0d7764b6e1076c4443a378f5275d1c6066)  (Jug)

## [v0.19.10](https://github.com/Haidra-Org/hordelib/compare/v0.19.9...v0.19.10)

12 May 2023

- fix: check underlying model before warm loading from cache [`#236`](https://github.com/Haidra-Org/hordelib/pull/236) (tazlin)
- test: add sampler tests [`#233`](https://github.com/Haidra-Org/hordelib/pull/233) (Jug)
- feat: build a payload to inference time prediction model [`#231`](https://github.com/Haidra-Org/hordelib/pull/231) (Jug)
- fix: pin timm version to 0.6.13 [`bc4f862`](https://github.com/Haidra-Org/hordelib/commit/bc4f862d0416d2905a660b7492f9229d9ffca5c4)  (Jug)
- test: add 10 step sampler tests [`363cbc2`](https://github.com/Haidra-Org/hordelib/commit/363cbc2ae5ed50c38a87f437c4afd38f6a309f7c)  (Jug)
- fix: fix kudos model validation [`e103518`](https://github.com/Haidra-Org/hordelib/commit/e1035183701a8fb7a3f8c06db45e25fa8f5c41b5)  (Jug)

## [v0.19.9](https://github.com/Haidra-Org/hordelib/compare/v0.19.8...v0.19.9)

8 May 2023

- fix: handle image / mask size mismatch [`#229`](https://github.com/Haidra-Org/hordelib/pull/229) (Jug)

## [v0.19.8](https://github.com/Haidra-Org/hordelib/compare/v0.19.7...v0.19.8)

7 May 2023

- fix: faster startup with many models cached [`#224`](https://github.com/Haidra-Org/hordelib/pull/224) (Jug)
- fix: cuts 25+ seconds from load time [`f1a453c`](https://github.com/Haidra-Org/hordelib/commit/f1a453c3fb1a40863ef79a9456ff2dfe06aeea5e)  (tazlin)
- fix: updates kudos test [`2102588`](https://github.com/Haidra-Org/hordelib/commit/210258860612ffcf623ec2841979a1850904c8b8)  (Jug)
- hack: disable optimizations for n_iter &gt; 1 [`89c4aac`](https://github.com/Haidra-Org/hordelib/commit/89c4aac1a2839336a00a57d8b50eb51f06678c27)  (tazlin)

## [v0.19.7](https://github.com/Haidra-Org/hordelib/compare/v0.19.6...v0.19.7)

3 May 2023

- fix: remove ether real from exclude list [`92b5794`](https://github.com/Haidra-Org/hordelib/commit/92b5794f68947a51b94433f7a3b8fa38bec8745a)  (tazlin)

## [v0.19.6](https://github.com/Haidra-Org/hordelib/compare/v0.19.5...v0.19.6)

3 May 2023

- feat: get model db from legacy model reference repo [`b3dd5a4`](https://github.com/Haidra-Org/hordelib/commit/b3dd5a4ed122170f514e986187cfe10764779fc1)  (tazlin)
- fix: the disaster with linking [`1de6e06`](https://github.com/Haidra-Org/hordelib/commit/1de6e061441ad0b19e29eb1eff29093c9a8847fe)  (tazlin)
- feat: add a model exclusion list to `consts.py` [`b7e8b46`](https://github.com/Haidra-Org/hordelib/commit/b7e8b4682feb5bd8712d11b8369038b22cfe5c24)  (tazlin)

## [v0.19.5](https://github.com/Haidra-Org/hordelib/compare/v0.19.4...v0.19.5)

1 May 2023

- fix: remove Ether Real model due to bad hash [`a671924`](https://github.com/Haidra-Org/hordelib/commit/a671924d00431b507a00ebbe97e3affe24084a38)  (Jug)
- ci: try upgrading pip before tests [`68cbd9d`](https://github.com/Haidra-Org/hordelib/commit/68cbd9df1e8f46741f3e652a38aacdafff199d27)  (Jug)

## [v0.19.4](https://github.com/Haidra-Org/hordelib/compare/v0.19.3...v0.19.4)

1 May 2023

- fix: update to latest model database [`2f037cf`](https://github.com/Haidra-Org/hordelib/commit/2f037cf2bbd64b6cc784bfa8c1b57138b3a29941)  (Jug)
- fix: fix some model download links [`4e6743c`](https://github.com/Haidra-Org/hordelib/commit/4e6743c57d5026ef7f9b7d94b32f950fd4b6ad0c)  (Jug)
- ci: change tests to abort after first failure [`d80613c`](https://github.com/Haidra-Org/hordelib/commit/d80613cc35a86d5b299cb70f70607e19785672a3)  (Jug)

## [v0.19.3](https://github.com/Haidra-Org/hordelib/compare/v0.19.2...v0.19.3)

1 May 2023

- ci: update some bits of the release ci [`1add1db`](https://github.com/Haidra-Org/hordelib/commit/1add1db011ed43d23cda10ac46709a2c7cf83fda)  (Jug)

## [v0.19.2](https://github.com/Haidra-Org/hordelib/compare/v0.19.1...v0.19.2)

1 May 2023

## [v0.19.1](https://github.com/Haidra-Org/hordelib/compare/v0.19.0...v0.19.1)

1 May 2023

- docs: update readme [`646a419`](https://github.com/Haidra-Org/hordelib/commit/646a419bef63c48bfb970efbd25781bd748c8b8e)  (Jug)

## [v0.19.0](https://github.com/Haidra-Org/hordelib/compare/v0.18.0...v0.19.0)

1 May 2023

## [v0.18.0](https://github.com/Haidra-Org/hordelib/compare/v0.17.0...v0.18.0)

1 May 2023

- feat: use less vram with large images (tiled vae decode) [`#207`](https://github.com/Haidra-Org/hordelib/pull/207) (Jug)
- fix: suppress some clip debug [`9849955`](https://github.com/Haidra-Org/hordelib/commit/98499553b367bb8c9fad3ab2c66a1d557cbb539b)  (Jug)

## [v0.17.0](https://github.com/Haidra-Org/hordelib/compare/v0.16.4...v0.17.0)

1 May 2023

- feat: minor performance tweaking [`#205`](https://github.com/Haidra-Org/hordelib/pull/205) (Jug)
- feat: update model database [`a80846e`](https://github.com/Haidra-Org/hordelib/commit/a80846e2f7b791f496bd3042e968b8b67ddbb7bf)  (Jug)
- fix: adds ersgan upscaler, SHA check now case insensitive [`1d82e30`](https://github.com/Haidra-Org/hordelib/commit/1d82e30aac4ce3207a034b184e7a7406b3206962)  (tazlin)
- docs: update readme [`26c3b62`](https://github.com/Haidra-Org/hordelib/commit/26c3b6268e5f8041a193a9967605d0843cee6884)  (Jug)

## [v0.16.4](https://github.com/Haidra-Org/hordelib/compare/v0.16.3...v0.16.4)

30 April 2023

- fix: support the latest model database format [`a986d06`](https://github.com/Haidra-Org/hordelib/commit/a986d0699edf3d299a0c8b9b8b75382fcebb1e39)  (Jug)

## [v0.16.3](https://github.com/Haidra-Org/hordelib/compare/v0.16.2...v0.16.3)

29 April 2023

- style: stable_diffusion.json whitespace [`d5dbd95`](https://github.com/Haidra-Org/hordelib/commit/d5dbd95ff1267ddb47c633ef13e0bece8a5044c3)  (tazlin)
- fix: update civitai links out of date, adds two safetensors [`70a675e`](https://github.com/Haidra-Org/hordelib/commit/70a675e8d7cc5a930664d2b94be3d97b6b995246)  (tazlin)
- fix: don't allow dynamic prompts to interfere with the random seed. [`5643490`](https://github.com/Haidra-Org/hordelib/commit/5643490d8fea6070074232b6623ef6c6f98b21e5)  (Jug)

## [v0.16.2](https://github.com/Haidra-Org/hordelib/compare/v0.16.1...v0.16.2)

29 April 2023

- fix: ensure we manage ram when loading models from cache [`516f001`](https://github.com/Haidra-Org/hordelib/commit/516f001383f27c9d2e9b56dff42164213a8d0b96)  (Jug)

## [v0.16.1](https://github.com/Haidra-Org/hordelib/compare/v0.16.0...v0.16.1)

29 April 2023

- fix: disk cache model load optimisation [`#198`](https://github.com/Haidra-Org/hordelib/pull/198) (Jug)

## [v0.16.0](https://github.com/Haidra-Org/hordelib/compare/v0.15.3...v0.16.0)

29 April 2023

- feat: automatic resource management [`#186`](https://github.com/Haidra-Org/hordelib/pull/186) (Jug)

## [v0.15.3](https://github.com/Haidra-Org/hordelib/compare/v0.15.2...v0.15.3)

29 April 2023

- fix: removed extraoneous clip debug messages [`#194`](https://github.com/Haidra-Org/hordelib/pull/194) (Divided by Zer0)
- feat: add torch and xformers versions to benchmark [`559f198`](https://github.com/Haidra-Org/hordelib/commit/559f1989e2ec3b42c95ee0e2947bf248f01a92f5)  (Jug)
- fix: exclude `build/` folder from linting [`5f38c3f`](https://github.com/Haidra-Org/hordelib/commit/5f38c3feecacb7e6a12af598b4a42bee8c00f43a)  (tazlin)

## [v0.15.2](https://github.com/Haidra-Org/hordelib/compare/v0.15.1...v0.15.2)

29 April 2023

- fix: validate denoising parameter bounds [`df1a369`](https://github.com/Haidra-Org/hordelib/commit/df1a369b612e7e960844ed5da7aee54fce42895e)  (Jug)
- fix: facefix didn't work on dev versions of torch [`7cc212b`](https://github.com/Haidra-Org/hordelib/commit/7cc212b4fb7bc174307e2d8de960042628d06cef)  (Jug)
- build: bump to xformers 0.0.19 [`1c0eb4a`](https://github.com/Haidra-Org/hordelib/commit/1c0eb4a094a5f88c2bcc3e61155141d743fdf92d)  (Jug)

## [v0.15.1](https://github.com/Haidra-Org/hordelib/compare/v0.15.0...v0.15.1)

27 April 2023

- fix: disable controlnet on low vram gpus in benchmark [`#191`](https://github.com/Haidra-Org/hordelib/pull/191) (Jug)
- fix: rectify txt2img highres denoising [`fd20e69`](https://github.com/Haidra-Org/hordelib/commit/fd20e691af566048df3032d42485dbc374101e51)  (Jug)

## [v0.15.0](https://github.com/Haidra-Org/hordelib/compare/v0.14.2...v0.15.0)

27 April 2023

- fix: remove unused file [`410923c`](https://github.com/Haidra-Org/hordelib/commit/410923cfb6880321c6532a7049a7f90aaefd95f4)  (Jug)
- tests: new test for cuda [`4288273`](https://github.com/Haidra-Org/hordelib/commit/4288273590cc7681ced9d104e1b7caa45276c21e)  (db0)
- fix: auto fix if width/height not divisible by 64 [`f89f889`](https://github.com/Haidra-Org/hordelib/commit/f89f889122bf3656c9c3706146863118c60bff9a)  (Jug)

## [v0.14.2](https://github.com/Haidra-Org/hordelib/compare/v0.14.1...v0.14.2)

27 April 2023

- fix: image sizing bugs with hires fix and controlnet [`ad0d6a9`](https://github.com/Haidra-Org/hordelib/commit/ad0d6a9551c5b3766c4c19bc08b994bf7e3589dc)  (Jug)
- fix: benchmark on linux [`48de047`](https://github.com/Haidra-Org/hordelib/commit/48de0477261b5b7f5c01789658a15b161d7796c2)  (Jug)

## [v0.14.1](https://github.com/Haidra-Org/hordelib/compare/v0.14.0...v0.14.1)

24 April 2023

- fix: use denoising as controlnet strength (compatibility hack) [`#183`](https://github.com/Haidra-Org/hordelib/pull/183) (Jug)

## [v0.14.0](https://github.com/Haidra-Org/hordelib/compare/v0.13.0...v0.14.0)

24 April 2023

- feat: encode prompt pipeline in raw output image metadata [`#181`](https://github.com/Haidra-Org/hordelib/pull/181) (Jug)
- feat: add OS and VRAM to benchmark [`95fa03d`](https://github.com/Haidra-Org/hordelib/commit/95fa03da94f0940248b09743de91a94732a9118a)  (Jug)
- fix: lint fixes [`c87f3b0`](https://github.com/Haidra-Org/hordelib/commit/c87f3b02ada9c7ee927636c1ebd1485c48891279)  (Jug)

## [v0.13.0](https://github.com/Haidra-Org/hordelib/compare/v0.12.1...v0.13.0)

24 April 2023

- feat: adds a hordelib benchmark test [`#179`](https://github.com/Haidra-Org/hordelib/pull/179) (Jug)

## [v0.12.1](https://github.com/Haidra-Org/hordelib/compare/v0.12.0...v0.12.1)

24 April 2023

- fix: unload local models correctly [`d75ffb9`](https://github.com/Haidra-Org/hordelib/commit/d75ffb91985025a71cb5960d260df178f3dfd269)  (Jug)
- fix: Clearer logging message for annotator check/download [`131d07f`](https://github.com/Haidra-Org/hordelib/commit/131d07fcc5142c28caaf451a440cd5d336ba1e3e)  (tazlin)
- fix: pidinet annotator being downloaded to wrong location [`8b40b16`](https://github.com/Haidra-Org/hordelib/commit/8b40b169a5a69c1cbc01f3eca201eb959918c096)  (tazlin)

## [v0.12.0](https://github.com/Haidra-Org/hordelib/compare/v0.11.1...v0.12.0)

24 April 2023

- fix: model loaded/unloading stress test fixes [`#175`](https://github.com/Haidra-Org/hordelib/pull/175) (Jug)
- feat: add support for controlnet hires fix [`#173`](https://github.com/Haidra-Org/hordelib/pull/173) (Jug)
- fix: implicitly load local models [`#174`](https://github.com/Haidra-Org/hordelib/pull/174) (Jug)

## [v0.11.1](https://github.com/Haidra-Org/hordelib/compare/v0.11.0...v0.11.1)

23 April 2023

- fix: parameter handling improvements [`#170`](https://github.com/Haidra-Org/hordelib/pull/170) (Jug)

## [v0.11.0](https://github.com/Haidra-Org/hordelib/compare/v0.10.1...v0.11.0)

23 April 2023

- feat: add control_strength parameter for cnet strength [`#167`](https://github.com/Haidra-Org/hordelib/pull/167) (Jug)
- feat: add support for local models including safetensors [`#166`](https://github.com/Haidra-Org/hordelib/pull/166) (Jug)
- feat: upgrade to latest comfyui backend [`#165`](https://github.com/Haidra-Org/hordelib/pull/165) (Jug)

## [v0.10.1](https://github.com/Haidra-Org/hordelib/compare/v0.10.0...v0.10.1)

22 April 2023

- fix: img2img passes 5 thread stress test [`#163`](https://github.com/Haidra-Org/hordelib/pull/163) (Jug)
- fix: unknown samplers and cnets changed to warnings [`c98c74b`](https://github.com/Haidra-Org/hordelib/commit/c98c74ba497555770b8a685bd8fbc356216fce90)  (Jug)

## [v0.10.0](https://github.com/Haidra-Org/hordelib/compare/v0.9.5...v0.10.0)

22 April 2023

- feat: add dynamic prompt support [`#161`](https://github.com/Haidra-Org/hordelib/pull/161) (Jug)
- fix: stability fixes [`#159`](https://github.com/Haidra-Org/hordelib/pull/159) (Jug)
- fix: Moves ControlNet Annotators to `AIWORKER_CACHE_HOME` [`e0a7db7`](https://github.com/Haidra-Org/hordelib/commit/e0a7db7e89dc91016dd5abba2e94ccf3767c65d3)  (tazlin)
- refactor: cleans up the preload annotators functions [`6b8f9c4`](https://github.com/Haidra-Org/hordelib/commit/6b8f9c453ef38af3439a6bf6ca2b99de649fc6c6)  (tazlin)
- feat: Preload controlnet annotators [`6d16515`](https://github.com/Haidra-Org/hordelib/commit/6d1651535915022cac8e7d218ca4d5081d1d2241)  (tazlin)

## [v0.9.5](https://github.com/Haidra-Org/hordelib/compare/v0.9.4...v0.9.5)

20 April 2023

- build: fix missing dependency in pypi build [`01169be`](https://github.com/Haidra-Org/hordelib/commit/01169beb575c0a0577eebc00210ca98d14eeff42)  (Jug)

## [v0.9.4](https://github.com/Haidra-Org/hordelib/compare/v0.9.3...v0.9.4)

20 April 2023

- fix: add missing dependency [`1dc5127`](https://github.com/Haidra-Org/hordelib/commit/1dc51270a15981aa6eb08aafe2ae8fba7a1e7d57)  (Jug)

## [v0.9.3](https://github.com/Haidra-Org/hordelib/compare/v0.9.2...v0.9.3)

20 April 2023

- CI: trigger CI with certain other critical files [`#152`](https://github.com/Haidra-Org/hordelib/pull/152) (tazlin)
- fix: stability fixes [`#150`](https://github.com/Haidra-Org/hordelib/pull/150) (Jug)
- fix: Tox lint/style environments now build (more) correctly [`#151`](https://github.com/Haidra-Org/hordelib/pull/151) (tazlin)
- Revert "Merge branch 'releases' into main" [`27987a0`](https://github.com/Haidra-Org/hordelib/commit/27987a0884b0ce48cad9d458c9fbdfa9b423b4a2)  (Jug)
- refactor: Housekeeping, preparing for full lint ruleset in CI [`06155d2`](https://github.com/Haidra-Org/hordelib/commit/06155d26eb0b81ba704466adfefe34fd7347e42f)  (tazlin)
- refactor: Control net model manager housekeeping [`37b6cac`](https://github.com/Haidra-Org/hordelib/commit/37b6cac2c1ebf79479996aecec1c4414d9c8b243)  (tazlin)

## [v0.9.2](https://github.com/Haidra-Org/hordelib/compare/v0.9.1...v0.9.2)

17 April 2023

- fix: don't mix up controlnets and run out of vram [`#147`](https://github.com/Haidra-Org/hordelib/pull/147) (Jug)

## [v0.9.1](https://github.com/Haidra-Org/hordelib/compare/v0.9.0...v0.9.1)

17 April 2023

- fix: add proper exception logging to comfyui, closes #64 [`#64`](https://github.com/Haidra-Org/hordelib/issues/64)  ()

## [v0.9.0](https://github.com/Haidra-Org/hordelib/compare/v0.8.8...v0.9.0)

16 April 2023

- feat: active memory and model management [`#144`](https://github.com/Haidra-Org/hordelib/pull/144) (Jug)

## [v0.8.8](https://github.com/Haidra-Org/hordelib/compare/v0.8.7...v0.8.8)

15 April 2023

- fix: Make thread locking as minimalist as possible [`#142`](https://github.com/Haidra-Org/hordelib/pull/142) (Jug)
- fix: fix broken stress test [`be9567e`](https://github.com/Haidra-Org/hordelib/commit/be9567e8935f6016a607ad7de58522d2d84b21f7)  (Jug)

## [v0.8.7](https://github.com/Haidra-Org/hordelib/compare/v0.8.6...v0.8.7)

15 April 2023

- fix: don't thread lock loading with inference [`00ec98d`](https://github.com/Haidra-Org/hordelib/commit/00ec98dc8c80c14208f38c58bc7673ad03d7ab4b)  (Jug)
- chore: more badge refresh tweaks [`4a54868`](https://github.com/Haidra-Org/hordelib/commit/4a54868cb05b5ac8c45e6646ff04565c28732df2)  (Jug)

## [v0.8.6](https://github.com/Haidra-Org/hordelib/compare/v0.8.5...v0.8.6)

15 April 2023

- fix: Sha validation fix [`#139`](https://github.com/Haidra-Org/hordelib/pull/139) (tazlin)
- fix: pytest discovery, broken by non-tests in test folder [`534695e`](https://github.com/Haidra-Org/hordelib/commit/534695e10e5f6a94571059a6916d9798867860fa)  (tazlin)
- fix: switches pr CI to use example/ run_* [`e6ba23e`](https://github.com/Haidra-Org/hordelib/commit/e6ba23e62bc44eaebe0996201baf807a150a389e)  (tazlin)
- build: update CI to do a weak lint/formatting check [`6d09423`](https://github.com/Haidra-Org/hordelib/commit/6d09423e3c8028bc17d0be36f460b9a1963207f1)  (tazlin)

## [v0.8.5](https://github.com/Haidra-Org/hordelib/compare/v0.8.4...v0.8.5)

14 April 2023

- test: add threaded torture test [`03bd56a`](https://github.com/Haidra-Org/hordelib/commit/03bd56a3c40d8ace9dbbb94c0747e207c8442e4a)  (Jug)
- fix: assert parameter bounds to stop errors [`d1a18f7`](https://github.com/Haidra-Org/hordelib/commit/d1a18f7659336614738d9106f7ffccc72c1b9de0)  (Jug)

## [v0.8.4](https://github.com/Haidra-Org/hordelib/compare/v0.8.3...v0.8.4)

14 April 2023

- fix: threading and job settings being mixed together [`#127`](https://github.com/Haidra-Org/hordelib/pull/127) (Jug)
- ci: try to refresh pypi badge on release [`fbb832c`](https://github.com/Haidra-Org/hordelib/commit/fbb832c8cf3906958ed08b6fb0408811130e57ca)  (Jug)
- docs: minor url tweak in readme [`6faee9a`](https://github.com/Haidra-Org/hordelib/commit/6faee9a8757b749013f3809c2617e7a7003310ba)  (Jug)

## [v0.8.3](https://github.com/Haidra-Org/hordelib/compare/v0.8.2...v0.8.3)

13 April 2023

- fix: defer model manager loading [`5c41949`](https://github.com/Haidra-Org/hordelib/commit/5c419490e708fa7fe0778d97b1c53cc5ec7aa63e)  (tazlin)

## [v0.8.2](https://github.com/Haidra-Org/hordelib/compare/v0.8.1...v0.8.2)

13 April 2023

- feat: performance optimisation [`#125`](https://github.com/Haidra-Org/hordelib/pull/125) (Jug)
- refactor: Logger tweaks, Model Manager housekeeping [`#118`](https://github.com/Haidra-Org/hordelib/pull/118) (tazlin)
- docs: Update README.md [`1fea1f1`](https://github.com/Haidra-Org/hordelib/commit/1fea1f1abd9372fb56711b67145f228c5987db07)  (tazlin)
- ci: remove junk from changelog [`f943b8f`](https://github.com/Haidra-Org/hordelib/commit/f943b8f5d3169f37c58f6415f2bb39314706dc12)  (Jug)

## [v0.8.1](https://github.com/Haidra-Org/hordelib/compare/v0.8.0...v0.8.1)

13 April 2023

- fix: suppress terminal spam from comfyui [`07764b5`](https://github.com/Haidra-Org/hordelib/commit/07764b51eb2a78c1557d5acceec265b3a4cd47da)  (Jug)

## [v0.8.0](https://github.com/Haidra-Org/hordelib/compare/v0.7.3...v0.8.0)

13 April 2023

- feat: Clip Rankings [`#117`](https://github.com/Haidra-Org/hordelib/pull/117) (Divided by Zer0)
- feat: Blip [`#116`](https://github.com/Haidra-Org/hordelib/pull/116) (Divided by Zer0)
- fix: make library thread safe [`b7274b4`](https://github.com/Haidra-Org/hordelib/commit/b7274b4dc1170480513fbd7eb34a4e6a0cd3aaf4)  (Jug)
- fix: remove thread mutex for now [`1a901b8`](https://github.com/Haidra-Org/hordelib/commit/1a901b8d8274f84663dd2933224d375105120a1b)  (Jug)
- build: fix build_helper for local use [`6ec5f38`](https://github.com/Haidra-Org/hordelib/commit/6ec5f38279eca2643fbfdf0ff9cc1ab7031b6bb3)  (Jug)

## [v0.7.3](https://github.com/Haidra-Org/hordelib/compare/v0.7.2...v0.7.3)

12 April 2023

- build: more production build fixes. [`0ca0367`](https://github.com/Haidra-Org/hordelib/commit/0ca0367e98ec88f9b30428f797101e333902a0f9)  (Jug)

## [v0.7.2](https://github.com/Haidra-Org/hordelib/compare/v0.7.1...v0.7.2)

12 April 2023

- build: fix production build packaging [`1236763`](https://github.com/Haidra-Org/hordelib/commit/12367632c4248562423c8745fa3534bc19d0c31e)  (Jug)

## [v0.7.1](https://github.com/Haidra-Org/hordelib/compare/v0.7.0...v0.7.1)

12 April 2023

- build: fix missing build time dependency [`de649d4`](https://github.com/Haidra-Org/hordelib/commit/de649d426c79140a85e3f70e60928628061422d5)  (Jug)

## [v0.7.0](https://github.com/Haidra-Org/hordelib/compare/v0.6.1...v0.7.0)

12 April 2023

- build: add support for production builld [`#109`](https://github.com/Haidra-Org/hordelib/pull/109) (Jug)
- build: fix detection of production build [`029bcac`](https://github.com/Haidra-Org/hordelib/commit/029bcac3b1dd86a06fa453db4e804818929d67bd)  (Jug)
- ci: if a label is forgotten on release, assume patch release [`57bdba3`](https://github.com/Haidra-Org/hordelib/commit/57bdba3f99c783bde769e5857762033d64b1acf1)  (Jug)

## [v0.6.1](https://github.com/Haidra-Org/hordelib/compare/v0.6.0...v0.6.1)

12 April 2023

- feat: make logging setup and control optional [`#106`](https://github.com/Haidra-Org/hordelib/pull/106) (Jug)
- style: Automatic formatting/lint with length 119 [`845764a`](https://github.com/Haidra-Org/hordelib/commit/845764ad5765f2b4e7c442a25f421af493fc7c88)  (tazlin)
- docs: cleanup readme for viewing in an editor [`76a7f7f`](https://github.com/Haidra-Org/hordelib/commit/76a7f7f7198da1f988d1972e2b9082944b97af3a)  (Jug)
- chore: Change black to line length 119 [`429aadf`](https://github.com/Haidra-Org/hordelib/commit/429aadff04e48948167173497d134983a9dc26c4)  (tazlin)

## [v0.6.0](https://github.com/Haidra-Org/hordelib/compare/v0.5.24...v0.6.0)

12 April 2023

- fix: suppress terminal spam [`#104`](https://github.com/Haidra-Org/hordelib/pull/104) (Jug)
- feat: add support for separate source_mask [`#103`](https://github.com/Haidra-Org/hordelib/pull/103) (Jug)

## [v0.5.24](https://github.com/Haidra-Org/hordelib/compare/v0.5.23...v0.5.24)

12 April 2023

- ci: include changelog link on pypi page [`a617c23`](https://github.com/Haidra-Org/hordelib/commit/a617c2381a46b9e3b421074dfb5162c3a600c131)  (Jug)

## [v0.5.23](https://github.com/Haidra-Org/hordelib/compare/v0.5.22...v0.5.23)

12 April 2023

- ci: customise the changelog format [`c85285a`](https://github.com/Haidra-Org/hordelib/commit/c85285ab213862d32dde591cbf714e2d2c3dd3ba)  (Jug)

## [v0.5.22](https://github.com/Haidra-Org/hordelib/compare/v0.5.21...v0.5.22)

12 April 2023

## [v0.5.21](https://github.com/Haidra-Org/hordelib/compare/v0.5.20...v0.5.21)

12 April 2023

- ci: try to generate changelog for the right version [`2b86531`](https://github.com/Haidra-Org/hordelib/commit/2b865314cb8f6f387e181a87771739cf983f1fa6)  (Jug)

## [v0.5.20](https://github.com/Haidra-Org/hordelib/compare/v0.5.19...v0.5.20)

12 April 2023

- ci: try a better changelog generator [`a03b5fc`](https://github.com/Haidra-Org/hordelib/commit/a03b5fcd052269451004e4c9f45ef5775f5331d8)  (Jug)
- ci: more tweaks [`81ac9b5`](https://github.com/Haidra-Org/hordelib/commit/81ac9b587fdeacf1159c9a01f7ef9c06a24bcc52)  (Jug)
- ci: ci again [`a185c41`](https://github.com/Haidra-Org/hordelib/commit/a185c410e3cadcd56bd5b2d63712abd2859884e5)  (Jug)

## [v0.5.19](https://github.com/Haidra-Org/hordelib/compare/v0.5.18...v0.5.19)

12 April 2023

- ci: changelog wasn't include in setuptools [`652e53c`](https://github.com/Haidra-Org/hordelib/commit/652e53cf4db43e6e5502edc05b299da3e8f63644)  (Jug)

## [v0.5.18](https://github.com/Haidra-Org/hordelib/compare/v0.5.17...v0.5.18)

11 April 2023

- ci: release ci tweaks [`1adf7ce`](https://github.com/Haidra-Org/hordelib/commit/1adf7ce5d1c607ea04011803324e20b26e348a3c)  (Jug)

## [v0.5.17](https://github.com/Haidra-Org/hordelib/compare/v0.5.16...v0.5.17)

11 April 2023

- style: Incremental style/lint catchup [`1cb70d2`](https://github.com/Haidra-Org/hordelib/commit/1cb70d2eb3c219bff304c4ed0ac34f7456946281)  (tazlin)
- ci: Enables a couple ruff rules for CI [`17bd0f8`](https://github.com/Haidra-Org/hordelib/commit/17bd0f8b1cfd73f3e1429ad4c9b007623517de35)  (tazlin)
- ci: another day another way to do changelogs [`6e7ed60`](https://github.com/Haidra-Org/hordelib/commit/6e7ed604fee66388570b9e953f25599d49a3bc9a)  (Jug)

## [v0.5.16](https://github.com/Haidra-Org/hordelib/compare/v0.5.15...v0.5.16)

11 April 2023

- ci: more ci tweaks [`7bbc0c3`](https://github.com/Haidra-Org/hordelib/commit/7bbc0c3491c12e00ee54fa5f96e73fcf801ae6f7)  (Jug)

## [v0.5.15](https://github.com/Haidra-Org/hordelib/compare/v0.5.14...v0.5.15)

11 April 2023

- ci: this is never going to work is it [`797a317`](https://github.com/Haidra-Org/hordelib/commit/797a3172666e4eab9fe88bc22307e7ee84063441)  (Jug)

## [v0.5.14](https://github.com/Haidra-Org/hordelib/compare/v0.5.13...v0.5.14)

11 April 2023

- ci: another day another ci hack [`bf007ac`](https://github.com/Haidra-Org/hordelib/commit/bf007ace0740eeebf17dd95013d5d68cf332a209)  (Jug)

## [v0.5.13](https://github.com/Haidra-Org/hordelib/compare/v0.5.12...v0.5.13)

11 April 2023

- ci: optimistically try to output a changelog [`cfc71a2`](https://github.com/Haidra-Org/hordelib/commit/cfc71a28468b391e70bd85a8b3b57550f51ec328)  (Jug)

## [v0.5.12](https://github.com/Haidra-Org/hordelib/compare/v0.5.11...v0.5.12)

11 April 2023

- ci: Try harder to generate a changelog [`4eff72d`](https://github.com/Haidra-Org/hordelib/commit/4eff72df9c5ea8c811a4fb09099aa2bc10319fc5)  (Jug)

## [v0.5.11](https://github.com/Haidra-Org/hordelib/compare/v0.5.10...v0.5.11)

11 April 2023

- ci: add some notes to the release ci [`faf9788`](https://github.com/Haidra-Org/hordelib/commit/faf9788de1e284a1d0b4b54b5c36b1a5fc789ff9)  (Jug)
- ci: generate a changelog once again [`8749370`](https://github.com/Haidra-Org/hordelib/commit/8749370ca78a0e5413293f5ca1a9a60859fd5e97)  (Jug)

## [v0.5.10](https://github.com/Haidra-Org/hordelib/compare/v0.5.9...v0.5.10)

11 April 2023

- docs: remove changelog [`62dae03`](https://github.com/Haidra-Org/hordelib/commit/62dae03cd056ee19a7a433a1c360e026266329a7)  (Jug)
- ci: tweak release scripts [`bf9a6a7`](https://github.com/Haidra-Org/hordelib/commit/bf9a6a76a7014e263a3554fefe5c8195c782f6f0)  (Jug)

## [v0.5.9](https://github.com/Haidra-Org/hordelib/compare/v0.5.8...v0.5.9)

11 April 2023

- ci: more tweaks to the ci process [`522d269`](https://github.com/Haidra-Org/hordelib/commit/522d2699385c32b89cbcdf45d89bb6801daaadfb)  (Jug)

## [v0.5.8](https://github.com/Haidra-Org/hordelib/compare/v0.5.7...v0.5.8)

11 April 2023

## [v0.5.7](https://github.com/Haidra-Org/hordelib/compare/v0.5.6...v0.5.7)

11 April 2023

- fix: img2img + highres_fix  [`#80`](https://github.com/Haidra-Org/hordelib/pull/80) (Divided by Zer0)
- ci: try to publish to pypi on release [`deb6eb5`](https://github.com/Haidra-Org/hordelib/commit/deb6eb5f7661be5ebbb91e121c382338a89ecb76)  (Jug)
- ci: tweaks to the release ci [`c234ea7`](https://github.com/Haidra-Org/hordelib/commit/c234ea7157b4c70e62adbc2b71d7220a86e1ec98)  (Jug)

## [v0.5.6](https://github.com/Haidra-Org/hordelib/compare/v0.5.5...v0.5.6)

11 April 2023

- tests: class scope on inference tests for speedup [`#78`](https://github.com/Haidra-Org/hordelib/pull/78) (Divided by Zer0)
- docs: recreate LICENSE [`158a70f`](https://github.com/Haidra-Org/hordelib/commit/158a70f32ab27dbea6eae9d37c2eddad90016263)  (Jug)
- docs: remove license to recreate it [`8ee4dde`](https://github.com/Haidra-Org/hordelib/commit/8ee4ddeb40b1824d029a7eca138cd76e61b484f0)  (Jug)
- build: placeholder changelog [`bbf880e`](https://github.com/Haidra-Org/hordelib/commit/bbf880e011ea34325beb0bbb46a0ad1545e25af0)  (Jug)

## [v0.5.5](https://github.com/Haidra-Org/hordelib/compare/v0.5.4...v0.5.5)

11 April 2023

## [v0.5.4](https://github.com/Haidra-Org/hordelib/compare/v0.5.3...v0.5.4)

11 April 2023

- build: add release mode flag [`#76`](https://github.com/Haidra-Org/hordelib/pull/76) (Jug)
- refactor!: Second big Model Manager rework step [`#75`](https://github.com/Haidra-Org/hordelib/pull/75) (tazlin)
- fix: adjust mlsd annotator defaults [`#74`](https://github.com/Haidra-Org/hordelib/pull/74) (Jug)
- chore: resolve merge conflicts [`007bc44`](https://github.com/Haidra-Org/hordelib/commit/007bc441ff448eda879994212fc0e5ad896b4e84)  (Jug)
- docs: remove the changelog from main [`6a650f2`](https://github.com/Haidra-Org/hordelib/commit/6a650f215482c316f77de2e8fb98609c4d60fbc7)  (Jug)
- fix: normal map and mlsd annotators [`203873d`](https://github.com/Haidra-Org/hordelib/commit/203873dc6e904f73f48c56d1b9f68509e3213c15)  (Jug)

## [v0.5.3](https://github.com/Haidra-Org/hordelib/compare/v0.5.2...v0.5.3)

11 April 2023

- build: patch release [`#73`](https://github.com/Haidra-Org/hordelib/pull/73) (Jug)
- build: try to fix test running and build [`9df056d`](https://github.com/Haidra-Org/hordelib/commit/9df056d98d4502398bb13437f51522cb6a0feebf)  (Jug)

## [v0.5.2](https://github.com/Haidra-Org/hordelib/compare/v0.5.1...v0.5.2)

11 April 2023

- build: upgrade to torch 2, xformers 18 and latest comfyui [`#68`](https://github.com/Haidra-Org/hordelib/pull/68) (Jug)

## [v0.5.1](https://github.com/Haidra-Org/hordelib/compare/v0.5.0...v0.5.1)

11 April 2023

- feat: Added is_model_loaded() to HyperMM [`#67`](https://github.com/Haidra-Org/hordelib/pull/67) (Divided by Zer0)

## [v0.5.0](https://github.com/Haidra-Org/hordelib/compare/v0.4.2...v0.5.0)

11 April 2023

- feat: add support for return_control_map [`#66`](https://github.com/Haidra-Org/hordelib/pull/66) (Jug)
- docs: update ci test badge [`e2b137e`](https://github.com/Haidra-Org/hordelib/commit/e2b137ed43d5b63c8a6f1d7899a31bbb78aa7045)  (Jug)

## [v0.4.2](https://github.com/Haidra-Org/hordelib/compare/v0.4.1...v0.4.2)

11 April 2023

- fix: resize img2img before inference [`#63`](https://github.com/Haidra-Org/hordelib/pull/63) (Divided by Zer0)
- fix: add timezone to build results [`#61`](https://github.com/Haidra-Org/hordelib/pull/61) (Jug)
- tests: gfpgan test and size assets [`#62`](https://github.com/Haidra-Org/hordelib/pull/62) (Divided by Zer0)
- docs: update with pypi test notes [`dd41120`](https://github.com/Haidra-Org/hordelib/commit/dd4112023d39e280fb61a1342707af4765f3b4df)  (Jug)

## [v0.4.1](https://github.com/Haidra-Org/hordelib/compare/v0.4.0...v0.4.1)

10 April 2023

- feat: Make use of the ControlNet ModelManager [`#53`](https://github.com/Haidra-Org/hordelib/pull/53) (Divided by Zer0)
- test: fix test with red border around it [`#58`](https://github.com/Haidra-Org/hordelib/pull/58) (Jug)
- build: activate build results website [`#57`](https://github.com/Haidra-Org/hordelib/pull/57) (Jug)
- build: make a webpage of test result images [`#55`](https://github.com/Haidra-Org/hordelib/pull/55) (Jug)
- test: fix black 64x64 image tests [`#54`](https://github.com/Haidra-Org/hordelib/pull/54) (Jug)
- version incremented [`14efa65`](https://github.com/Haidra-Org/hordelib/commit/14efa65031d595179cd00b4a1f27b9bce6ab88ac)  (github-actions)
- build: try to be smarter when we run tests [`e0d9d4b`](https://github.com/Haidra-Org/hordelib/commit/e0d9d4bea09233f0f59ac28a413dd754eab613b8)  (Jug)
- build: try to run tests more often [`4470a24`](https://github.com/Haidra-Org/hordelib/commit/4470a243135c47d1bc24859573c6676e58dfc64c)  (Jug)

## [v0.4.0](https://github.com/Haidra-Org/hordelib/compare/v0.3.1...v0.4.0)

10 April 2023

- feat: add face fixing support [`#50`](https://github.com/Haidra-Org/hordelib/pull/50) (Jug)
- version incremented [`c5aa1d5`](https://github.com/Haidra-Org/hordelib/commit/c5aa1d5614738cc50418772dcf70343e614e2e9d)  (github-actions)

## [v0.3.1](https://github.com/Haidra-Org/hordelib/compare/v0.3.0...v0.3.1)

10 April 2023

- test: change all tests to webp [`#49`](https://github.com/Haidra-Org/hordelib/pull/49) (Jug)
- version incremented [`a1adb39`](https://github.com/Haidra-Org/hordelib/commit/a1adb398cdc55f242158d6d3e2f6ec11645af892)  (github-actions)

## [v0.3.0](https://github.com/Haidra-Org/hordelib/compare/v0.2.2...v0.3.0)

10 April 2023

- feat: add controlnet support [`#46`](https://github.com/Haidra-Org/hordelib/pull/46) (Jug)
- version incremented [`62f72c1`](https://github.com/Haidra-Org/hordelib/commit/62f72c10373711df96d43f89c1834f2d4dee3cf5)  (github-actions)
- docs: add build status badge to readme [`86b3d1a`](https://github.com/Haidra-Org/hordelib/commit/86b3d1a61442733b0a81f97f02ca58f8196f2f1c)  (Jug)

## [v0.2.2](https://github.com/Haidra-Org/hordelib/compare/v0.2.1...v0.2.2)

9 April 2023

- ci: inpainting tests [`#47`](https://github.com/Haidra-Org/hordelib/pull/47) (Divided by Zer0)
- version incremented [`5940da8`](https://github.com/Haidra-Org/hordelib/commit/5940da8efeae955a45dc84ea51905d700df5b190)  (github-actions)

## [v0.2.1](https://github.com/Haidra-Org/hordelib/compare/v0.2.0...v0.2.1)

9 April 2023

- build: change how custom nodes are loaded into comfyui [`#44`](https://github.com/Haidra-Org/hordelib/pull/44) (Jug)

## [v0.2.0](https://github.com/Haidra-Org/hordelib/compare/v0.1.0...v0.2.0)

9 April 2023

- ci: Disable pypi publish [`#45`](https://github.com/Haidra-Org/hordelib/pull/45) (Divided by Zer0)
- docs: readme updates. [`#43`](https://github.com/Haidra-Org/hordelib/pull/43) (Jug)
- docs: readme updates. [`#42`](https://github.com/Haidra-Org/hordelib/pull/42) (Jug)
- feat: Re-adds diffusers model manager [`#41`](https://github.com/Haidra-Org/hordelib/pull/41) (tazlin)
- test: add diffusers inpainting run example [`#40`](https://github.com/Haidra-Org/hordelib/pull/40) (Jug)
- docs: update readme [`#39`](https://github.com/Haidra-Org/hordelib/pull/39) (Jug)
- refactor: We do some light refactoring... [`#34`](https://github.com/Haidra-Org/hordelib/pull/34) (Divided by Zer0)
- test: Optimized tests [`#32`](https://github.com/Haidra-Org/hordelib/pull/32) (Divided by Zer0)
- refactor: Significant code cleanup and CI/build improvements. [`#30`](https://github.com/Haidra-Org/hordelib/pull/30) (tazlin)
- feat: Post processors [`#27`](https://github.com/Haidra-Org/hordelib/pull/27) (Divided by Zer0)
- feat: adds inpainting [`dea0e9e`](https://github.com/Haidra-Org/hordelib/commit/dea0e9e54c8fcca87f4bb385fd68b811e8eb9a4e)  (Jug)
- feat: image loader, basic img2img [`04994ea`](https://github.com/Haidra-Org/hordelib/commit/04994eaa4cd224071630f479f49d3ca578cb920a)  (Jug)
- test: reduce vram requirements for hires fix tests [`2932764`](https://github.com/Haidra-Org/hordelib/commit/2932764a6e7bc5af271f883a11cb73ee94b5fb12)  (Jug)

## [v0.1.0](https://github.com/Haidra-Org/hordelib/compare/v0.0.10...v0.1.0)

6 April 2023

- fix: Duplicate lines [`#25`](https://github.com/Haidra-Org/hordelib/pull/25) (tazlin)
- feat: Adds a github action when pushing to main that will generate a new release and an automatic changelog [`#24`](https://github.com/Haidra-Org/hordelib/pull/24) (Jug)
- fix: References to `horde_model_manager`, more docs [`#23`](https://github.com/Haidra-Org/hordelib/pull/23) (tazlin)
- docs: Update LICENSE [`#20`](https://github.com/Haidra-Org/hordelib/pull/20) (tazlin)
- refactor: ModelManager improvements, test adjustments [`#19`](https://github.com/Haidra-Org/hordelib/pull/19) (tazlin)
- fix: missing return [`#18`](https://github.com/Haidra-Org/hordelib/pull/18) (Divided by Zer0)
- refactor: 'ModelManager' rework, added 'WorkerSettings' [`#17`](https://github.com/Haidra-Org/hordelib/pull/17) (tazlin)
- refactor: Test tweaks, type hint fixes [`#16`](https://github.com/Haidra-Org/hordelib/pull/16) (tazlin)
- refactor: Type hints, refactoring, preemptive checks [`#15`](https://github.com/Haidra-Org/hordelib/pull/15) (tazlin)
- feat: adds clip skip support [`dd1cbcc`](https://github.com/Haidra-Org/hordelib/commit/dd1cbcc44b9c8558f3961de1c99e25b548170066)  (Jug)
- refactor: make things more explicit. [`970fd4a`](https://github.com/Haidra-Org/hordelib/commit/970fd4a21b6b771fe5e83769a74a6ae4b9be2aec)  (Jug)
- feat: allow running comfyui easily. [`3ce7af1`](https://github.com/Haidra-Org/hordelib/commit/3ce7af146462bf2140b85514fef21314f2b8bdaa)  (Jug)

## [v0.0.10](https://github.com/Haidra-Org/hordelib/compare/v0.0.9...v0.0.10)

3 April 2023

- fix: test_horde.py syntax error [`#14`](https://github.com/Haidra-Org/hordelib/pull/14) (tazlin)
- fix: Compat fixes for tests from pr #11 [`#12`](https://github.com/Haidra-Org/hordelib/pull/12) (tazlin)
- feat: Clip interrogation support [`#11`](https://github.com/Haidra-Org/hordelib/pull/11) (tazlin)
- feat: Adds support for using a Model Manager  [`#8`](https://github.com/Haidra-Org/hordelib/pull/8) (Divided by Zer0)
- build: fixes for new model manager and clip [`9d09885`](https://github.com/Haidra-Org/hordelib/commit/9d0988505a845a433b60c9f9fe1d8e9784c8ced9)  (Jug)
- build: update comfyui to latest version [`a5cfc05`](https://github.com/Haidra-Org/hordelib/commit/a5cfc05352f8a86c9beb511ab5b869a2c72b6cb3)  (Jug)
- build: disable forced reformatting from black [`835ffe5`](https://github.com/Haidra-Org/hordelib/commit/835ffe546ec7dd43342bc133aeeaf6b625b8e357)  (Jug)

## [v0.0.9](https://github.com/Haidra-Org/hordelib/compare/v0.0.8...v0.0.9)

3 April 2023

- test: More thorough tests for ComfyUI install [`a247f2b`](https://github.com/Haidra-Org/hordelib/commit/a247f2b9fd9b62c3b0718468a50859e06c92ee65)  (Jug)
- build: adds build helper script. [`afd38ea`](https://github.com/Haidra-Org/hordelib/commit/afd38eabbf103b52c32a8e4daff2e7f1e7b2324d)  (Jug)
- build: don't run inference tests on github (no cuda) [`638056b`](https://github.com/Haidra-Org/hordelib/commit/638056bc2d48098a4cdcad592ab955abe815fcd7)  (Jug)

## v0.0.8

2 April 2023

- Initial commit. [`e3eae1c`](https://github.com/Haidra-Org/hordelib/commit/e3eae1c452e0f3145af3b8b62c14c377b3136f7b)  (Jug)
- feat: Support loading ComfyUI pipelines without manual modification. [`8c2fd13`](https://github.com/Haidra-Org/hordelib/commit/8c2fd13db4ce6a293f335cefaaf9c7d52aaefd7b)  (Jug)
- feat: adds stable difussion hires fix pipeline. [`6e573cb`](https://github.com/Haidra-Org/hordelib/commit/6e573cb364343569ad59cbd709b266d292021428)  (Jug)

Generated by [`auto-changelog`](https://github.com/CookPete/auto-changelog).
