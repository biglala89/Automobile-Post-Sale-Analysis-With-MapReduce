## Post-Sale-Automobile-Report

### Objective
The goal of this mini project is to use a MapReduce program to produce a report of the total number of accidents per make and year of the car.

### Data
The sample data is from an automobile tracking platform that tracks the history of important incidents after the initial sale of a new vehicle. Such incidents include subsequent private sales, repairs, and accident reports. The platform provides a good reference for second-hand buyers to understand the vehicles they are interested in.

| Column | Type |
| --- | --- |
| incident_id | INT |
| incident_type | STRING (I: initial sale, A: accident, R: repair) |
| vin_number | STRING |
| make | STRING (The brand of the car, only populated with incident type “I”) |
| model | STRING (The model of the car, only populated with incident type “I”) |
| year | STRING (The year of the car, only populated with incident type “I”) |
| incident_date | DATE (The year of the car, only populated with incident type “I”) |
| description | STRING |

### Data enrichment
The original sample dataset is quite small. To fully test the power of MapReduce in a distributed environment, a much richer dataset is always preferred. Therefore, under the **_data mocking module_**, I have developed a program to enrich the original dataset to a user-customizable number of records.
To generate more data, use
```bash
cd data_mocking/scripts/
```
```python
python data_mocking.py --gen_n 10000
```
Refer to data_mocking module to see details.

### Running the job
The actual job is done in a Hadoop distributed system. A Hortonworks Hadoop Sandbox was used to run and test the program. The sandbox is a pre-configured virtual machine that has all necessary installation completed. 
If Hadoop and Sandbox are not set, simply use the bash pipeline command to simulate what happens in MapReduce. This will not work in distributed mode, but it can be used to test the functionality.

```bash
cat source_data/data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py | sort | python autoinc_reducer2.py
```

The result should look similar to this:
<br>('A4 2017', 834)
<br>('A7 2019', 881)
<br>('Beetle 2014', 947)
<br>('Bentayga 2013', 869)
<br>('Optima 2019', 746)
<br>('Prius 2019', 793)
<br>('Q8 2019', 775)
<br>('QX30 2014', 828)
<br>('S5 2012', 808)
<br>('S60 2019', 794)
<br>('XJ 2014', 791)
<br>('XT4 2016', 757)
<br>('Yaris 2018', 754)
<br>('Yukon XL 2016', 827)
<br>('Z4 2019', 822)
