# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.5.1 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/ami/Desktop/virtauslaskenta/etukateenTehty/cad')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("L", 0.075)
notebook.set("R", 0.025)
notebook.set("LR", "L+R")
notebook.set("nR", "-R")
notebook.set("rb", 0.01)
notebook.set("rs", 0.005)
notebook.set("Ls", 0.025)
notebook.set("nLs", "-Ls")
####################################################
##        End of NoteBook variables section       ##
####################################################
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Vertex_1 = geompy.MakeVertex(0, 0, 0)
Vertex_2 = geompy.MakeVertex(0, "L", 0)
Vertex_3 = geompy.MakeVertex("R", "LR", 0)
Vertex_4 = geompy.MakeVertex("LR", "LR", 0)
Vertex_5 = geompy.MakeVertex("nLs", "LR", 0)
Disk_1 = geompy.MakeDiskPntVecR(Vertex_1, OY, "rb")
Disk_2 = geompy.MakeDiskPntVecR(Vertex_5, OX, "rs")
Line_1 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_2)
Line_2 = geompy.MakeLineTwoPnt(Vertex_3, Vertex_4)
Vertex_6 = geompy.MakeVertex("R", "L", 0)
Arc_1 = geompy.MakeArcCenter(Vertex_6, Vertex_2, Vertex_3,False)
Wire_1 = geompy.MakeWire([Line_1, Line_2, Arc_1], 1e-07)
Pipe_1 = geompy.MakePipe(Disk_1, Wire_1)
Extrusion_1 = geompy.MakePrismVecH(Disk_2, OX, "L")
Fuse_1 = geompy.MakeFuseList([Pipe_1, Extrusion_1], True, False)
[inletSmall,Face_2,inletBig,Face_4,Face_5,Face_6,outlet] = geompy.ExtractShapes(Fuse_1, geompy.ShapeType["FACE"], True)
wall = geompy.CreateGroup(Fuse_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(wall, [12, 7, 27, 22])
geompy.ExportSTL(inletSmall, "/home/ami/Desktop/virtauslaskenta/etukateenTehty/cad/inletSmall.stl", True, 0.001, True)
geompy.ExportSTL(inletBig, "/home/ami/Desktop/virtauslaskenta/etukateenTehty/cad/inletBig.stl", True, 0.001, True)
geompy.ExportSTL(outlet, "/home/ami/Desktop/virtauslaskenta/etukateenTehty/cad/outlet.stl", True, 0.001, True)
geompy.ExportSTL(wall, "/home/ami/Desktop/virtauslaskenta/etukateenTehty/cad/wall.stl", True, 0.001, True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Disk_1, 'Disk_1' )
geompy.addToStudy( Disk_2, 'Disk_2' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Wire_1, 'Wire_1' )
geompy.addToStudy( Pipe_1, 'Pipe_1' )
geompy.addToStudy( Extrusion_1, 'Extrusion_1' )
geompy.addToStudy( Fuse_1, 'Fuse_1' )
geompy.addToStudyInFather( Fuse_1, inletSmall, 'inletSmall' )
geompy.addToStudyInFather( Fuse_1, Face_2, 'Face_2' )
geompy.addToStudyInFather( Fuse_1, inletBig, 'inletBig' )
geompy.addToStudyInFather( Fuse_1, Face_4, 'Face_4' )
geompy.addToStudyInFather( Fuse_1, Face_5, 'Face_5' )
geompy.addToStudyInFather( Fuse_1, Face_6, 'Face_6' )
geompy.addToStudyInFather( Fuse_1, outlet, 'outlet' )
geompy.addToStudyInFather( Fuse_1, wall, 'wall' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)
