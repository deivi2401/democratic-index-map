import geopandas as gpd

shapefile_path = 'ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile_path)
output_csv_path = 'C:/Users/towrz/Downloads/file.csv'

gdf.to_csv(output_csv_path, index=False)

print(f"Los datos se han guardado exitosamente en '{output_csv_path}'.")
