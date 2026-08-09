
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import rasterio
import matplotlib.pyplot as plt

def run_ml_classification():
    print("Starting Machine Learning Process...")


    width = 100
    height = 100
    bands = 3
    
  
    print("1. Generating fake satellite image...")
    fake_satellite_image = np.random.rand(bands, height, width)


    flattened_pixels = fake_satellite_image.transpose(1, 2, 0).reshape(-1, bands)



    print("2. Preparing training data...")
    
    
    water_clues = np.array([[0.1, 0.1, 0.8]] * 10) 
    water_answers = np.array([1] * 10)             

    
    forest_clues = np.array([[0.2, 0.9, 0.2]] * 10) 
    forest_answers = np.array([2] * 10)             

    
    X_train = np.vstack((water_clues, forest_clues))
    y_train = np.concatenate((water_answers, forest_answers))


    
    print("3. Training the Random Forest...")
   
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    
    
    model.fit(X_train, y_train)


    print("4. Predicting the whole map...")

    predicted_pixels = model.predict(flattened_pixels)


    
    print("5. Rebuilding map...")
    
    final_map_grid = predicted_pixels.reshape(height, width)
    
    print("Process Complete! In a real scenario, we would now save 'final_map_grid' as a .tif file using rasterio.")
    
    print("6. Displaying the map...")
    plt.imshow(final_map_grid, cmap='viridis')
    plt.colorbar(label='Land Cover Class (1=Water, 2=Forest, 3=City)')
    plt.title('Machine Learning Land Cover Map')
    plt.show()

if __name__ == "__main__":
    run_ml_classification()
    
