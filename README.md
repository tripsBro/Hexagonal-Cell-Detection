# Hexagon-Detection

A project to summarize my attempt at finding and counting hexagons and/or distorted hexagonal endothelial cells in an corneal image.

## Abstract

The corneal endothelium is a single cell layer on the innermost surface of the cornea. A given number or density of endothelial cells is present at birth, usually about 5,000 cells per square millimeter. There is a normal, progressive and slow loss of endothelial cells with aging. Specular microscopy is a noninvasive photographic technique that gives us a visualization of the corneal endothelium. I got fortunate enough to work with some of the images. The target was to find and count the endothelial cells in the image. 

### Analysis 1: Low contrast Image

The Specular microscope gave a very low contrast B/W image. The exposure of the images were a little offset and the endothelial cells were not clear. This problem has been solved by Adaptive Thresholding and Histogram Equalization.

### Analysis 2: Hexagonal Cells

The endothelial cells appreared to be approximately hexagonal when tried to construct a generalized geometric figure with a lot of images. Hexagons are very interesting geometric shape to detect as for an image with such low resolution the hexagons tend to be miscalculated as a circle. This puts straight restriction to a lot of common methods. Here I have tried to solve it by two popular methods.

### Analysis 3: Cell Density and Approximate Area

The cell density, i.e number of cells per square millimeter, can be found by counting number of detected cells in a fixed frame shape and then be inveresed mapped by knowing the camera resolution.

This project can be modified and extended to detect cells in any medical image.
