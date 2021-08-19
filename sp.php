<?php

if(isset($_GET["test"])){
	$command = escapeshellcmd('/usr/bin/python3 /home/milesproject2021/sentence_analyzer.py ' . $_GET["test"]);
	$output = shell_exec($command);
	//$output = shell_exec('/root/anaconda3/bin/python3 /home/milesproject2021/sentence_analyzer.py ' . $_GET["test"] );
	echo $output;
}
/*
$command = escapeshellcmd('/usr/bin/python3 /home/milesproject2021/sentence_analyzer.py');
$output = shell_exec($command);
echo $output;
/*
#echo 'Current script owner: ' . get_current_user();
$current_user = trim(shell_exec('whoami'));
echo $current_user;
 */
?>
