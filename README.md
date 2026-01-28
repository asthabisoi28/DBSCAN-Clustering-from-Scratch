**DBSCAN Clustering from Scratch**
Overview

This project implements the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm completely from scratch using Python.
The goal is to group data points based on density and identify clusters and noise without predefining the number of clusters.
The implementation uses Euclidean distance, NumPy for calculations, and matplotlib for visualization.

Features
- DBSCAN implemented from scratch
- Uses Euclidean distance
- Identifies core, border, and noise points
- Works on a 2D synthetic dataset
- Clear cluster visualization
- No external ML libraries used

Technologies Used:
- Python 3.10.11
- NumPy
- matplotlib

How the Project Works:

1. Dataset Creation
A synthetic 2D dataset is generated using NumPy.
It contains:
- Three dense clusters placed at different locations
- Random noise points scattered across the space
- This helps clearly demonstrate how DBSCAN detects clusters and isolates noise.

2. DBSCAN Implementation
The DBSCAN algorithm is implemented in dbscan.py without using any external ML libraries.
Steps-
- Calculating Euclidean distance between points
- Finding neighboring points within a given radius (eps)
- Identifying core points, border points, and noise
- Expanding clusters based on density
Noise points are labeled as -1, while clusters are labeled starting from 0.

3. Visualization
The clustered data is visualized using a scatter plot:
- Each cluster is shown in a different color
- Noise points are shown in black
This makes it easy to understand how DBSCAN groups points based on density.

Parameters Used:
1. eps = 1.2
Defines the maximum Euclidean distance between two points to be considered neighbors.
2. min_samples = 5
Minimum number of points required to form a dense region (core point).

Time Complexity
O(n²) - Each point checks its distance against all other points during neighborhood searches.

