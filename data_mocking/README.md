## Vehicle Data Mocking

The original dataset is fairly small, in which case data enrichment is needed to produce more data to fully test the effectiveness of map-reduce concept. Therefore, I have developed the program to generate raw data based on the original dataset. 

To run the program, use 
```python
python data_mocking.py --gen_n 10000
```
to generate 10,000 unique vehicles VINs. If no argument is provided, a default value of 500 is used.
* Note:
    1. there could be a random number of records per VIN, the number of records (capped at 10 per VIN) is determined by a random number generator every time a new VIN is generated. 
    2. Incident_date and description are left out of the equation as they are irrelevant to the analysis.
    3. If you find two vehicles (make, model, year) with the same VIN, congratulations you just hit the jackpot!
