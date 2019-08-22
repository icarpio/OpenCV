# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:12 2019
Este ejemplo construye un Gráfico de adyacencia de región (RAG) y combina progresivamente regiones que son similares en color. 
Fusionar dos regiones adyacentes produce una nueva región con todos los píxeles de las regiones fusionadas. 
Las regiones se fusionan hasta que no quedan pares de regiones muy similares.
@author: Icarpio
"""

from skimage import data, io, segmentation, color
from skimage.future import graph
import numpy as np

PTH='./images/'
def _weight_mean_color(graph, src, dst, n):

    diff = graph.node[dst]['mean color'] - graph.node[n]['mean color']
    diff = np.linalg.norm(diff)
    return {'weight': diff}

def merge_mean_color(graph, src, dst):
    graph.node[dst]['total color'] += graph.node[src]['total color']
    graph.node[dst]['pixel count'] += graph.node[src]['pixel count']
    graph.node[dst]['mean color'] = (graph.node[dst]['total color'] / graph.node[dst]['pixel count'])

img = io.imread('persona.jpg')

labels = segmentation.slic(img, compactness=30, n_segments=400)  
g = graph.rag_mean_color(img, labels) 
labels2 = graph.merge_hierarchical(labels, g, thresh=35, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=merge_mean_color,
                                   weight_func=_weight_mean_color)

out = color.label2rgb(labels2, img, kind ='avg')
out = segmentation.mark_boundaries(out, labels2,(0,0,0))
mos = segmentation.mark_boundaries(out, labels,(0,0,0))
io.imshow(out)

io.imsave(PTH+'rag.jpg', out)
io.imsave(PTH+'mosaico.jpg', mos)
io.show()


    
    
    
    
    