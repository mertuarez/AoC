<?php
$input = file_get_contents('./input');
$ents = preg_split('/\n/' , $input);
function myCount($txt){
	$pos="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	$prio=array();
	for($i=0; $i<strlen($txt);$i++) {
		$val=strpos($pos, $txt[$i])+1;
		if (!in_array($val,$prio)) {
				$prio[] = $val;
		}
	}
	return array_sum($prio);
}

function mySum($carriage,$item) {
	if (!empty($item)) {
		$txt = preg_replace('/[^'.substr($item,strlen($item)/2).']/', '', substr($item,0,strlen($item)/2));
		$result=myCount($txt);
		$carriage[]=$result;
	}
	return $carriage;
}

function mySum2($items) {
	$result=array();
	for($i=0;$i<count($items)-3;$i+=3){
		$val = preg_replace('/[^'.$items[$i+1].']/', '', $items[$i]);
		$val = preg_replace('/[^'.$items[$i+2].']/', '', $val);
		$result[] = myCount($val);
	}
	return $result;
}

//part 1
$red = array_reduce($ents,"mySum");
var_dump(array_sum($red));

//part2
$red = mySum2($ents);
var_dump(array_sum($red));

