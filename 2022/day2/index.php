<?php
$input = file_get_contents('./input');
$ents = preg_split('/\n/' , $input);
function sum($carriage,$item) {
	if (!empty($item)) {
		switch($item){
			case "A X": $result = 3+1; break;
			case "A Y": $result = 6+2; break;
			case "A Z": $result = 0+3; break;
			case "B X": $result = 0+1; break;
			case "B Y": $result = 3+2; break;
			case "B Z": $result = 6+3; break;
			case "C X": $result = 6+1; break;
			case "C Y": $result = 0+2; break;
			case "C Z": $result = 3+3; break;
		}
		$carriage[]=$result;
	}
	return $carriage;
}

function sum2($carriage,$item) {
	if (!empty($item)) {
		switch($item){
			case "A X": $result = 0+3; break;
			case "B X": $result = 0+1; break;
			case "C X": $result = 0+2; break;
			case "A Y": $result = 3+1; break;
			case "B Y": $result = 3+2; break;
			case "C Y": $result = 3+3; break;
			case "A Z": $result = 6+2; break;
			case "B Z": $result = 6+3; break;
			case "C Z": $result = 6+1; break;
		}
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
