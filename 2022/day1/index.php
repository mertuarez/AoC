<?php
$input = file_get_contents('./input');
$ents = preg_split('/\n\n/' , $input);
function sum($a,$b) {
	$a[]=array_sum(preg_split('/\n/' , $b));
	return $a;
}

//part 1
$red = array_reduce($ents,"sum");
var_dump(max($red));
//part2
rsort($red);
var_dump($red[0]+$red[1]+$red[2]);
