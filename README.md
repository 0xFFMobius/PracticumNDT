# Interfacing and Analyzing NDT Signals
In completion of the requirements for M.S. Data Science, Data Engineering emphasis I present a project to collect process signals from a third-party vendor and summarize signal characteristics for future process analysis.

# Background
Non-destructive testing (NDT), including ultrasonic (UT) and eddy current (EC) is required by customer specification to be performed on many steel sections and shapes. The intent of this testing is to inspect the surface and internal steel to look for defects which would affect the performance of the product in service. Defects may be present in the material, but they must be larger than a detectable threshold, and distinguishable from background noise. 

To support equipment calibration, sample pieces are manufactured with known defect sizes and locations. These test pieces are regularly processed by the inspection equipment to validate the equipment will be capable of seeing a defect in final product.

# Project Objective
The output results of new non-destructive testing equipment needs to be analyzed over time to determine if process or equipment shifts occur. Process shifts will be detrimental to the company's ability to certify product, and may induce additional rework.

Along with the new NDT inspection equipment we have a systems integrator which will be tracking the product going through the inspection equipment. The integrator will be relaying instructions to the equipment, including the identifiers, classifications and inspection recipes. They will obtain some basic information from the inspection equipment. 

I will be using some of this information to perform API queries to the inspection equipment in order to obtain and analyze results. 

* Use API to obtain streaming data from the NDT inspection equipment
* Use SQL queries to obtain data not available via API from it's SQL database
* Use SQL queries to obtain data from system integrator for piece tracking information
* Perform analysis on byte stream data to extract relevant testing characteristics
* Define new table structure and upload resulting characteristic results
* Perform basic statistical process control analysis on characteristic results

# Project Proposal
The proposal for the project scope and applicability to coursework can be found at [Project Proposal](project_proposal.md).

# Available Data
A sample database has been provided by the original equipment manufacturer as part of the factory acceptance testing. Test runs for a single sample with known targets (defects) has been processed multiple times. This data should be sufficient to support the extractions and analyses needed as a demonstration of concept. 

A remote test database has been set up by the integrator to provide the current database structures they will be using in production. I have permissions to modify and upload additional structures in support of this project efforts.

# Project Updates
This project was completed over 8 weeks in the spring of 2023. Progress reports can be found here:
* [Week 2 project update](project_reports/week_2.md)
* [Week 3 project update](project_reports/week_3.md)
* [Week 4 project update](project_reports/week_4.md)
* [Week 5 project update](project_reports/week_5.md)
<!--* [Week 6 project update](project_reports/week_6.md)
* [Week 7 project update](project_reports/week_7.md)
* -->