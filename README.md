# FDRI-comparing-rainfall-data-in-upper-severn
Project comparing rainfall estimates in the Upper Severn using rain gauges and gridded rainfall products. 

**Project Goal:** To reduce the uncertainty of rain-driven flood estimation in the upper reaches of the Severn catchment.

*This work was carried out as part of the [Floods and Droughts Research Infrastructure](https://fdri.org.uk/) (FDRI) project led by the UK Centre for Ecology & Hydrology.*

## The Upper Severn
We examine three catchments towards the source of the River Severn:  [Abermule](https://nrfa.ceh.ac.uk/data/station/info/54014) (flow gauge at: 86.8 m), [Dolwen](https://nrfa.ceh.ac.uk/data/station/info/54080) (147.3 m) and [Plynlimon Flume](https://nrfa.ceh.ac.uk/data/station/info/54022) (321.3 m). 
<img src="figures/upper_severn_catchments.png" width="600">

## Gridded rainfall data products
The two main observation-based gridded rainfall products available for the UK are the CEH-GEAR (available [here](https://catalogue.ceh.ac.uk/documents/dbf13dd5-90cd-457a-a986-f2f9dd97e93c)) and HadUK-Grid (available [here](https://catalogue.ceda.ac.uk/uuid/4dc8450d889a491ebb20e724debe2dfb/)). For this project, we use daily 1km by 1km rainfall from each of these products.

# Factors contributing to differences between CEH-GEAR & HadUK-Grid
## Reduction in daily rain gauges in Upper Severn
In the 1980s there used to be more rain gauges in the Upper Severn (see figure below):
*Red circles represent daily rain gauges around the Abermule catchment available and used in the CEH-GEAR data product.*
<img src="figures/num_gauges_around_abermule_1980vs2022.png" width="700">

This puts more uncertainty into the rainfall estimation, and means greater differences are created by the exact methods used to spatially interpolate data from rain gauges to a regular grid (e.g. 1km by 1km).

## Gridding methods
Rain gauge data is interpolated onto a regular grid. The exact gauges which are included differ based on gridded rainfall product.

Example of rain gauge data onto a regular grid:  
<img src="figures/gridding_example_from_gdal.png" width="400">

CEH-GEAR uses [Natural Neighbour Interpolation](https://en.wikipedia.org/wiki/Natural-neighbor_interpolation), HadUK-Grid uses [Inverse Distance Weighting](https://en.wikipedia.org/wiki/Inverse_distance_weighting).

Differences will be subtle, but the choice of spatial interpolation creates uncertainty.
Below a figure shows the differences between spatial interpolation methods (for more see: [DOI:10.5772/65996](https://www.intechopen.com/chapters/52704)):  
<img src="figures/fig2_from_wu_and_hung_2016.png" width="400">


<!-- ## Quality control procedures on the inclusion of rain gauges data -->

# Exploring differences
## Methods
We mask the areas around each catchment
<img src="figures/ceh_vs_haduk_differences/catchment_mask_vs_boundary.png" width="700">

We also use a 1km by 1km height profile for the region
<img src="figures/gauge_distance_vs_height/abermule_height_profile.png" width="500">

## Results
<!-- Clearly there is a bias in certain regions
<img src="figures/ceh_vs_haduk_differences/ceh_vs_haduk_by_season.png" width="700">  -->

Histogram of differences between CEH-Gear and HadUK in Upper Severn:  
<img src="figures/ceh_vs_haduk_differences/catchment_hist_ceh_vs_haduk.png" width="700">

Rainfall difference between CEH-GEAR and HadUK vs Height of rain gauge.  
<img src="figures/ceh_vs_haduk_differences/uppersevern_rain_vs_height_scatter.png" width="700">

Rainfall difference between CEH-GEAR and HadUK versus minimum distance to gauge (from CEH-GEAR).  
<img src="figures/ceh_vs_haduk_differences/uppersevern_rainfall_vs_mindist_scatter.png" width="700">

Height of rain gauge versus minimum distance to gauge (from CEH-GEAR).  
<img src="figures/ceh_vs_haduk_differences/uppersevern_height_vs_mindist_scatter.png" width="700">

# Influence of gridded data differences during floods
We examine 5 major Severn-wide high flow events (i.e. those above 95th percentile in each of the Abermule, Plynlimon, Bewdley, Buildwas and Dolwen catchments).
TODO...
<!-- <img src="figures/carreg_wen_gauge_vs_grid/flood_comparison_line.png" width="700"> -->

The rain gauge used (Carreg Wen) is data that was not included in either the CEH-GEAR or HadUK-Grid.   
<img src="figures/carreg_wen_gauge_vs_grid/flood_comparison_heatmap_percentage_difference.png" width="700">

<img src="figures/carreg_wen_gauge_vs_grid/uppersevern_flood_events_differences.png" width="700">


# Other
Figure below compares annual differences in mean rainfall between CEH-GEAR and HadUK. Positive (red) values represent higher rainfall in CEH-GEAR than HadUK-Grid. Outlines represent the Abermule (largest), Dolwen and Plynlimon Flume (smallest) catchment boundaries
![til](./figures/abermule_annual_differences_w_gauge_changes.gif)