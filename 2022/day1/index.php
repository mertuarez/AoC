<?php
$input = file_get_contents('./input');
$ents = preg_split('/\n\n/' , $input);
function sum($a,$b) {
	$a[]=array_sum(preg_split('/\n/' , $b));
	return $a;
}

$red = array_reduce($ents,"sum");
var_dump(max($red));
