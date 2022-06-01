import rioxarray


def test_dim_reordering(bahamas_rgb):
    da = rioxarray.open_rasterio(bahamas_rgb)
    # ('band', 'y', 'x')
    assert da.pyvista_rectilinear._get_ordered_dims() == ("x", "y", "band")
