**Please use your own copies of the HadUK-Grid data**
## Downloading HadUK-Grid
1km HadUK-Grid data available from CEDA at: https://catalogue.ceda.ac.uk/uuid/4dc8450d889a491ebb20e724debe2dfb/ (Last accessed 5th Feb 25)

## Using HadUKGrid on JASMIN
See CEDA link above for path: /badc/ukmo-hadobs/data/insitu/MOHC/HadOBS/HadUK-Grid/v1.3.0.ceda/1km/rainfall

## Using CEH-Gear 1km instead:
If you would like to use the CEH-Gear dataset instead (available [here](https://catalogue.ceh.ac.uk/documents/dbf13dd5-90cd-457a-a986-f2f9dd97e93c)), the grid is slightly offest by about 50 metres from the grid that the topography (HGHT) data is on. Please adapt the following code for your purpose:
```python

SEVERN_X_RANGE = slice(280000, 399500)
SEVERN_Y_RANGE = slice(260000, 359500)
def coerse_cehgear_into_haduk(one_day_cehgear, offset=50):
    """
    Quick fix for coersing CEH-GEAR to have same grid as HADUK.
    """
    one_day_cehgear = one_day_cehgear.assign_coords(x=(one_day_cehgear['x'] + offset))
    one_day_cehgear = one_day_cehgear.assign_coords(y=(one_day_cehgear['y'] + offset))
    one_day_cehgear = one_day_cehgear.sel(x=SEVERN_X_RANGE, y=SEVERN_Y_RANGE)
    one_day_cehgear = one_day_cehgear.rename({'x': 'projection_x_coordinate', 'y': 'projection_y_coordinate'})
    return one_day_cehgear

```