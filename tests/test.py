import mesdf
import trimesh
import numpy as np
import pytest
import inspect
import os

path = os.path.dirname(
    os.path.abspath(inspect.getsourcefile(lambda: 0))
)

def test_sdf():
    obj = trimesh.load_mesh(os.path.join(path, '..', "sample-obj", "boxframe.obj"))
    sdf = mesdf.SDF(verts=obj.vertices, faces=obj.faces)
    p = np.array([1.0, 2.0, 3.0])
    assert pytest.approx(sdf(p)[0]) == -2.9094794