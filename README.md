<p align="left" >
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://carbonplan-assets.s3.amazonaws.com/monogram/light-small.png">
  <img alt="CarbonPlan monogram." height="48" src="https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png">
</picture>
</p>

# carbonplan / extreme-heat-extension-data

## summary

This repository provides access to code, data, and pre-generated figures to assess the risk of extreme humid heat in cities across Southeast Europe and Central Asia. The work contained here builds on [previous work](https://github.com/carbonplan/extreme-heat), expanding the dataset's number of scenarios and time coverage. The data is fully reproducible using a codebase located [here](https://github.com/carbonplan/extreme-heat-extension). The work was supported by The World Bank's Global Practice for Urban, Resilience and Land and Global Facility for Disaster Reduction and Recovery.

## data

The final output dataset includes historical and future estimates of WBGT in the shade and in the sun for 130 cities across Southeast Europe and 204 cities across Central Asia. The full analysis includes 22 global climate models (GCMs) and two emissions scenarios (SSP2-4.5 and SSP3-7.0) for different time periods depending on the region of interest. To support different use cases, we've made the results available at a few different levels of granularity and in two different formats. The available data is summarized below in order of increasing detail and size. For each row, click on the `List` to see a full list of files and their associated URLs.

| Data                                            | Format | Files                                   | Uses                                                     |
| ----------------------------------------------- | ------ | --------------------------------------- | -------------------------------------------------------- |
| Medians over time and medians over GCMs         | CSV    | [Southeastern Europe](/data/southeastern-europe/csv_locations.md) [Central Asia](/data/central-asia/csv_locations.md)          | Common summary statistics of extreme heat                |
| Medians over time for the full ensemble of GCMs | Zarr   | [Southeastern Europe](/data/southeastern-europe/zarr_summary_locations.md) [Central Asia](/data/central-asia/zarr_summary_locations.md)| Inspecting variability of summary statistics across GCMs |
| Daily projections for the full ensemble of GCMs | Zarr   | [Southeastern Europe](/data/southeastern-europe/zarr_daily_locations.md)  [Central Asia](/data/central-asia/zarr_daily_locations.md)  | Inspecting full daily time series across GCMs            |

## about us

CarbonPlan is a non-profit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. [Find out more at carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/extreme-heat/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
