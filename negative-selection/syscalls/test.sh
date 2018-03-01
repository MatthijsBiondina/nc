cat snd-cert/snd-cert.{1..3}.test > snd.test
cat snd-cert/snd-cert.{1..3}.labels > snd.labels
# java -jar negsel2.jar -alphabet file://snd-cert.alpha -self snd-cert/snd-cert.train -n 10 -r 3 -c -l < english.test > english.scores
# for lang in hiligaynon middle-english plautdietsch xhosa; do
# 	rm scores.txt
# 	for r in {1..9}; do
# 	    java -jar negsel2.jar -self snd-unm.train -n 10 -r $r -c -l < english.test > english.scores
# 	    java -jar negsel2.jar -self english.train -n 10 -r $r -c -l < lang/$lang.txt > other.scores
# 	    python3 AUC.py >> scores.txt
# 	done
# 	python3 plotIt.py $lang
# done
