Commands to run
```bash
docker build -t log_to_csv . 
docker run -t -i --volume /path/where/log/is/located/:/data/ --env INPUT_FILE=/data/access.log log_to_csv
```


Command to run unittests
```bash
docker build -t log_to_csv . 
docker run -t -i --entrypoint "/scripts/run_tests.sh" log_to_csv
```

