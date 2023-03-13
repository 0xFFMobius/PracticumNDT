# Project Proposal MSDS696

## Contact Information
Bryce Lakamp

blakamp@regis.edu

(719) 248-2456

https://github.com/0xFFMobius/PracticumNDT

# Interfacing and Analyzing NDT Signals

## Project Description
The output results of new non-destructive testing equipment needs to be analyzed over time to determine if process or equipment shifts occur. Process shifts will be detrimental to the company's ability to certify product, and may require additional rework. The project's focus will be on the development of the data-pipeline over the determination of process shifts. 

The inspection equipment allows for querying of some scalar test results using a socket based API. These available results are not representative of all needed parameters which are important the business operations, (validating the inspection system is healthy). The raw stream data of the tests must also be extracted and processed for statistical characteristics. These characteristics will be tracked over time to look for process shifts. 

The raw data streams and interface have similarities to big data. The communications, analysis, data storage and tracking all need to be developed. These steps will include drawing from multiple data sources (TCP socket API, SQL), and publication of transformed data an SQL database in real time. Basic visualizations for determining process shifts should be included. 

## Data Source
There are 72 pieces in the test database. Some characteristics will be accessed using the TCP socket API interface (sending and receiving JSON strings). Other data will make direct database queries to the underlying MS SQL Server. The API can also be used to send byte raw stream data of the actual testing response over TCP. Each piece has multiple streams (15 UT and 39 EC) looking for different targets. This is enough data to produce a proof of concept evaluation process.

## Data Description
The JSON data will need to be parsed for relevant fields to associate with the byte stream results. A mixture of categorical and continuous data will need to be stored. After analyzing stream results, continuous data points and key values (IDs) will be uploaded to a separate MS SQL Server. This processed data will be the basis for equipment health determination. 

## Analysis Approach
With the emphasis on the data pipeline, the analysis will not be as involved as a typical data science project. Threshold determination, low pass and high pass band filtering to generate categorical pass/fail for the byte stream. 

If time allows, using a nearest neighbors algorithm (or similar unsupervised classification algorithm) to generate a defect "fingerprint" would be useful. As the test piece is re-run it should have the same fingerprint. If there is low variation in the training set, deviations should be identified and addressed before complete failure occurs. 

# Possible Project Complications
The test database and tracking database have no documentation. To find relevant information, I will have to examine individual table structures, and develop my own UML. The API documentation is complete enough to get started, but more advanced usage will require effort. 


# Project Timeline
Week 1:
* Select project
* Start to explore and document target database structures & table interactions

Week 2:
* Complete database documentation
* Write SQL creation scripts for output data tables

Week 3:
* Write download interface from NDT equipment for SQL and JSON interfaces

Week 4:
* Generate analysis files for stream data pulling required characteristics

Week 5:
* Write upload scripts for distilled characteristics 
* Write batch scripts to process data in bulk and realtime

Week 6:
* Explore tracking analysis methods either nearest-neighbor finger print or statistical process control

Week 7:
* Continue tracking analysis method

Week 8:
* Clean up documentation
* Write final presentation
