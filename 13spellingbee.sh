 #gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E ".{4,}" | grep -E ".*r.*" | grep -v "b" | grep -v "d" | grep -v "e" | grep -v "f" | grep -v "g" | grep -v "h" | grep -v "j" | grep -v "k" | grep -v "l" | grep -v "m" | grep -v "p" | grep -v "q" | grep -v "s" | grep -v "t" | grep -v "u" | grep -v "v" | grep -v "w" | grep -v "x" | grep -v "y"
 # This  was a round about way of doing the second one
 gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -E "[zonica]+" | grep -v -E "[^zonicar]+" | grep -E ".{4,}"
