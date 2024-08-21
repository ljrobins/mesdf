import mesdf
import trimesh
import numpy as np
import pytest


def test_sdf():
    obj = trimesh.load_mesh("sample-obj/boxframe.obj")
    sdf = mesdf.SDF(verts=obj.vertices, faces=obj.faces)
    p = np.array([1.0, 2.0, 3.0])
    assert pytest.approx(sdf(p)[0]) == -2.9094794
