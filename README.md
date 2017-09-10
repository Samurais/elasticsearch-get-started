# elasticsearch-get-started

## Deps

* docker 
* docker compose
* python2
* pip

## Run

```
docker-compose up
open http://localhost:9200/_plugin/head/ # verify
```

## Import data
```
cd tools
pip install -r Requirement.txt
python insuranceqa_run.py --pipe-to-es
```

## Query
```
cd tools
python insuranceqa_run.py --query="为什么要获得医疗保险补充保险"
```

## Quick get started
To get started quickly, use ```dev.sh```.
```
scripts/dev.sh
```

# LICENSE
[Apache 2.0](./LICENSE)