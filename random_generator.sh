RANDOM=$$
> rand_num.txt
for i in `seq 10000`
do
    echo $RANDOM >>rand.txt
done

> rand_word.txt
for i in `seq 10000`
do
    perl -e 'open IN, "</usr/share/dict/words";rand($.) < 1 && ($n=$_) while <IN>;print $n' >>rand2.txt
done

paste rand.txt rand2.txt | column -s $'\t' -t > random_key_value.txt
