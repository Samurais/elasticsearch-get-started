#! /bin/bash 
###########################################
# analysis data
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
echo "Generate conversations and corpus ..."
cd $baseDir
source ~/venv-py2/bin/activate
python insuranceqa_run.py \
    --generateConversations \
    --generateCorpus \
