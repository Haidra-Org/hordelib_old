# test_initialisation.py


def test_find_comfyui():
    from hordelib.ComfyUI import execution

    assert hasattr(execution, "get_input_data")


def test_instantiation():
    from hordelib.pipeline import HordeComfyPipelineHandler

    _ = HordeComfyPipelineHandler()
    assert isinstance(_, HordeComfyPipelineHandler)


def test_path():
    """Because ComfyUI is not a library, we change the python paths to include it,
    as if it were a package."""
    import sys

    from hordelib.config_path import set_system_path

    set_system_path()
    foundComfy = False
    for path in sys.path:
        if "ComfyUI" in path:
            foundComfy = True
            break
    assert foundComfy is True


def test_imports():
    """This is fallback test to catch any new files which have errors on import."""
    import pkgutil
    import types

    import hordelib

    def recurse_packages(path):
        modules = pkgutil.walk_packages(path)
        for finder, name, ispkg in modules:
            if name == "esrgan":  # XXX # FIXME
                continue
            if ispkg:
                print(f"recursing: {name}")
                print(finder.path)
                recurse_packages([f"{finder.path}/{name}"])
                continue

            loader = finder.find_module(fullname=name)  # type: ignore
            assert loader is not None
            loaded_module = loader.load_module(name)
            assert isinstance(loaded_module, types.ModuleType)

    recurse_packages(hordelib.__path__)
