import os
import rasterio

def create_multispectral_image():
    print("Starting the stacking process...")
    
    # Locate the folder where this script lives (D:\Mim's Projects)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check for 'Data' or 'data' folder
    data_dir = os.path.join(script_dir, 'Data')
    if not os.path.exists(data_dir):
        data_dir = os.path.join(script_dir, 'data')

    # Define the 4 band file paths
    file_list = [
        os.path.join(data_dir, 'band2.tif'),
        os.path.join(data_dir, 'band3.tif'),
        os.path.join(data_dir, 'band4.tif'),
        os.path.join(data_dir, 'band5.tif')
    ]

    # Check that all 4 files exist before running
    for filepath in file_list:
        if not os.path.exists(filepath):
            print(f"\nERROR: File not found -> {filepath}")
            print("Please ensure the file is named 'band2' (lowercase) inside your Data folder.")
            return

    # Open band 2 to copy metadata
    with rasterio.open(file_list[0]) as src0:
        meta = src0.meta

    # Update metadata count to 4 bands
    meta.update(count=len(file_list))

    # Output master file location
    output_path = os.path.join(data_dir, 'kangra_master.tif')
    with rasterio.open(output_path, 'w', **meta) as dst:
        for band_idx, layer_path in enumerate(file_list, start=1):
            with rasterio.open(layer_path) as src1:
                dst.write_band(band_idx, src1.read(1))
                print(f"Added band {band_idx} to the stack.")
                
    print(f"\nSuccess! Master image saved to: {output_path}")

if __name__ == "__main__":
    create_multispectral_image()