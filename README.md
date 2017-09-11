# elasticsearch-get-started

## Deps

* docker v17.*
* docker-compose v1.14.*
* Python v2.7
* virtualenv v15.1.0

## Run

```
docker-compose up
open http://localhost:9200/_plugin/head/ # verify
```

## Import data
```
cd iqabot.v1
pip install -r Requirement.txt
python bot.py --pipe-to-es
```

## Query
```
cd iqabot.v1
python bot.py --query="为什么要获得医疗保险补充保险"
```

## Quick Get Started
To get started quickly, use ```dev.sh```.
```
iqabot.v1/setup.sh
```

# LICENSE
[Apache 2.0](./LICENSE)