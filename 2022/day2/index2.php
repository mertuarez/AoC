<?php
$input = file_get_contents('./input');
$ents = preg_split('/\n/' , $input);
function sum($carriage,$item) {
	if (!empty($item)) {
		$vals = array("A"=>1,"B"=>2,"C"=>3,"X"=>1,"Y"=>2,"Z"=>3,);
		$result = $vals[$item[2]];
		$result += $vals[$item[0]] - $vals[$item[2]] == +0 ? 3 : 0;
		$result += $vals[$item[0]] - $vals[$item[2]] == -1 ? 6 : 0;
		$result += $vals[$item[0]] - $vals[$item[2]] == +2 ? 6 : 0;
		$carriage[]=$result;
	}
	return $carriage;
}

function sum2($carriage,$item) {
	if (!empty($item)) {
		$vals = array(1,2,3,"A"=>0,"B"=>1,"C"=>2);
		$index = $vals[$item[0]];
		$result = $item[2] == "X" ? 0+$vals[($index+2)%3] : 0;
		$result = $item[2] == "Y" ? 3+$vals[$index] : $result;
		$result = $item[2] == "Z" ? 6+$vals[($index+1)%3] : $result;
		$carriage[]=$result;
	}
	return $carriage;
}

//part 1
$red = array_reduce($ents,"sum");
var_dump(array_sum($red));

//part 2
$red = array_reduce($ents,"sum2");
var_dump(array_sum($red));
