# FDRI-comparing-rainfall-data-in-upper-severn
Project comparing rainfall estimates in the Upper Severn using rain gauges and gridded rainfall products. The two main gridded rainfall products available in the UK are the CEH-GEAR and HadUK-Grid, both of which have been extracted on a 1km by 1km grid.

This work was carried out as part of the [Floods and Droughts Research Infrastructure](https://fdri.org.uk/) (FDRI) project led by the UK Centre for Ecology & Hydrology.

### The Upper Severn
<img src="figures/upper_severn_catchments.png" width="600">


## Factors contributing to differences between CEH-GEAR & HadUK-Grid
### Interpolation methods
[Figure showing IDW vs Natural Neighbour]

### Quality control procedures on the inclusion of rain gauges data
Figure below compares annual differences in mean rainfall between CEH-GEAR and HadUK. Positive (red) values represent higher rainfall in CEH-GEAR than HadUK-Grid. Outlines represent the Abermule (largest), Dolwen and Plynlimon Flume (smallest) catchment boundaries
![til](./figures/abermule_annual_differences_w_gauge_changes.gif)

### Cumulative rainfall comparing gauged and gridded rainfall over Carreg Wen
*Dashed-lines represent flood dates*
<img src="figures/monthly_carreg_wen_rainfall.png" width="600">

### Cumulative rainfall difference from rain gauge
*Dashed-lines represent flood dates*
<img src="figures/monthly_carreg_wen_rainfall_diff.png" width="600">

## Severn-wide flood events at Carreg Wen
<img src="figures/flood_comparison_line.png" width="600">

### Cumalative rainfall
*including the sum of rain 10-0 days before the event*
<img src="figures/flood_comparison_heatmap_percentage_difference.png" width="600">


### Nearby rain gauges
There are not many rain gauges active near Carreg-wen
<img src="figures/flood_comparison_line_nearbygauges_w_grid.png" width="600">

<img src="figures/flood_comparison_line_nearbygauges_w_grid_nearby.png" width="600">


### Maps of floods
More maps available under `figures/`
<img src="figures/ceh_vs_haduk_grid_vs_gauge_sum_rain_13_Feb_2001.png" width="600">