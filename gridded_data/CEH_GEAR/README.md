**Please use your own copies of the CEH-GEAR data**
## Downloading CEH-GEAR
1km CEH-GEAR rainfall data available from UKCEH EIDC [here](https://catalogue.ceh.ac.uk/documents/dbf13dd5-90cd-457a-a986-f2f9dd97e93c) (Last accessed 10th Mar 25)

## Using CEH-Gear 1km with HadUK-Grid:
The CEH-Gear dataset has a grid that is slightly offest compared with HadUK-Grid by about 50 metres. This is also the offset from the from the grid that the topography (HGHT) data is on. Please adapt the following code for your purpose:
```python

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