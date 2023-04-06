# test_initialisation.py


def test_find_comfyui():
    from hordelib.ComfyUI import execution

    assert hasattr(execution, "get_input_data")


def test_instantiation():
    from hordelib.pipeline import HordeComfyPipelineHandler

    _ = HordeComfyPipelineHandler()
    assert isinstance(_, HordeComfyPipelineHandler)


def test_path():  # XXX
    from hordelib.config_path import set_system_path

    set_system_path()
