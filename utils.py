# Utils for loading inputs, manipulating data, and plotting results
import pandas as pd
import s3fs
import xarray as xr
import numpy as np
import geopandas as gpd
import sparse
from shapely.geometry import Polygon
import fsspec
import dask
from matplotlib import cm
import matplotlib.pyplot as plt
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy      
import matplotlib as mpl


def map_cities(ax, df, column_name, cmap, var_limits):
    m = ax.scatter(df['longitude'], df['latitude'], 
                c=df[column_name], 
                s=4,
               cmap=cmap,
               vmin=var_limits[0], vmax=var_limits[1], 
                   rasterized=True, 
                  #  edgecolor='k',
                  # linewidths=0.2
                  )
    ax.coastlines(color='gray')
    ax.add_feature(cartopy.feature.BORDERS, edgecolor='gray', zorder=-5)
    ax.set_extent([-7, 52, 31, 58])
    return m

def multipanel_map(df, threshold, var_limits, variable):
    figure, axarr = plt.subplots(4, 2, subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10,10))
    axarr[0,0].set_title('Historical')
    c = map_cities(axarr[0,0], 
                   df, 
                   f'days over {threshold} degC - CarbonPlan - historical', 
                   'OrRd',
                   var_limits)
    for i, timeframe in enumerate(['2030', '2050', '2070']):
        for j, scenario in enumerate(['ssp245', 'ssp370']):
            c = map_cities(axarr[i+1,j], 
                           df, 
                           f'days over {threshold} degC - CarbonPlan - {scenario}-{timeframe}',
                           'OrRd',
                           var_limits)
            axarr[i+1,j].set_title(f'{scenario.upper()} - {timeframe}')

    axarr[0,1].axis('off')

    plt.suptitle(f'Median days per year with maximum daily {variable} exceeding {threshold} $^\circ$C')
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15, hspace=0.2)
    cbar_ax = figure.add_axes([0.1, 0.1, 0.8, 0.04])
    cbar = figure.colorbar(c, cax=cbar_ax, orientation='horizontal')
    cbar.set_label('# days')
    plt.savefig(f'./figures/days_exceeding_{threshold}_{variable}.svg', format='svg')

def calc_emergence_categories(df):
    for ndays in [10, 20]:
        for scenario in ['ssp245', 'ssp370']:
            emergence=(df[['days over 29 degC - CarbonPlan - historical', 
                            f'days over 29 degC - CarbonPlan - {scenario}-2030', 
                            f'days over 29 degC - CarbonPlan - {scenario}-2050', 
                            f'days over 29 degC - CarbonPlan - {scenario}-2070']] > ndays).sum(axis=1)
            df[f'emergence-{scenario}-{ndays}']=emergence*-1+4
    return df

def emergence_cmap():
    # Define listed colormap
    cmap_list = ['#1b1e23', '#f07071', '#ea9755', '#d4c05e', '#a9b4c4']
    cmap = mpl.colors.ListedColormap(cmap_list)
    return cmap


def plot_multipanel_daily_timeseries(cities, df, ds_shade, ds_sun, threshold, scenario, time_frame):
    fig, axarr = plt.subplots(nrows=4, ncols=2, figsize=(8,10), sharex=True, sharey=True)

    for i, city, in enumerate(cities):
        city_id = df[df['UC_NM_MN']==city]['ID_HDC_G0'].values[0].astype('int')-1
        ax = axarr.flatten()[i]
        ds_shade.sel(processing_id=city_id
                        ).groupby('time.dayofyear').mean()['wbgt-shade'].mean(dim='gcm'
                        ).plot(ax=ax, label='Shade', rasterized=True)
        ds_sun.sel(processing_id=city_id
                        ).groupby('time.dayofyear').mean()['wbgt-sun'].mean(dim='gcm'
                        ).plot(ax=ax, label='Sun', rasterized=True)

        ax.axhline(y=threshold, color='grey', linestyle='--', zorder=-5, rasterized=True)
        ax.set_ylabel('WBGT $^\circ$C')
        ax.set_ylim(0,40)
        ax.set_title(city)
    if i==5:
        ax.legend()
    plt.tight_layout()
    plt.savefig(f'./figures/sun_shade_sample_timeseries_{scenario}_{time_frame}.svg', format='svg')