gunzip -c ~/Code/MCB185/data/dictionary.gz | grep a | grep -v -E "[^uomtfca]+"

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep b | grep -v -E "[^ailnrtb]+"

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep m | grep -v -E "[^caonidm]+"

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep z | grep -v -E "[znorgia]+"

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep diatoms

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep urochordates

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep nematodes

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep fungi

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep insects

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep plants

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep vertebratessh 
