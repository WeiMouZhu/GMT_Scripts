'''
Author:  WilmerZhu
Email: zhuwm@mail.iggcas.ac.cn
Date: 2023-09-24 10:07:14
LastEditTime: 2024-01-11 10:50:21
FilePath: /GMT_Scripts/2017_Lv_Vpn_Alps.py

'''
###############################################################################
# Description:
# This is for plotting the Pn velocity fig in the Alps
# data from 2017_Lv
###############################################################################
import pandas as pd
import pygmt
###############################################################################
# define parameters for plotting
pygmt.config(
    MAP_FRAME_TYPE="plain",
    MAP_GRID_PEN_PRIMARY="0.3p,dimgrey",
    MAP_ANNOT_OBLIQUE="30",
    MAP_ANNOT_OFFSET_PRIMARY="5p",
    MAP_ANNOT_OFFSET_SECONDARY="5p",
    FONT_ANNOT_PRIMARY="10p,5",
    FONT_LABEL="10p,28,black",
    MAP_FRAME_WIDTH="2p",
    MAP_FRAME_PEN="0.5p",
    MAP_TICK_LENGTH_PRIMARY="5p",
    MAP_LABEL_OFFSET="5.5p",
)
# define the region for plotting
region_Alps = [4, 20, 38, 49]
# dealing with the Pn velocity
pygmt.surface(
    region=region_Alps,
    spacing="0.1/0.1",
    data="data_Alps/Pn/2017_Lv_Pn_cut.txt",
    outgrid="data_Alps/Pn/Alps_Pn_velo.grd",
)
# make cpt file for Pn velocity
pygmt.makecpt(
    cmap="jet",
    series=[7.4, 8.7],
    reverse=True,
    # continuous=True,
    output="data_Alps/cpt/Alps_Pn_velo.cpt",
)

# begin plot
fig = pygmt.Figure()

fig.grdimage(
    grid="data_Alps/Pn/Alps_Pn_velo.grd",
    region=region_Alps,
    projection="M15c",
    frame = ["af", f"WsNe"],
    cmap="data_Alps/cpt/Alps_Pn_velo.cpt",
)

fig.coast(
    resolution="i",
    shorelines="1/0.5p,black",
    # C="steelblue",
    # borders=["1/0.5p,black,--"],
    # water="white",
    # map_scale="f8.3/70.3/56/400+lkm+jt",
)

with pygmt.config(
    FONT_ANNOT_PRIMARY="10p,5",
    FONT_LABEL="10p",
    MAP_ANNOT_OFFSET="0.05i",
    MAP_TICK_LENGTH_PRIMARY="0.05",
    MAP_LABEL_OFFSET="3.5p",
    MAP_FRAME_PEN="0.8p",
):
    fig.colorbar(
        frame="af+lPn velocity (km/s)",
        position="jBL+w4c/0.4c+o0.55c/1.c+h",
        box="+r2p+gwhite@10+p0.5p",
        cmap="data_Alps/cpt/Alps_Pn_velo.cpt",
    )

fig.savefig("fig_Alps/Alps_Pn_velo_py.pdf", dpi=720, show=True)
