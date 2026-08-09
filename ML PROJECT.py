# PART 1: THE SETUP
# Import the tools we installed
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import rasterio
import matplotlib.pyplot as plt

def run_ml_classification():
    print("Starting Machine Learning Process...")

    # PART 2: CREATE A DUMMY SATELLITE IMAGE
    # Since you don't have a massive satellite file yet, we will generate a tiny fake one to test the logic.
    # Let's pretend this is a 100x100 pixel image with 3 bands (Red, Green, Near-Infrared)
    width = 100
    height = 100
    bands = 3
    
    # np.random.rand generates random numbers to act as fake pixel colors
    print("1. Generating fake satellite image...")
    fake_satellite_image = np.random.rand(bands, height, width)

    # To feed this to the ML model, we must flatten it from 3D (3x100x100) to 2D (10000 pixels x 3 bands)
    # We read the bands, transpose them, and reshape them into a long table.
    flattened_pixels = fake_satellite_image.transpose(1, 2, 0).reshape(-1, bands)


    # PART 3: THE CHEAT SHEET (TRAINING DATA)
    # We need to teach the model what to look for. 
    # 'X' is the clues (the color numbers). 'y' is the answer (1=Water, 2=Forest, 3=City).
    print("2. Preparing training data...")
    
    # 10 fake examples of Water (high blue, low red/infrared)
    water_clues = np.array([[0.1, 0.1, 0.8]] * 10) 
    water_answers = np.array([1] * 10)             

    # 10 fake examples of Forest (low red/blue, high infrared)
    forest_clues = np.array([[0.2, 0.9, 0.2]] * 10) 
    forest_answers = np.array([2] * 10)             

    # Combine our clues (X) and answers (y) together
    X_train = np.vstack((water_clues, forest_clues))
    y_train = np.concatenate((water_answers, forest_answers))


    # PART 4: THE BRAIN (TRAINING)
    print("3. Training the Random Forest...")
    # We create the brain, telling it to use 50 decision trees
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    
    # .fit() is the most important word in Machine Learning. It means "Learn this data."
    model.fit(X_train, y_train)


    # PART 5: THE TEST (PREDICTING)
    print("4. Predicting the whole map...")
    # Now we hand it the 10,000 unclassified pixels from our fake image.
    # .predict() tells it to guess the answer for every single one.
    predicted_pixels = model.predict(flattened_pixels)


    # PART 6: REBUILDING THE MAP
    print("5. Rebuilding map...")
    # The result is a long list of 10,000 numbers. We reshape it back into a 100x100 grid.
    final_map_grid = predicted_pixels.reshape(height, width)
    
    print("Process Complete! In a real scenario, we would now save 'final_map_grid' as a .tif file using rasterio.")
    # PART 7: SHOWING THE MAP
    print("6. Displaying the map...")
    plt.imshow(final_map_grid, cmap='viridis')
    plt.colorbar(label='Land Cover Class (1=Water, 2=Forest, 3=City)')
    plt.title('Machine Learning Land Cover Map')
    plt.show()

# This tells Python to actually run the function above when you start the file
if __name__ == "__main__":
    run_ml_classification()
    