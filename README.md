## Post-Sale-Automobile-Report-Hadoop-MapReduce

You can use the Bash pipeline function to simulate what happens in MapReduce. This will not
work in distributed mode, but it can be used to test your functionality.

```bash
cat data.csv | autoinc_mapper1.py | sort | autoinc_reducer1.py | autoinc_mapper2.py | sort |
autoinc_reducer2.py
```
