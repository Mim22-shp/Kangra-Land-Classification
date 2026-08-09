# Machine Learning Land Cover Classification: Kangra Valley

## Project Overview
This project applies machine learning to remote sensing data to automatically classify land cover in the Kangra Valley, Himachal Pradesh. The model categorizes the terrain into three distinct classes: Water, Forest, and Urban/City environments.

## Methodology
1. **Data Acquisition:** Sourced multispectral Level-2 Surface Reflectance data from Landsat 8 (Bands 2, 3, 4, and 5) to capture true-color and near-infrared signatures.
2. **Preprocessing:** Stacked individual spectral bands into a unified multidimensional master raster using `rasterio`.
3. **Training Data Generation:** Digitized ground-truth polygons over visually identified features using QGIS.
4. **Model Architecture:** Implemented a Random Forest Classifier (`scikit-learn`). The model extracts pixel values intersecting with the ground-truth polygons to learn spectral signatures, then predicts the classification for the entire regional footprint.

## Tech Stack
* **Python:** Core scripting.
* **Geospatial Libraries:** `rasterio`, `geopandas`, `shapely`.
* **Machine Learning:** `scikit-learn` (Random Forest).
* **GIS Software:** QGIS (for training data digitization and CRS management).