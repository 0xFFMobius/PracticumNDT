# Practicum 2 (23S8W2) Progress Report
## Capture and Processing of Non-Destructive Testing Data
NAME: Bryce Lakamp

GITHUB REPOSITORY LINK: https://github.com/0xFFMobius/PracticumNDT

WEEK: 2

## Project Summary
The output results of new non-destructive testing equipment needs to be analyzed over time to determine if process or equipment shifts occur. By establishing a base line "fingerprint" of known defects in a calibration piece, I intend to perform classification machine learning to look for degradation of signals or equipment. 

The data contains spacial locations of defects the measured intensity, and the probe which was used to capture the result. There are a substantial number of defects in the calibration pieces, but only a small number of other factors. Ideally I need to be able to state that two (or more) separate measurements of a single defect are the same even though they have some reasonable variation (intensity and position). 

## Milestones
* ~~Generate Project Proposal~~ (Done)
* ~~Validate data availability~~ (Done)
* ~~Generate connection system~~ (Done)
* ~~Review Database UML~~ (Done)
* ~~Write functions for data retrieval using API~~ (Done)

To Do:
* Retrieve full data set
* Save merged data to local system
* Data review
* Data cleaning
* Deduplication
* EDA
* Distributions
* Correlations
* Feature selection for machine learning
* Additional exploration as needed
* Determine classification model
* Model development
  * Hyper parameter optimization
* Visualizations
* Generation of final presentation